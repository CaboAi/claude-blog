# Editorial Heuristics: Ordinal Scoring Rubric (0 to 4)

The existing 100-point system in `quality-scoring.md` (sibling file in this directory) tells you a post scores 78. This ordinal rubric tells you **which sections are P0 blockers and which are P3 polish**. They are complementary, not competing; run both when an editorial review needs to be actionable.

Adapted from Nielsen's 10 Usability Heuristics as applied in the impeccable plugin (Paul Bakaus, Apache 2.0). The original scores UI quality; this version scores editorial quality.

---

## How to score

Each heuristic gets one of five scores:

| Score | Meaning |
|---|---|
| 0 | Absent or actively wrong |
| 1 | Major gaps; most checks fail |
| 2 | Mixed; some checks pass, important ones do not |
| 3 | Good; most checks pass with minor gaps |
| 4 | Genuinely excellent. A 4 is rare. |

Be honest. A 4 means "would cite this in a meta-review of best-practice blog craft," not "good enough to ship." Most strong production posts land between 2 and 3 across the board.

Each finding gets a severity tag:

| Tag | Meaning | When to use |
|---|---|---|
| P0 | Blocking. Do not publish. | Fabricated stat, broken structure, plagiarism risk, factually wrong |
| P1 | Ship-blocking polish. Fix before publish. | Missing source on a load-bearing claim, broken citation, AI-detection signal |
| P2 | Should fix soon. Publish then iterate. | Weak heading, missing schema, suboptimal answer-first opener |
| P3 | Nice to have. | Cosmetic, marginal SEO gain, stylistic preference |

A 0 or 1 on any heuristic should generate at least one P0 or P1.

---

## Mapping to Nielsen's original heuristics

For readers familiar with Nielsen's UI heuristics, here is the translation:

| Nielsen original (UI) | Editorial adaptation |
|---|---|
| 1. Visibility of system status | 1. Visibility of intent |
| 2. Match between system and the real world | 2. Match between heading and section content |
| 3. User control and freedom | 3. Reader control and exit |
| 4. Consistency and standards | 4. Consistency of voice and standards |
| 5. Error prevention | 5. Fabricated-stat prevention |
| 6. Recognition rather than recall | 6. Recognition over recall |
| 7. Flexibility and efficiency of use | 7. Flexibility for skimmer vs deep reader |
| 8. Aesthetic and minimalist design | 8. Aesthetic and information-density discipline |
| 9. Help users recognize, diagnose, and recover from errors | 9. Failure-recovery copy |
| 10. Help and documentation | 10. Help, sources, and related documentation |

Nielsen reference: Jakob Nielsen, "10 Usability Heuristics for User Interface Design," Nielsen Norman Group, 1994 (revised 2020). https://www.nngroup.com/articles/ten-usability-heuristics/

## The 10 Editorial Heuristics

### 1. Visibility of intent (the post tells the reader what it is)

Adapted from Nielsen's "Visibility of system status." The reader should know within 5 seconds what the post is, what they will learn, and roughly how long it takes.

**Check for**:
- Title accurately reflects body content (no clickbait drift)
- Description / meta description previews real substance
- Summary box ("Key Takeaways" / "TL;DR") at the top with 3 to 5 bullets
- Estimated reading time or word count visible
- H1 matches title (within reason)

| Score | Criteria |
|---|---|
| 0 | Title misleading or absent; no summary; reader has to infer the topic |
| 1 | Title present; nothing else orients the reader |
| 2 | Title and meta present; no summary box |
| 3 | Summary present but generic or low-information |
| 4 | Title, meta, and summary all reinforce a specific promise the body keeps |

### 2. Match between heading and section content

Adapted from "Match between system and real world." A heading is a contract; the section under it should deliver what the heading promises, in the order the reader expects.

**Check for**:
- Each H2 promise is fulfilled in the first 100 words of that section
- No bait-and-switch (heading says "compare X and Y," body only discusses X)
- Information order matches the cognitive sequence (problem then solution, not solution then problem)
- Domain terms used as the audience uses them (not the model's preferred synonym)

| Score | Criteria |
|---|---|
| 0 | Headings disconnected from section content |
| 1 | Major mismatch on more than half the H2s |
| 2 | Some H2s fulfill; others bury or redirect |
| 3 | Most sections deliver on their heading; minor reordering needed |
| 4 | Every H2 is a contract the section keeps in the opening paragraph |

### 3. Reader control and exit

Adapted from "User control and freedom." Long-form prose can trap the reader. Good blogs let them scan, jump, and bail without losing the thread.

**Check for**:
- Table of contents present for posts over 1,500 words
- Internal jump links between sections
- Each H2 self-contained enough to read independently (passage-level citability)
- Clear "what next" at the end (related posts, downstream action)

| Score | Criteria |
|---|---|
| 0 | One wall of text; no navigation |
| 1 | Sections exist but readers cannot skim |
| 2 | Navigation partial; some sections require previous context |
| 3 | TOC present, most sections standalone |
| 4 | Skim-readable end to end with self-contained sections, clear exits, downstream paths |

### 4. Consistency of voice and standards

Adapted from "Consistency and standards." Within a post, terminology, tone, formatting, and structural patterns should not drift.

**Check for**:
- Same term used for the same concept throughout (not "AI" then "LLM" then "model" then "system" arbitrarily)
- Sentence cadence stable (no jarring switches between conversational and academic)
- Bullet vs prose decision applied consistently in similar sections
- Citation format identical across all references
- Heading capitalization style consistent

| Score | Criteria |
|---|---|
| 0 | Reads like three drafts stitched together |
| 1 | Multiple voice or terminology shifts |
| 2 | Mostly consistent; occasional drift |
| 3 | One or two minor inconsistencies |
| 4 | Reads as one author writing in one sitting |

### 5. Fabricated-stat prevention

Adapted from "Error prevention." Better than caught-after-the-fact retractions is structure that prevents fabricated or unsourced data from entering the draft.

**Check for**:
- Every numeric claim has a named source within the same paragraph
- Every source URL is reachable (tier 1 to 3)
- Year anchor in prose for time-sensitive claims (FLOW evidence triple)
- Retrieval date on the source citation
- No vague "studies show" or "experts agree" without naming who

| Score | Criteria |
|---|---|
| 0 | Multiple unsourced numeric claims (P0) |
| 1 | Half of numeric claims unsourced |
| 2 | Most sourced; one or two suspicious |
| 3 | All sourced; minor gaps in retrieval dates |
| 4 | Full FLOW evidence triple on every statistic |

### 6. Recognition over recall (the reader does not memorize)

Adapted from "Recognition rather than recall." The reader should not have to remember what was said three sections ago to follow the current paragraph.

**Check for**:
- Key terms redefined or aliased on reuse if introduced more than 500 words earlier
- Comparison tables for X-vs-Y content (not buried prose)
- Visual aids (charts, images) where data is dense
- Repeated context cues rather than implicit reference
- Numbered steps numbered in body, not just lists

| Score | Criteria |
|---|---|
| 0 | Reader must hold many threads to follow |
| 1 | High memory load throughout |
| 2 | Some sections require backtracking |
| 3 | Mostly recognition-friendly |
| 4 | Every section can be entered cold |

### 7. Flexibility for skimmer vs deep reader

Adapted from "Flexibility and efficiency of use." The post should reward both modes: the executive who scans bullets and headings, and the practitioner who reads end to end.

**Check for**:
- Bold lead-ins on key points for skimmability
- Pull quotes or call-out boxes for high-leverage claims
- Each H2 opener is a 40 to 60 word answer-first paragraph
- Lists used where lists are right; prose where prose is right
- FAQ section for jump-look answers

| Score | Criteria |
|---|---|
| 0 | Only readable end-to-end; no skim affordances at all |
| 1 | Some headings, but no bold lead-ins, pull quotes, or answer-first openers |
| 2 | Skim affordances in some sections; missing FAQ or answer-first opener |
| 3 | Most sections have skim affordances; one of (answer-first opener, FAQ, pull quotes) missing |
| 4 | Rewards skimmer and deep reader equally: bold lead-ins, answer-first openers on every H2, FAQ, pull quotes where leverage exists |

### 8. Aesthetic and information-density discipline

Adapted from "Aesthetic and minimalist design." Long does not equal valuable. Every paragraph should earn its place; padding is a slop signal.

**Check for**:
- No paragraph over 150 words
- No introduction that delays the first substantive claim by more than 150 words
- No SEO-padded conclusion ("In summary, we have covered...")
- No filler transitions ("Now, let's discuss...")
- Word count appropriate to topic (1,500 word listicle topic should not be 3,500 words)

| Score | Criteria |
|---|---|
| 0 | Padding pervasive; intro buries the lede; conclusion restates the post |
| 1 | Several paragraphs over 150 words; multiple filler transitions |
| 2 | One bloat axis present (e.g. SEO-padded conclusion, or long intro, or word-count drift) |
| 3 | Minor bloat (1 to 2 long paragraphs or one filler transition); otherwise tight |
| 4 | Every paragraph earns its place; no padding; word count matches topic scope |

### 9. Failure-recovery copy (broken paths fail gracefully)

Adapted from "Help users recognize, diagnose, and recover from errors." The post must handle reader confusion or partial knowledge.

**Check for**:
- Glossary or inline definitions for jargon
- "If you are new to X, read this first" links
- Clearly marked "for advanced readers" sections if they exist
- Examples for every abstract concept
- Acknowledgement of when a technique does not apply

| Score | Criteria |
|---|---|
| 0 | Newcomers will bounce; no definitions; abstract claims without examples |
| 1 | Jargon undefined in most cases; few examples |
| 2 | Some jargon defined; examples present for half of abstract claims |
| 3 | Most jargon defined or aliased; examples for most abstract concepts |
| 4 | Graceful for every audience tier: glossary or inline definitions, examples for every abstract concept, audience-tier signposts, scope-of-applicability notes |

### 10. Help, sources, and related documentation

Adapted from "Help and documentation." Even the best post is one node in a knowledge graph.

**Check for**:
- 3 to 10 contextual internal links to related posts
- 3 to 8 outbound links to tier 1 to 3 sources
- Author bio with credentials and contact path
- Last-updated date visible
- Related-reads section at the end

| Score | Criteria |
|---|---|
| 0 | Isolated content; zero internal links; no author bio; no outbound sources |
| 1 | One or two internal links; author bio thin; few sources |
| 2 | Some links and a basic bio, but missing related-reads or last-updated date |
| 3 | Most signals present; minor gap (e.g. only 2 internal links, or related-reads but no last-updated date) |
| 4 | Fully embedded in a content graph: 3+ internal links, 3+ outbound tier 1 to 3 sources, full author bio, last-updated date, related-reads section |

---

## Reporting format

```
## Editorial Heuristics Report: [Title]

| # | Heuristic | Score | Severity of gap | Note |
|---|---|---|---|---|
| 1 | Visibility of intent | 3 | P2 | Summary box generic; tighten the promise |
| 2 | Heading-content match | 4 | (none) | Every H2 fulfills in opener |
| 3 | Reader control | 2 | P1 | No TOC on 2,400-word post |
| 4 | Voice consistency | 3 | P3 | One paragraph shifts to academic |
| 5 | Fabricated-stat prevention | 4 | (none) | All sources verified, FLOW triple present |
| 6 | Recognition over recall | 2 | P2 | "Type-Token Ratio" used 4 times without aliasing |
| 7 | Skim vs deep flexibility | 3 | P3 | Bold lead-ins missing from 3 sections |
| 8 | Aesthetic discipline | 4 | (none) | No padding |
| 9 | Failure-recovery copy | 2 | P1 | Jargon introduced without definitions in 3 places |
| 10 | Help and sources | 3 | P3 | Only 2 internal links |

### Prioritized fixes
- **P0**: (none)
- **P1**: Add TOC; define jargon (3 spots)
- **P2**: Tighten summary box; alias "TTR" on reuse
- **P3**: Add bold lead-ins; add 2 more internal links; smooth voice shift in paragraph 12
```

The ordinal score is independent of the 100-point system. Both can run on the same post; cross-checking them surfaces inconsistencies (e.g. a 78/100 with three P0s means the 100-point system is missing a load-bearing failure mode).

---

## Attribution

This rubric adapts Nielsen's 10 Usability Heuristics (Jakob Nielsen, NN/g, 1994 revised 2020) via the impeccable plugin's `heuristics-scoring.md` (Paul Bakaus, Apache 2.0, https://github.com/pbakaus/impeccable). The 0 to 4 ordinal scale, P0 to P3 severity model, and per-dimension scoring tables come from the impeccable adaptation. The 10 heuristics are translated from UI ergonomics to editorial ergonomics; see the Nielsen-mapping table at the top of this file for the one-to-one correspondence.
