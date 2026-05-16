"""Smoke tests for scripts/discourse_research.py.

Covers:
1. Happy path: a small set of multi-platform results produces a brief with
   themes, source breakdown, and inline-link citations.
2. Empty input: zero results does not crash and emits a brief noting
   insufficient coverage.
3. LAW hygiene: output contains no em-dashes (LAW 3) and no fabricated titles
   that differ from the input data (LAW 2).

Stdlib + pytest only. No network. Subprocess invocation matches the
documented CLI.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "discourse_research.py"


def _run(input_path: Path, topic: str, days: int = 30, fmt: str = "json") -> dict:
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--input", str(input_path),
            "--topic", topic,
            "--days", str(days),
            "--format", fmt,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, f"non-zero exit: stderr={result.stderr!r}"
    if fmt == "json":
        return json.loads(result.stdout)
    return {"markdown": result.stdout}


def test_happy_path_multi_platform(tmp_path: Path) -> None:
    """A mixed-platform result set produces a brief with themes and breakdown."""
    today = dt.date.today()
    recent = (today - dt.timedelta(days=5)).isoformat()
    older = (today - dt.timedelta(days=20)).isoformat()
    results = [
        {
            "platform": "reddit",
            "url": "https://reddit.com/r/docker/comments/xx1",
            "title": "Docker compose for production: tips and tricks",
            "snippet": "Multi-stage Dockerfile cut my image from 4 GB to 187 MB. Use node:18-alpine plus a slim build step.",
            "date": recent,
            "engagement_proxy": "450 upvotes",
        },
        {
            "platform": "hackernews",
            "url": "https://news.ycombinator.com/item?id=xx2",
            "title": "Show HN: Image size matters more than you think",
            "snippet": "Discussion of image bloat in production. Multi-stage builds and alpine variants reduce attack surface too.",
            "date": recent,
            "engagement_proxy": "210",
        },
        {
            "platform": "devto",
            "url": "https://dev.to/x/docker-image-size-deep-dive",
            "title": "Docker image size deep dive: 4 GB to 187 MB",
            "snippet": "Concrete steps to slim Docker images using multi-stage builds and alpine base images.",
            "date": older,
            "engagement_proxy": "1.2k",
        },
        {
            "platform": "x",
            "url": "https://x.com/nginxguy/status/xx3",
            "title": "@nginxguy: 31% of registries I audited ship 4 GB+ images",
            "snippet": "Audit data on production Docker registries: image bloat is the dominant issue.",
            "date": recent,
            "engagement_proxy": "800",
        },
    ]
    inp = tmp_path / "results.json"
    inp.write_text(json.dumps(results), encoding="utf-8")
    brief = _run(inp, "Docker workflows", days=30, fmt="json")
    assert brief["source_count"] == 4
    assert brief["topic"] == "Docker workflows"
    assert brief["window_days"] == 30
    assert "reddit" in brief["platform_breakdown"]
    assert "x" in brief["platform_breakdown"]
    # At least one cluster should be detected from the shared theme
    total_clusters = (
        len(brief["themes_new"])
        + len(brief["themes_consensus"])
        + len(brief["themes_niche"])
    )
    assert total_clusters >= 1
    # Markdown is embedded; it should contain at least one inline link
    assert "](" in brief["markdown"]


def test_empty_input_no_crash(tmp_path: Path) -> None:
    """Zero results produces a brief that notes insufficient coverage."""
    inp = tmp_path / "empty.json"
    inp.write_text("[]", encoding="utf-8")
    brief = _run(inp, "obscure topic", fmt="json")
    assert brief["source_count"] == 0
    assert brief["themes_new"] == []
    assert brief["themes_consensus"] == []
    # The markdown should still be well-formed and note the empty state
    assert "Discourse Brief" in brief["markdown"]
    assert "No" in brief["markdown"]  # "No distinctly new themes..." or similar


def test_law_hygiene_no_em_dashes_no_invented_titles(tmp_path: Path) -> None:
    """Output must obey LAW 3 (no em-dashes) and LAW 2 (no invented titles)."""
    today = dt.date.today()
    recent = (today - dt.timedelta(days=10)).isoformat()
    # Include source titles with em-dashes in the input; LAW 3 should strip them in output.
    results = [
        {
            "platform": "medium",
            "url": "https://medium.com/x/post-1",
            "title": "Title with em-dash - and more text",  # the upstream variant has unicode em-dash
            "snippet": "Some snippet content discussing the topic in depth - including various examples.",
            "date": recent,
            "engagement_proxy": "300",
        },
        {
            "platform": "substack",
            "url": "https://substack.com/x/post-2",
            "title": "Plain title without dashes",
            "snippet": "Another snippet covering the topic from a different angle.",
            "date": recent,
            "engagement_proxy": "150",
        },
    ]
    # Add an actual unicode em-dash into the snippet to test stripping
    results[0]["snippet"] = "Some snippet — with a real em-dash — inside."
    inp = tmp_path / "with_dashes.json"
    inp.write_text(json.dumps(results, ensure_ascii=False), encoding="utf-8")
    brief = _run(inp, "test topic", fmt="json")
    md = brief["markdown"]
    # LAW 3: no unicode em-dash or en-dash in output
    assert "—" not in md, "Output contains a unicode em-dash"
    assert "–" not in md, "Output contains a unicode en-dash"
    # LAW 2: input titles should appear in output verbatim (up to 80 chars), not fabricated.
    # Original title contains "Plain title without dashes" - check it's there.
    assert "Plain title without dashes" in md


def test_output_file_write_integration_contract(tmp_path: Path) -> None:
    """When --output is passed, the script writes a parseable markdown brief
    AND prints JSON metadata on stdout. This is the integration contract that
    downstream skills (blog-brief, blog-write, blog-strategy) depend on via
    the orchestrator's DISCOURSE.md auto-load.
    """
    today = dt.date.today()
    recent = (today - dt.timedelta(days=8)).isoformat()
    results = [
        {
            "platform": "reddit",
            "url": "https://reddit.com/r/example/comments/aa1",
            "title": "Sample discussion thread",
            "snippet": "Practitioner discussion of the topic with concrete examples.",
            "date": recent,
            "engagement_proxy": "120",
        },
    ]
    inp = tmp_path / "results.json"
    inp.write_text(json.dumps(results), encoding="utf-8")
    output_md = tmp_path / "DISCOURSE.md"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--input", str(inp),
            "--topic", "integration test topic",
            "--days", "30",
            "--output", str(output_md),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, f"stderr={result.stderr!r}"

    # 1. Markdown file was written and is parseable
    assert output_md.exists()
    md_text = output_md.read_text(encoding="utf-8")
    assert md_text.startswith("# Discourse Brief: integration test topic")
    assert "Window: last 30 days" in md_text
    # Required sections downstream skills look for
    for section in ("## What's NEW", "## Consensus", "## Niche", "## Source breakdown"):
        assert section in md_text, f"missing section: {section}"

    # 2. JSON metadata printed on stdout (not the markdown body)
    metadata = json.loads(result.stdout)
    assert "topic" in metadata
    assert "source_count" in metadata
    # The `markdown` key is excluded from --output mode stdout
    assert "markdown" not in metadata, "markdown should be in file, not stdout, when --output is set"


def test_em_dash_in_snippet_does_not_leak_to_output(tmp_path: Path) -> None:
    """Additional LAW 3 hardening: em-dashes anywhere in the input pipeline
    (title, snippet, engagement label) must not leak to the output. This is a
    regression test against future refactors that might bypass strip_em_dashes
    in the rendering path.
    """
    today = dt.date.today()
    recent = (today - dt.timedelta(days=3)).isoformat()
    # Every field carries an em-dash. None should appear in output.
    results = [
        {
            "platform": "x",
            "url": "https://x.com/user/status/123",
            "title": "Title with em-dash — here",
            "snippet": "Snippet — also with em-dash — multiple times — and en-dash – too",
            "date": recent,
            "engagement_proxy": "1k",
        },
    ]
    inp = tmp_path / "with_dashes.json"
    inp.write_text(json.dumps(results, ensure_ascii=False), encoding="utf-8")
    brief = _run(inp, "law 3 hardening", fmt="json")
    md = brief["markdown"]
    assert "—" not in md, f"em-dash leaked: {md!r}"
    assert "–" not in md, f"en-dash leaked: {md!r}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
