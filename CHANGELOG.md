# Changelog

## 5.1.0

- **Voice profiles.** After language detection, the skill reads `~/.claude/voice/<lang>.md` if it exists. A profile records the writer's own habits with evidence. It beats Pass 1 and Pass 2, but never the fidelity rules: a phrase, word, dash or sentence length that the profile names is kept, not treated as a tell. Rhetorical rules come back as suggestions only.
- New `references/voice-profile.md`: format, precedence and a template.
- `scripts/ste_check.py` has a new `--voice PATH|auto|none` option (default `auto`). With a profile, it does not report the writer's own phrases and words, it checks dashes against the writer's dash character and rate, and it checks rhythm against the writer's sentence average.

## 5.0.0

- **Connected sentences by default.** In Humanize mode, S1 keeps the reason, condition or result of a statement in the same sentence, and S2 allows descriptions up to about 35 words when commas and clauses carry the structure. A row of short sentences no longer counts as the goal. Strict mode keeps the hard limits of 20 and 25 words.
- **German mode.** The skill detects the language of the text. For German, it reads the new `references/german.md`, which adapts §1, §7, §8, §10, §21, S1, S6 to S10, S12 and S15 and adds German tells. It keeps Perfekt, separable verbs, modal particles, „…“ quotes and the Gedankenstrich used now and then.
- `references/german-research.md` holds the research and sources behind the German rules.
- `scripts/ste_check.py` has a new `--lang auto|en|de` option. It counts words with umlauts correctly, knows German abbreviations and ordinals, and flags German tells. In English, it now also flags a spaced en dash, and its 80% limit for descriptions is 35 words.
- SKILL.md now gives a target for connected prose: an average of 15 to 20 words per sentence in Humanize mode, also when the user asks for "STE". Step 5 checks for a choppy average and for claims that got stronger.
- `german.md` now also catches the staged half form "Das ist nicht nur ärgerlich." without a "sondern".
- The checker flags prose that averages fewer than 12 words per sentence (80% mode only; lists, headings and greetings do not count) and the German half form of §1. It no longer reads "is permanent" as passive.
- New eval `humanize-german-email`. The sentence-length graders now allow 38 words. New graders check connected prose and that nothing is added. The strict runbook grader now accepts "To do X, do Y" steps.

## 4.0.0

- SKILL.md is now 217 lines instead of 573, and about 2,650 words instead of 6,250. Pass 1 and Pass 2 are compact tables with one example per group.
- The full entries for the 26 AI tells moved to `references/ai-tells.md`. The worked example moved to `references/worked-example.md`.
- AGENTS.md now sets a limit of 500 lines for SKILL.md.

## 3.2.1

- LICENSE is now a plain MIT license. The blader/humanizer MIT notice moved to `THIRD_PARTY_NOTICES.md`.

## 3.2.0

- Cut SKILL.md down to what the model needs. The story of Karpathy's post, the note about the graphic and the sources moved out. They are in the README.
- Fixed a sentence in the README that had an AI tell.

## 3.1.0

- Renamed from `humanizer-ste80` to `ste80-humanizer` ("STE80 Humanizer"). Install with `npx skills add Dodaios/ste80-humanizer`. The slash command is now `/ste80-humanizer`.

## 3.0.0

- Rewrote SKILL.md from top to bottom for readability.
- New section "How to read this skill": two passes, §1 to §26 for AI tells, S1 to S15 for structure, the same fields in every entry.
- New section "The method": Karpathy's full tip, the ladder from writing to diagrams, HTML and video, why STE works on LLMs, a table of what 100% and 80% mean, and a note on errors in the graphic that came with his post.
- Pass 1 now covers all 26 patterns of blader/humanizer in the same order (adds hyphenated pairs, vague association, repeated heading, borrowed authority with prestige lists, and others), each with Watch for, Problem, and new Before/After examples. The MIT notice of blader/humanizer is in LICENSE.
- Pass 2 has 15 S-rules, each with 80% and Strict levels and examples.
- New worked example that shows the text after Pass 1 and after Pass 2.
- Return formats now include file mode, embedded mode and review mode.

## 2.0.0

- Renamed from `ste80` to `humanizer-ste80`. The skill is now a general humanizer that uses STE80 as its method.
- New Part 1: 23 AI tells in five groups (staging, rhythm, inflation, formatting, chat residue), inspired by Wikipedia's "Signs of AI writing" and blader/humanizer.
- Part 2: the 23 STE80 structure rules, now in compact form. The full rules with before and after examples moved to `references/ste80-rules.md`.
- New modes: Humanize (default), Light, Strict STE.
- New sections: Voice (match a writing sample), "Human quirks" to keep, contradiction flag in the fidelity rules.
- `ste_check.py` now also flags AI tells: not-X-but-Y, chatbot openers and closers, run-ups, fake depth, stacked hedges, vague authority, "-ing" riders, inflated significance and curly quotes.
- New eval case: `humanize-linkedin-post`.

## 1.0.0

- First release.
- 80% mode (default) and strict mode.
- 23 rules in six groups (sentences, verbs, words, structure, punctuation, what 80% relaxes), with before and after examples.
- Fidelity rules: keep every fact, keep uncertainty at its strength, add nothing.
- `references/word-swaps.md`: plain alternatives in ten groups, including typical LLM vocabulary.
- `references/strict-mode.md`: paraphrased ASD-STE100 Issue 9 rule sections and a final checklist.
- `scripts/ste_check.py`: dependency-free heuristic linter.
