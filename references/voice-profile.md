# Voice profiles

A voice profile describes how one writer writes in one language. It lives outside the skill, at `~/.claude/voice/<lang>.md` (`de.md`, `en.md`), so it stays private. The skill reads it after language detection. `scripts/ste_check.py` reads it too (`--voice auto` is the default).

## Why a profile beats the tells

Pass 1 lists habits that are typical of machine text. Some writers have these habits themselves: they write "let me know", use a dash in every second mail, or close with "Ich hoffe, das hilft". A rewrite that removes these habits makes the text less like the writer, not more human. The profile records them with evidence, so the skill can tell the writer's habit from a machine habit.

Precedence, highest first:

1. Fidelity rules (facts, names, numbers, certainty)
2. A writing sample in the request
3. The voice profile
4. Pass 2 (structure)
5. Pass 1 (tells)

## What a profile holds

Three kinds of rules. Only the first kind belongs to the writer in every text:

| Kind | Examples | What the skill does |
|---|---|---|
| **Voice** | address forms, greetings and closings, preferred words, dash character, sentence length, connectors | Applies them inside each paragraph |
| **Rhetorical** | lists for asks, bottom line first, where the question sits | Lists them as suggestions after the rewrite |
| **Genre** | paragraph length, heading density | Ignores them: they belong to the document type, not the writer |

Write each rule so that a reader can check it against a text, and give the evidence: "Closes with 'Viele Grüße' (36 of 38 mails)" is a rule. "Writes warmly" is not.

## Format

Markdown with front matter. The `overrides` block is for the checker. Keep it flat: numbers, quoted strings and `[lists]`.

```markdown
---
profile: de/base
status: draft | confirmed
corpus: what the rules come from (source, years, number of texts)
overrides:
  sentence_avg: [15, 17]        # the writer's average words per sentence in prose
  dash_char: " - "              # the writer's dash: " - ", " – " or "—"
  dash_per_1k: 8                # dashes per 1,000 words
  keep_phrases: ["Ich hoffe, das hilft", "melde Dich gern"]   # not tells for this writer
  keep_words: ["Business Case", "Update"]                      # no plain-word swap
---

# Base Profile: German

## Address and frame
1. **Capitalise Du, Dich, Ihr, Euch.** 72 of 73.
...

## Structure (rhetorical — propose, do not apply)
19. **Lists with "*" for asks.** 8 of 38 mails.

## Never
- Never add modal particles the writer did not write.
```

## Checker behaviour with a profile

- Phrases and words in `keep_phrases` and `keep_words` are not reported as tells or swaps.
- Dashes: the checker reports a dash character that is not `dash_char`, and a dash rate above 1.5 × `dash_per_1k` (from 300 words or 3 dashes). The general dash rules do not apply.
- Rhythm: the checker reports prose that averages more than 3 words below or 5 words above `sentence_avg`. The general 15 to 20 target does not apply.
- `--voice none` turns the profile off. `--voice PATH` uses another profile.

## Privacy

A profile can contain short fragments of real writing. Keep it out of shared repositories, and do not put names, customers or numbers from the source texts into it.
