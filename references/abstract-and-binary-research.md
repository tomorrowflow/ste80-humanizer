# Research: abstract reference nouns, spelled-out alternatives and personified documents

Research notes for three patterns in Claude's German and English business mail that the skill does not catch yet. Researched in November 2026. The format follows `german-research.md`: every claim has a link, and "unverified" marks a point that no primary source confirmed.

Each claim carries one of three labels:

- **Sourced:** a primary or high-trust source says it. The link follows.
- **Sourced (general style):** a style guide or standard supports the fix, but it does not call the pattern an AI tell.
- **Observation:** our own reading of real output. No source documents it as an AI tell.

The three patterns:

- **A. Abstract reference nouns.** The text points at the structure of a table, list or document that the reader never saw ("je Zeile", "dieser Punkt", "ein Viertel der Liste", "each row").
- **B. Spelled-out alternatives and negations.** The text names both branches of a decision, or adds the opposite of a statement ("ob es die Antwort hält und belegt oder korrigiert", "ob X oder nicht", "kein X, sondern Y").
- **C. Personified documents.** A document acts like a person ("Die Service Description schweigt zu diesen Punkten"), often with a vague link between two claims.

## 1. Summary

1. **No source documents pattern A as an AI tell.** No corpus study, no Wikipedia page and no Anthropic document names structure nouns ("row", "Zeile", "Eintrag") as an LLM sign. The closest sourced finding is general: instruction-tuned models write in an "informationally dense, noun-heavy style" and use nominalizations at 1.5 to 2 times the human rate (Reinhart et al., PNAS 2025, English, GPT-4o and Llama 3). Kobak et al. found the opposite for vocabulary: 2024 excess words were mostly verbs (66%) and adjectives (14%), not nouns. So A rests on our observation plus general style advice (Wolf Schneider on Oberbegriffe, tekom and DIN 8581-1 on references). [Reinhart et al.](https://arxiv.org/html/2410.16107v2), [Kobak et al.](https://arxiv.org/html/2406.07016)
2. **Part of pattern B is sourced.** English Wikipedia lists "Y rather than X" as a negative parallelism and says it is "particularly common in recent LLM output". A 2026 preprint finds "rather than" in ACL-style papers at seven times the 2019 rate, and higher in GPT-written papers. German Wikipedia names parallel constructions with "nicht", "aber", "jedoch" and "sondern". So "X statt Y", "kein X, sondern Y" and "Das heißt nicht, dass …" belong to §1. [en.WP](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [Zamaraeva et al. 2026](https://arxiv.org/abs/2610.10092), [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte)
3. **The other part of pattern B is observation.** No source names "both branches of a binary decision", "ob X oder nicht", "mit oder ohne" or "in beiden Fällen" as an AI tell. Grice's maxim of quantity ("no more informative than is required") explains why the extra branch reads as noise. Usage guides call "or not" after "whether" redundant when no alternative needs stating. [SEP: Grice](https://plato.stanford.edu/entries/grice/), [Curzan, Michigan Public](https://www.michiganpublic.org/podcast/thats-what-they-say/2024-04-14/twts-whether-or-not-belongs-in-whether-or-not-or-not)
4. **Pattern C as an AI tell is observation.** No source names personified documents ("das Dokument schweigt") as an LLM sign. The anthropomorphism studies found cover how LLMs describe AI systems, not how they describe documents. But the legal and lexical facts are sourced:
   - Duden gives "schweigen" for texts only in a figurative sense ("darüber schweigt die Geschichtsschreibung"). No Duden or Wiktionary example has a document, contract or law as the subject.
   - In German law, "Schweigen" is a term for a party that does not react (§ 455 BGB: "gilt sein Schweigen als Billigung"). In legal method, "beredtes Schweigen" belongs to the Gesetzgeber, a body that acts, not to the text (BAG 10 AZR 674/05).
   - German statutes do use documents as subjects with plain verbs: "wenn der Gesellschaftsvertrag nichts anderes bestimmt" (§ 29 GmbHG), "Sofern die Satzung dies vorsieht" (§ 58 AktG). So "sieht vor", "bestimmt", "regelt" and "enthält" are standard. "schweigt" is not.
   - In Linguee's EU parallel texts, 1 of 10 German renderings of "is silent on" uses "schweigt". The others say "enthält keine Bestimmungen hierzu", "keine Regelung enthält", "keine Angaben … enthält" and similar.
5. **Claude-specific evidence is thin.** Sun et al. (ICML 2025) found that Claude refers to "the text" ("according to the text", "based on the text") more than other chatbots, and that its answers are more concise. This is adjacent to pattern A (pointing at the source instead of the subject). It is not evidence for "je Zeile". en.WP notes that "broader context" framing is more typical of ChatGPT and Grok than of Claude. No Anthropic document lists these patterns. [Sun et al.](https://arxiv.org/html/2502.12150v2)
6. **Regexes work for the fixed phrases, not for the logic.** On 803 sentences of human German Wikipedia text (contracts, AGB, SLA, Lastenheft, spreadsheets, databases), the proposed A and C regexes had 0 hits. "ob … oder nicht" and the decision-plus-alternatives regex each had 1 hit. "nicht X, sondern Y" (5 hits) and scope words like "bzw.", "in jedem Fall" (12 hits) are too common for a regex. Report those by density or not at all. Whether a branch is redundant needs a reader. A regex cannot decide it.
7. **Recommended changes:**
   - Extend §25 with "structure the reader never saw" (A).
   - Extend §4 and §19 with meta-labels (A).
   - Extend §1 with "X statt Y", "kein X, sondern Y" and "Das heißt nicht, dass" (B, sourced).
   - Extend §6 with "both branches of a decision", weak alone (B, observation).
   - Extend §18 with personified documents and "X bleibt ohne Y" (C).
   - Extend §14 for "und" where the source has a cause (C).
   - Add the fixed-phrase regexes to `TELLS_DE` and `TELLS`.

   Section 6 has the details.

## 2. Sources checked

| Source | What it says about A, B or C | Label |
|---|---|---|
| en.WP "Signs of AI writing", raw wikitext read 24 Nov 2026 | Negative parallelisms in three forms: "Not just X, but also Y", "Not X, but Y", "Y rather than X". "Y rather than X" is "particularly common in recent LLM output". Inline-header lists with labels such as "Key Takeaways" and "Key Figures" (Style subpage). "landscape" and "tapestry" flagged "as an abstract noun". Humans use simple is/has phrases more than LLMs. Nothing on rows, columns, entries, "whether or not" or personified documents. | Sourced for B (contrast part) and the meta-labels in A |
| de.WP "Anzeichen für KI-generierte Inhalte", raw wikitext read 24 Nov 2026 | "Negative Parallelismen": "nicht nur … sondern auch", "es geht nicht nur um … sondern", and parallel constructions with "nicht", "aber", "jedoch", "sondern" are more frequent in LLM articles. Nothing on structure nouns, binary alternatives or personification. | Sourced for "kein X, sondern Y" |
| Reinhart et al., "Do LLMs write like humans?", PNAS 122(8), 2025 | Instruction-tuned models use present participial clauses at 2 to 5 times the human rate and nominalizations at 1.5 to 2 times. GPT-4o: nominalizations 2.1×, phrasal coordination 1.9×. They call it an "informationally dense, noun-heavy style". English only. GPT-4o and Llama 3, not Claude. | Sourced (general) for A |
| Kobak et al., "Delving into LLM-assisted writing…", Science Advances 2025 | In 2024, 66% of the 379 excess style words were verbs and 14% adjectives. Before 2024, excess words were mostly content nouns. No category of abstract or structure nouns. | Counter-evidence: A is not a vocabulary effect |
| Juzek and Ward, COLING 2025 and arXiv 2508.01930 | Lexical overrepresentation ("delve", "intricate"), linked to learning from human feedback. Nothing on A, B or C. | Not relevant beyond context |
| Sun et al., "Idiosyncrasies in LLMs", ICML 2025 | A classifier tells five chatbots apart with 97.1% accuracy. Claude "usually references the original prompt using the phrases like 'according to the text' and 'based on the text'". Claude answers are "more concise and direct". | Sourced, Claude-specific, adjacent to A |
| Zamaraeva et al., "I would rather quit NLP…", arXiv 2610.10092, Oct 2026 | "rather than" in 2026 ACL-style papers is seven times the 2019 rate, and higher in GPT-written papers. Preprint, not peer reviewed. | Sourced (preprint) for "X statt Y" / "Y rather than X" |
| Lubrano, "Emphatic Epanorthosis on LLMs", Zenodo 2025 | States that "not X, but Y" appears in LLM output "at rates far exceeding those in baseline human corpora". No numbers in the abstract. Data paper, not peer reviewed. | Weak support for §1 |
| Grice, maxim of quantity (SEP entry "Paul Grice", § 3) | "make your contribution as informative as is required" and "make it no more informative than is required". | Theory behind B |
| Usage guides on "whether or not" | Curzan: mostly a style choice. A search snippet attributes to Grammarist that "or not" is redundant unless it is a needed alternative. Grammar Girl, via a LitReactor column, calls "or not" fluff. | Sourced (general style) for B, English only |
| Wolf Schneider, *Deutsch für Profis*, p. 57, quoted in Becker 2024 | Avoid abstract Oberbegriffe. Write the concrete word you know: "Wenn ich lauter Birken sehe, werde ich nicht ‚Bäume' sagen". Becker adds that nouns ending in -ung, -heit, -keit and similar are often pale Oberbegriffe. | Sourced (general style, secondary quote) for A |
| tekom "Regelbasiertes Schreiben" 2013, public TOC | S 101/S 102 pronoun references, S 314 no double negation, S 505 avoid nominalizations, L 101 vague verbs, L 108 superfluous words, L 112 stock phrases. Rule bodies are paywalled. | Sourced (general style) for A, B, C |
| DIN 8581-1:2024-05, public TOC | 5.2.4 Nominalstil, 6.3 references, 6.8 negation, 7.3 nominalizations. Content is paywalled. | Sourced (general style) |
| ISO 24495-1:2023 | First principle: readers get what they need ("relevant"). | Sourced (general style) for B |
| Duden "schweigen" | Sense 1 "nicht reden", with "über, von etwas schweigen" and, marked "in übertragener Bedeutung", "darüber schweigt die Geschichtsschreibung". No example with a document or law. | Sourced for C |
| Duden "sprechen" | "für sich selbst sprechen (keiner weiteren Erläuterung bedürfen)". "für, gegen etwas sprechen" is standard ("das spricht dafür, dass …"). Sense 7, marked gehoben: "Zahlen [für sich] sprechen lassen". | Sourced for C |
| Wiktionary "schweigen" | Two senses, both for people: be quiet, keep a secret. No example with a document. | Sourced for C |
| BGB § 455, GmbHG § 29 Abs. 2, AktG § 58 Abs. 5 (gesetze-im-internet.de) | "Schweigen" is a party's non-reaction with legal effect. Contracts and statutes "bestimmen" and "sehen vor". No statute text found in which a contract "schweigt". | Sourced for C |
| BAG, 13.12.2006, 10 AZR 674/05 | "jedes Schweigen des Gesetzgebers", "ein ‚beredtes' Schweigen des Gesetzgebers". The silent party is the legislator. | Sourced for C |
| Linguee, "the contract is silent on" (EU parallel texts) | 10 German renderings. 1 uses "schweigt … dazu". 3 use "enthält keine Bestimmungen / Regelung / Angaben". The rest use "erwähnt mit keinem Wort", "keine Aussage darüber macht" and others. Small, unreviewed sample. | Sourced (weak) for C |
| "is silent on" in English legal drafting | Justia's legal dictionary example (via search snippet): "The contract was silent on the details of overtime payment." Ken Adams (Adams on Contract Drafting) argues against "is silent on" in contracts (via search snippet). Both pages returned 403, so this is not verified at the source. | Unverified at source |
| Anthropomorphism studies (HumT DumT, arXiv 2502.13259; Dehumanizing Machines, arXiv 2502.14019; and others) | They measure human-like language about AI systems ("The system decides…") and in LLM self-description. None counts personified documents or "the data shows" in LLM output. | Not evidence for C. Do not cite as such |
| Anthropic prompting docs | Newer models write more directly. Prose over bullets for reports. No list of style tics. | Not evidence for A, B or C |

## 3. Pattern A: abstract reference nouns

### A1. Structure the reader never saw

**Watch for:** je Zeile, pro Zeile, pro Spalte, für jeden Eintrag, je Position, dieser Punkt, diese Punkte, der Eintrag, das Feld, die Ebene, die Dimension, die Zahl (for a number the reader never saw), die Liste (for a list the reader never got). English: each row, per row, this column, the line item, the entry, the field, the figure, the list.
**Problem:** The writer worked from a table, a spreadsheet or a list of questions. The reader gets only the mail. "Je Zeile" makes the reader rebuild a table that is not there. Name the thing the row stands for: the answer, the product, the invoice, the risk. If the reader has the table (it is attached or in the mail), "je Zeile" is fine.
**Before:**
> Je Zeile entscheidet das Produktteam, ob es die Antwort hält und belegt oder korrigiert.
**After:**
> Das Produktteam prüft jede Antwort.

(Then add "und belegt sie" only if the source needs the proof step. See B1.)

**Before:**
> Für jede Zeile mit Status „offen“ fehlt die Preisgrundlage.
**After:**
> Für die fünf offenen Leistungen fehlt die Preisgrundlage.
**Before (English):**
> For each row, the product team decides whether to keep and support the answer or correct it.
**After:**
> The product team checks each answer.

**Evidence:** Observation. No source names this as an AI tell. Supporting sources (general style):

- Schneider's advice to write the concrete word instead of the Oberbegriff (Becker 2024, quoting *Deutsch für Profis*, p. 57).
- tekom S 101/S 102 (unclear references).
- DIN 8581-1 6.3 (references).
- en.WP "Text about the document" is not a match. That point is about a layout the reader *can* see. A1 is the reverse case.

Our explanation (observation): the model reasons over a table in its context and leaks the table's vocabulary into the text for the reader. That makes it a "wrong reader" problem (group F), close to §25.

### A2. Abstract quantities

**Watch for:** ein Viertel der Liste, die Hälfte der Punkte, der Großteil der Positionen, ein Teil der Fälle. English: a quarter of the list, half of the items, most of the entries.
**Problem:** The share replaces the count and the things. The reader does not know the size of the list, so "ein Viertel" carries no number. Give the count and name the things.
**Before:**
> Ohne Auskunft des Produktteams bleibt ein Viertel der Liste ohne Preisgrundlage.
**After:**
> Für 12 der 48 Leistungen fehlt die Preisgrundlage, bis das Produktteam sie klärt.
**Before (English):**
> Without input from the product team, a quarter of the list has no pricing basis.
**After:**
> 12 of the 48 services have no pricing basis until the product team answers.

**Evidence:** Observation. No source. Use only numbers from the source. If the source has only "ein Viertel", keep the share and name the things ("ein Viertel der Leistungen").

### A3. Meta-labels

**Watch for:** "Kernpunkt:", "Kernaussage:", "Kurz gesagt:", "Unterm Strich:", "Der springende Punkt ist", "Der entscheidende Punkt ist", "Hier geht es um", "Dabei geht es darum". English: "Key point:", "Key takeaway:", "Bottom line:", "The real point is", "Here's the thing".
**Problem:** The label announces a point instead of making it. Delete the label and keep the sentence. Keep a label only where the reader scans for it, for example "Frist:" or "Entscheidung:" at the top of a mail with a real date or decision after it.
**Before:**
> Kernpunkt: Die Lizenz läuft im März aus, und ohne Verlängerung steht das Tool still.
**After:**
> Die Lizenz läuft im März aus. Ohne Verlängerung steht das Tool still.
**Before (English):**
> The real point here is that the licence expires in March.
**After:**
> The licence expires in March.

**Evidence:** Partly sourced. en.WP (Style subpage) lists inline-header lists with labels such as "Key Takeaways", "Key Figures" and "Key highlights". The skill already has "here's the thing" (§4) and bold labels (§19). The German phrases are observation.

## 4. Pattern B: spelled-out alternatives and negations

### B1. Both branches of a decision

**Watch for:** a check or decision verb followed by both outcomes: "entscheidet, ob es X oder Y", "prüft, ob X stimmt oder korrigiert werden muss", "klärt, ob wir verlängern oder kündigen". English: "decides whether to keep or correct", "checks whether it is right or needs fixing".
**Problem:** "prüfen" already means that the result can go either way. Naming both branches tells the reader nothing new (Grice: "no more informative than is required"). It also makes a simple task sound like a procedure. Name the action. Keep the branches only when the next step differs per branch and the reader must act on it.
**Before:**
> Je Zeile entscheidet das Produktteam, ob es die Antwort hält und belegt oder korrigiert.
**After:**
> Das Produktteam prüft jede Antwort und belegt sie.

(Keep "und belegt sie" only if the source asks for proof.)

**Keep:**
> Wenn die Antwort stimmt, legt das Produktteam den Beleg bei. Wenn nicht, schickt es die Korrektur bis Freitag.

(Each branch has its own action, so both stay.)

**Before (English):**
> The legal team decides whether to accept the clause or push back on it.
**After:**
> The legal team reviews the clause.

**Evidence:** Observation for the AI-tell claim. The theory is sourced: Grice's maxim of quantity (SEP, § 3), ISO 24495-1 "relevant", tekom L 108 (superfluous words).

### B2. Fixed exhaustive forms

**Watch for:** ob X oder nicht, mit oder ohne, unabhängig davon, ob, entweder … oder (when one option is obvious), so oder so, in jedem Fall, in beiden Fällen, jeweils, beziehungsweise / bzw. English: whether or not, whether X or not, with or without, regardless of whether, either way, in both cases, in either case, respectively, and/or.
**Problem:** Each form makes the reader check that the text covers all cases. That makes sense in a contract clause. In a mail, the reader assumes full coverage anyway. Delete the second branch, or use "jeweils" and "bzw." only when the pairing is not clear without them.
**Before:**
> Bitte prüf, ob die Rechnung stimmt oder nicht.
**After:**
> Bitte prüf die Rechnung.
**Before:**
> Mit oder ohne Wartungsvertrag liefern wir bis Ende Mai.
**After:**
> Wir liefern bis Ende Mai.

(Keep "mit oder ohne Wartungsvertrag" if the reader asked about it.)

**Before (English):**
> Please let me know whether or not you can join.
**After:**
> Please let me know if you can join.

**Evidence:** Observation for the AI-tell claim. For "whether or not": usage guides (Curzan; Grammarist and Grammar Girl via secondary sources) call "or not" optional or redundant when no alternative needs stating. No German source checked. A false-positive test (section 5) shows that "bzw." and "in jedem Fall" are normal in human German reference text, so treat B2 as weak alone.

### B3. Contrast and inversion (extends §1)

**Watch for:** X statt Y, anstatt, anstelle von (when nobody proposed Y), kein X, sondern Y, nicht X, sondern Y, "Das heißt nicht, dass …", "Das bedeutet nicht, dass …", a sentence that states the opposite of the one before ("Das ist kein Rückschritt. Es ist eine Klärung."). English: Y rather than X, instead of X, not X but Y, "This doesn't mean X."
**Problem:** Same as §1. The negative half names something nobody claimed, so the positive half sounds bigger. Keep a contrast when the reader or the thread really holds X.
**Before:**
> Das ist kein Preisproblem, sondern ein Mengenproblem.
**After:**
> Wir bestellen 40 Lizenzen zu viel.
**Before:**
> Wir verlängern den Vertrag um ein Jahr, statt ihn jetzt neu auszuschreiben.
**After:**
> Wir verlängern den Vertrag um ein Jahr.

(Keep "statt …" if someone in the thread proposed a new tender.)

**Before (English):**
> The tool acts as an interface between the agents and the existing tools rather than replacing them.
**After:**
> The tool connects the agents to the existing tools.

**Evidence:** Sourced:

- en.WP "Y rather than X" ("particularly common in recent LLM output") and "Not X, but Y".
- de.WP: parallel constructions with "nicht", "aber", "jedoch", "sondern" are more frequent in LLM articles.
- Zamaraeva et al. 2026: "rather than" rose sevenfold, and is higher in GPT papers.
- The German forms "X statt Y" and "Das heißt nicht, dass" are the obvious German equivalents. No German study counts them, so that part is unverified.

## 5. Pattern C: personified documents and abstract subjects

### C1. A document that acts like a person

**Watch for:** das Dokument / die Beschreibung / die Service Description / der Vertrag / das Angebot / die Richtlinie / die Tabelle **schweigt**, verschweigt, verrät, erzählt, bleibt vage, bleibt stumm, lässt offen (weak). English: the document is silent on, the contract is silent on (legal idiom, see below), the data tells us, the numbers speak.
**Problem:** In German business and contract mail, documents "regeln", "enthalten", "sehen vor" and "bestimmen". They do not "schweigen". "Schweigen" for a text is a figurative, literary use (Duden's only example: "darüber schweigt die Geschichtsschreibung"). In law, "Schweigen" is what a party does, and it can have legal effect (§ 455 BGB). So the metaphor can also confuse a legal reader. Use the plain verb, or say who has not answered.
**Before:**
> Die Service Description schweigt zu diesen Punkten.
**After:**
> Die Service Description regelt diese Leistungen nicht.

or:

> Die Service Description enthält zu diesen fünf Leistungen keine Angaben.

**Before (English):**
> The service description is silent on these items.
**After:**
> The service description does not cover these five services.

(In an English contract or legal memo, "the contract is silent on X" is an established idiom. Keep it there. In a business mail, "does not cover" or "says nothing about" is plainer.)

**Keep (standard German):**

| Phrase | Why it stays | Source |
|---|---|---|
| der Vertrag sieht vor, die Satzung sieht vor | statutory wording | AktG § 58 Abs. 5 "Sofern die Satzung dies vorsieht" |
| der Vertrag bestimmt, soweit nichts anderes bestimmt ist | statutory wording | GmbHG § 29 Abs. 2 "wenn der Gesellschaftsvertrag nichts anderes bestimmt" |
| der Vertrag regelt, enthält keine Regelung zu | standard; the most frequent rendering of "is silent on" in EU texts | Linguee EU parallel texts |
| das spricht für / gegen | standard Duden sense | Duden "sprechen" |
| die Daten zeigen, die Tabelle zeigt (when the reader has the data) | standard; a §17 problem only when no source is named | de.WP §17 list |
| beredtes Schweigen des Gesetzgebers | legal-method term; the subject is the legislator | BAG 10 AZR 674/05 |

**Evidence:** The lexical and legal facts are sourced (Duden, Wiktionary, BGB, GmbHG, AktG, BAG, Linguee). The claim that LLMs personify documents more than people do is observation. No study found. Whether "schweigt zu" is a calque of "is silent on" is unverified. German historiography has its own "die Quellen schweigen" (Duden's figurative example points that way), so the use may be native and literary rather than borrowed. In the Linguee sample, translators avoided "schweigt" in 9 of 10 cases. That supports "not the business register", not "calque".

### C2. "X bleibt ohne Y" and other abstract subjects

**Watch for:** bleibt ohne Grundlage, bleibt ohne Antwort, bleibt unklar, bleibt offen, steht im Raum. A share or a list as the subject ("ein Viertel der Liste bleibt …"). English: remains without, remains unclear, stays open.
**Problem:** The sentence makes a list or a share the subject and hides the actor and the thing. "X bleibt ohne Y" is a negated "hat" (§18). Make the thing the subject and use "hat", "fehlt" or the actor.
**Before:**
> Ohne Auskunft des Produktteams bleibt ein Viertel der Liste ohne Preisgrundlage.
**After:**
> Für 12 Leistungen fehlt die Preisgrundlage, bis das Produktteam antwortet.

**Evidence:** Observation. Supported in general by tekom S 505 and DIN 8581-1 5.2.4 and 7.3 (Nominalstil, nominalizations). "bleibt ohne Folgen" and "bleibt offen" are normal idioms. Act only when the subject is a list, a share or a document.

### C3. "und" where the source has a cause

**Watch for:** two claims joined by "und" (or a comma) where the second follows from the first. In the real example: "schweigt zu diesen Punkten **und** … bleibt … ohne Preisgrundlage". The user's own version: "Es gibt keine Klärung … **Daher** besteht keine Preisgrundlage."
**Problem:** "und" hides the relation. The reader has to infer that the missing rule causes the missing price. Name the relation the source gives: daher, deshalb, weil, sodass. This is §14 (vague connection) at sentence level, and S1 ("keep the clause that carries the reason").
**Before:**
> Die Service Description schweigt zu diesen Punkten und ohne Auskunft des Produktteams bleibt ein Viertel der Liste ohne Preisgrundlage.
**After:**
> Die Service Description regelt 12 der 48 Leistungen nicht. Deshalb fehlt dafür die Preisgrundlage, bis das Produktteam sie klärt.
**Before (English):**
> The service description is silent on these items and a quarter of the list has no pricing basis.
**After:**
> The service description does not cover 12 of the 48 services, so they have no pricing basis until the product team answers.

**Evidence:** Observation. Theory: Grice's maxim of manner (be perspicuous; SEP names it, but the submaxims are not quoted there). No study counts "und" for a causal link in LLM output.

### C4. Literary closers on data

**Watch for:** Die Zahlen sprechen für sich. Die Daten sprechen eine klare Sprache. English: The numbers speak for themselves. The data tells a clear story.
**Problem:** This is §2 (one-line closer). Duden lists "Zahlen [für sich] sprechen lassen" as gehoben. Give the number.
**Before:**
> Die Zahlen sprechen für sich.
**After:**
> Die Kosten sind um 18 % gestiegen.

**Evidence:** Register sourced (Duden "sprechen", sense 7, gehoben). As an AI tell: observation.

## 6. Mapping to §1 to §26 and recommended skill changes

| Pattern | Closest tell | Recommendation | Basis |
|---|---|---|---|
| A1 structure the reader never saw | §25 Text about the document (and group F, wrong reader) | **Extend §25.** Add to Watch for: "structure the reader never saw: je Zeile, pro Spalte, der Eintrag, dieser Punkt; each row, the line item". Fix: name the thing. Add a German row in `german.md`. | Observation + general style |
| A2 abstract quantities | §25, S11 | **Fold into A1** (same fix: count and name the things). | Observation |
| A3 meta-labels | §4 Staged run-up, §19 Bold labels | **Extend §4** with "Der springende Punkt ist", "Hier geht es um", "The real point is". **Extend §19** with "Kernpunkt:", "Key takeaway:", "Bottom line:" as line starts, with or without bold. | en.WP (labels) + observation |
| B1 both branches of a decision | §6 Forced triads | **Extend §6** to "Forced triads and pairs", *weak alone*: keep both branches only if each needs its own action. A new tell would break the 1:1 match with the blader/humanizer catalog that AGENTS.md asks for. | Observation + Grice |
| B2 fixed exhaustive forms | §6, §9 Stacked qualifiers | **Extend §6** (same entry as B1) for "ob … oder nicht", "mit oder ohne", "whether or not", "with or without". Do not flag "jeweils", "bzw.", "in jedem Fall" by regex. | Observation + usage guides |
| B3 contrast and inversion | §1 Not X but Y | **Extend §1** in `german.md`: "X statt Y", "kein X, sondern Y", "nicht X, sondern Y", "Das heißt nicht, dass …". SKILL.md §1 already lists "X rather than Y" in `ai-tells.md`. Add "instead of" there. | Sourced (en.WP, de.WP, Zamaraeva) |
| C1 personified documents | §18 Avoiding is, are, has | **Extend §18** (German row): "die Beschreibung schweigt zu", "verrät", "bleibt vage" → "regelt nicht", "enthält keine Angaben zu". Add a keep list: "sieht vor", "bestimmt", "regelt", "spricht für". | Sourced facts (Duden, BGB, Linguee) + observation |
| C2 X bleibt ohne Y | §18, S8 | **Extend §18** (same row). | Observation |
| C3 "und" for a cause | §14 Vague connection, S1 | **Extend §14**: "two claims joined by 'und' / 'and' where the source gives a cause: use daher, weil, so". | Observation |
| C4 literary data closers | §2 One-line closers | **Extend §2** German list: "Die Zahlen sprechen für sich". | Duden register + observation |

If the skill gets a German "new" tell row like the existing calques and false ranges, A1 is the best candidate: it is frequent in Claude's German mail and the fix is clear. Keep it marked "observation" in `german.md`, like the "Uniform text" row.

Keep in sync (per AGENTS.md): SKILL.md tables, README tell list, `references/ai-tells.md` entries (Watch for, Problem, Before, After), `references/german.md`, `scripts/ste_check.py`.

## 7. Regex proposals for `scripts/ste_check.py`

All patterns use the `(pattern, rule, message)` format of `TELLS_DE` and `TELLS`, and run with `re.I`. Patterns that start with `^` also need `re.M` or a per-line run, as the script does now.

### Test

A scratch test ran each pattern on 13 positive sentences (the real examples above plus constructed ones) and 11 negative sentences (standard phrases such as "Der Vertrag sieht … vor", "Er schweigt zu den Vorwürfen", "Der Fehler bleibt ohne Folgen", "pro Zeile einen Datensatz"). It also ran on 803 sentences of human German Wikipedia text: the articles Allgemeine Geschäftsbedingungen, Tabellenkalkulation, Rechnung (Dokument), Vertrag, Service-Level-Agreement, Lastenheft, Kaufvertrag (Deutschland) and Datenbank. Not tested on a German AI corpus (none available), so recall is unknown.

| Proposed rule | Hits in 803 human sentences | Verdict |
|---|---|---|
| A structure nouns (de) | 0 (one constructed negative "pro Zeile einen Datensatz" hit) | Add, weak. Skip when the file has a Markdown table |
| A "diese Punkte" etc. (de) | 0 | Add, weak |
| A abstract share (de) | 0 | Add |
| A meta-labels (de) | 0 | Add |
| B decision + "ob … oder" (de) | 1 | Add, weak |
| B "ob … oder nicht" (de) | 1 | Add, weak |
| B "mit oder ohne", "unabhängig davon, ob", "entweder … oder" (de) | 1 | Add, weak |
| B3 "kein X, sondern Y" (de) | 2 | Add under §1, weak |
| B3 "nicht X, sondern Y" (de) | 5 | Do not add. Too common in legal and reference text |
| B3 "Das heißt nicht, dass" (de) | 0 | Add under §1 |
| B scope words "in beiden Fällen", "in jedem Fall", "bzw." (de) | 12 | Do not add. At most a density note |
| C personified document (de) | 0 (constructed negatives "Er schweigt", "Der Vertrag sieht vor" did not hit) | Add |
| C "bleibt … ohne" with 1 to 4 words between (de) | 0 ("bleibt ohne Folgen" did not hit) | Add, weak |
| C "Zahlen sprechen für sich" (de) | 0 | Add |

The English patterns were tested only on the constructed sentences, not on an English corpus.

### Proposed `TELLS_DE` entries

```python
# A: structure the reader never saw (§25). Weak: real tables use "pro Zeile".
(r"\b(?:je|pro|für\s+jede[nrs]?|in\s+jede[rm])\s+(?:Zeile|Spalte|Zelle|Position|Eintrag|Feld|Ebene|Dimension|Punkt|Posten|Element)\b",
 "structure-noun", "'je Zeile', 'pro Eintrag': name the thing, unless the reader has the table (§25)"),
(r"\b(?:diese[nrms]?|die\s+genannten|die\s+offenen|die\s+übrigen|die\s+restlichen)\s+(?:Punkte?n?|Einträgen?|Positionen|Aspekten?|Ebenen?|Dimensionen?)\b",
 "structure-noun", "'diese Punkte': name the things (weak alone, §25)"),
(r"\b(?:ein(?:e[mnr]?)?\s+(?:Viertel|Drittel|Fünftel|Zehntel|Teil|Großteil|Grossteil)|die\s+Hälfte|der\s+(?:Groß|Gross)teil|die\s+Mehrheit)\s+(?:der|des)\s+(?:Liste|Tabelle|Punkte|Positionen|Einträge|Zeilen|Fälle|Antworten)\b",
 "structure-noun", "share of a list: give the count and name the things (§25)"),
# A: meta-labels (§4, §19)
(r"^(?:Kernpunkt|Kernaussage|Kernfrage|Kurz\s+gesagt|Kurzum|Der\s+Punkt|Das\s+Entscheidende|Die\s+Pointe|Unterm\s+Strich|Kurzfassung)\s*:|\bder\s+(?:springende|entscheidende|eigentliche|wichtigste)\s+Punkt\s+(?:ist|hier)\b|\b(?:hier|dabei)\s+geht\s+es\s+(?:darum|um)\b",
 "meta-label", "label instead of the point: delete the label, keep the sentence (§4)"),
# B: spelled-out alternatives (§6, weak alone)
(r"\b(?:entscheid\w*|prüf\w*|klär\w*|bewert\w*|festleg\w*|beurteil\w*)\b[^.!?]{0,40}\bob\b[^.!?]{3,80}\boder\b",
 "both-branches", "both outcomes of a check spelled out: name the action ('prüft jede Antwort') unless each branch needs its own step (§6)"),
(r"\bob\b[^.!?]{1,80}\boder\s+nicht\b|\bmit\s+oder\s+ohne\b|\bunabhängig\s+davon,?\s+ob\b",
 "both-branches", "'ob … oder nicht', 'mit oder ohne': the reader assumes both cases, delete the second (weak alone, §6)"),
# B3: contrast family (§1)
(r"\bkein(?:e[mnrs]?)?\s+[^,.!?]{1,40},\s*sondern\b",
 "not-x-but-y", "'kein X, sondern Y': keep only a real contrast (§1)"),
(r"\b(?:das|dies)\s+(?:heißt|heisst|bedeutet)\s+(?:aber\s+)?nicht,?\s+dass\b",
 "not-x-but-y", "'Das heißt nicht, dass …': state the point (§1)"),
# C: personified documents (§18) and data closers (§2)
(r"\b(?:Dokument|Vertrag|Angebot|Beschreibung|Description|Spezifikation|Richtlinie|Policy|Tabelle|Liste|Bericht|Studie|Analyse|Daten|Zahlen|Quelle|Unterlage|Text|SLA|AGB|Mail)\w*\s+(?:schweig\w*|verrät|verraten|verschweig\w*|erzählt|erzählen|flüster\w*|bleib\w*\s+(?:vage|stumm|still))\b",
 "personified-doc", "document as a person: use 'regelt nicht', 'enthält keine Angaben zu' (§18)"),
(r"\bbleib\w*\s+(?:[\wäöüß]+\s+){1,4}ohne\s+\w+",
 "personified-doc", "'X bleibt ohne Y': use 'fehlt' or 'hat kein' and name the thing (weak alone, §18)"),
(r"\b(?:Zahlen|Fakten|Daten|Ergebnisse)\s+sprechen\s+(?:eine\s+\w+\s+Sprache|für\s+sich)\b",
 "closer", "'Die Zahlen sprechen für sich': give the number (§2)"),
```

### Proposed `TELLS` entries (English)

```python
(r"\b(?:each|per|every|this|that)\s+(?:row|column|line\s+item|cell|field|entry)\b",
 "structure-noun", "'each row', 'this column': name the thing, unless the reader has the table (§25)"),
(r"^(?:key\s+(?:point|takeaway)s?|bottom\s+line|tl;dr|the\s+short\s+(?:version|answer)|short\s+version)\s*:|\bthe\s+(?:key|real|main)\s+point\s+(?:is|here)\b",
 "meta-label", "label instead of the point: delete the label (§4)"),
(r"\b(?:decide\w*|check\w*|review\w*|assess\w*|determin\w*)\b[^.!?]{0,40}\bwhether\b[^.!?]{3,80}\bor\b",
 "both-branches", "both outcomes of a check spelled out: name the action (weak alone, §6)"),
(r"\bwhether\b[^.!?]{0,80}\bor\s+not\b|\bwith\s+or\s+without\b|\bregardless\s+of\s+whether\b",
 "both-branches", "'whether or not', 'with or without': delete the second branch (weak alone, §6)"),
(r"\b(?:document|contract|spec|policy|description|report)s?\s+(?:is|are|remains?)\s+silent\b|\b(?:data|numbers|figures)\s+(?:tell|speak)\b",
 "personified-doc", "document or data as a speaker: 'does not cover', give the number (keep 'is silent on' in legal text, §18)"),
```

### Script behaviour to add

- **Table guard for "structure-noun".** Skip the A1 rules when the file holds a Markdown table (`re.search(r"^\s*\|.*\|", text, re.M)`) or mentions an attachment ("Anhang", "anbei", "attached"). This keeps the rule for prose mail and drops it for spreadsheet docs. Proposed, untested.
- **Density instead of single hits** for "statt", "anstatt", "rather than", "instead of", "jeweils", "bzw.", "respectively": flag a paragraph with two or more. The threshold is unverified, like the other thresholds in `german-research.md` section 6.
- **No regex** for C3 ("und" for a cause), for "nicht X, sondern Y" in general, or for judging whether a branch is redundant. These need a reader. Leave them to Pass 1.

## 8. Open questions and unverified points

- **No corpus count exists** for structure nouns, both-branch decisions, "ob … oder nicht" or personified documents in LLM output, in English or German. A small study would settle it: count these regexes in Claude German mail drafts against human business mail of the same type.
- **Reinhart et al. and Kobak et al. disagree in direction for nouns.** Reinhart finds more nominalizations (grammar). Kobak finds that excess *words* are verbs and adjectives. Both are English and neither tests Claude. Do not cite either as proof of A.
- **The Claude-specific evidence** (Sun et al.) covers early-2025 models and English prompts. Its "according to the text" finding is adjacent to A, not the same pattern.
- **"schweigt zu" as a calque** of "is silent on": unverified. The figurative "die Quellen schweigen" may be native German. The Linguee sample (10 sentences) is too small to measure frequency.
- **"is silent on" in English contracts:** the Justia example and the Adams critique were seen only as search snippets (403 on fetch). Verify before citing in the skill.
- **Usage-guide claims on "whether or not"** (Grammarist, Grammar Girl) come from secondary snippets. Only the Curzan page is a direct source.
- **Schneider's quote** comes from a secondary source (Becker 2024, spielbox) that cites *Deutsch für Profis*, p. 57. Not checked in the book.
- **Thresholds and the table guard** are proposals. The 803-sentence test covers human reference text, not business mail. Business mail may use "in beiden Fällen" and "bzw." even more.
- **Zamaraeva et al. 2026** is a preprint. The abstract does not give the GPT rate as a number.

## 9. Sources

### Wikipedia project pages

- Wikipedia:Signs of AI writing (raw wikitext, read 24 Nov 2026). https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Wikipedia:Signs of AI writing/Style. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style
- Wikipedia:Anzeichen für KI-generierte Inhalte (raw wikitext, read 24 Nov 2026). https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte

### Studies

- Reinhart, Markey, Laudenbach, Pantusen, Yurko, Weinberg, Brown: Do LLMs write like humans? Variation in grammatical and rhetorical styles. PNAS 122(8), 2025. https://pnas.org/doi/10.1073/pnas.2422455122 (full text read at https://arxiv.org/html/2410.16107v2)
- Kobak, González-Márquez, Horvát, Lause: Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Science Advances 11(27), 2025. https://www.science.org/doi/10.1126/sciadv.adt3813 (full text read at https://arxiv.org/html/2406.07016)
- Juzek, Ward: Why Does ChatGPT "Delve" So Much? COLING 2025. https://aclanthology.org/2025.coling-main.426.pdf
- Juzek, Ward: Word Overuse and Alignment in Large Language Models. https://arxiv.org/pdf/2508.01930
- Sun, Yin, Xu, Kolter, Liu: Idiosyncrasies in Large Language Models. ICML 2025. https://arxiv.org/html/2502.12150v2
- Zamaraeva, Gude, Santos-Ríos, Gómez-Rodríguez: I would rather quit NLP than read another paper like this: The rise of antithesis in NLP papers. arXiv 2610.10092, Oct 2026 (preprint). https://arxiv.org/abs/2610.10092
- Lubrano: Beyond Hallucinations: Emphatic Epanorthosis on LLMs. Zenodo, Aug 2025 (data paper). https://zenodo.org/records/16947334
- HumT DumT: Measuring and controlling human-like language in LLMs (checked, not relevant to C). https://arxiv.org/html/2502.13259v1
- Dehumanizing Machines (checked, not relevant to C). https://arxiv.org/pdf/2502.14019

### Pragmatics and usage

- Stanford Encyclopedia of Philosophy: Paul Grice, § 3 Conversational implicature. https://plato.stanford.edu/entries/grice/
- Curzan, That's What They Say: "whether or not". Michigan Public, 14 Apr 2024. https://www.michiganpublic.org/podcast/thats-what-they-say/2024-04-14/twts-whether-or-not-belongs-in-whether-or-not-or-not
- LitReactor column on redundancy (quotes Grammar Girl; secondary). https://litreactor.com/columns/watching-out-for-reiterations-eliminating-redundancy-in-your-writing

### German style and standards

- Becker: Wie Wörter wirken – eine kleine Stilkunde. spielbox, 2024 (quotes Schneider, Deutsch für Profis, p. 57). https://www.spiel-des-jahres.de/wp-content/uploads/2024/05/Becker-Wie-Woerter-wirken.pdf
- tekom: Regelbasiertes Schreiben, 2nd ed. 2013, sample with TOC. https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf
- DIN 8581-1:2024-05 TOC. https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download
- ISO 24495-1:2023. https://iso.org/standard/78907.html

### Dictionaries

- Duden: schweigen. https://www.duden.de/rechtschreibung/schweigen
- Duden: sprechen. https://www.duden.de/rechtschreibung/sprechen
- Wiktionary: schweigen. https://de.wiktionary.org/wiki/schweigen
- Linguee: "the contract is silent on" (EU parallel texts). https://www.linguee.de/deutsch-englisch/search?source=englisch&query=the+contract+is+silent+on

### Law

- BGB § 455 (Billigungsfrist). https://www.gesetze-im-internet.de/bgb/__455.html
- GmbHG § 29 (Ergebnisverwendung). https://www.gesetze-im-internet.de/gmbhg/__29.html
- AktG § 58 (Verwendung des Jahresüberschusses). https://www.gesetze-im-internet.de/aktg/__58.html
- BAG, Urteil vom 13.12.2006, 10 AZR 674/05. https://lexetius.com/2006,3707

### Seen only as search snippets (verify before use)

- Justia Legal Dictionary: silent. https://dictionary.justia.com/silent
- Adams on Contract Drafting: "Is Silent On". https://www.adamsdrafting.com/is-silent-on/
- Grammarist on "whether or not" (via search summary). No URL confirmed.

### Anthropic

- Claude prompting best practices (no list of style tics). https://platform.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices
