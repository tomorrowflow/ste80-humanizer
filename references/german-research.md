# German research: adapting the skill for German text

Research notes for a German mode of `ste80-humanizer`. Researched in November 2026. Every claim has a link. "Unverified" marks a point that no primary source confirmed. Paywalled standards (tekom, DIN, IEC) are described only from their public tables of contents, publisher pages and reviews. Rule titles from those standards are short paraphrases, not rule text.

The task started from a first analysis with these claims: S7 pushes Perfekt to Präteritum; S1 chops Nebensätze; S10 backfires on Partikelverben; S12 fights German compounds; S6 mishandles passive, "man" and Zustandspassiv; §1 flags normal German; Modalpartikeln get cut; §8 bans the Gedankenstrich; §21 replaces „…“; §10 and §20 carry English logic; S9 misses "muss nicht" and "werden"; S15 confuses contractions with "im/zum/beim"; the checker splits umlaut words and mis-splits sentences. Section 2 confirms, corrects or contradicts each point.

## 1. Summary

1. **Do not apply the English Pass 2 to German.** German has its own controlled-language catalog (tekom, 2nd ed. 2013) and its own plain-language standard (DIN 8581-1:2024-05). Both cover the German problems that STE does not: Satzklammer, Genitiv chains, Funktionsverbgefüge, compounds with hyphens. Build Pass 2-DE on their public tables of contents. [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [DIN 8581-1 TOC](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download)
2. **There is no "DIN 8581-1:2025".** The current edition is 2024-05 (26 pages). The 2025 document is DIN SPEC 33429:2025-03, which covers Leichte Sprache, a different target group. [DIN Media 8581-1](https://www.dinmedia.de/de/norm/din-8581-1/377238273), [DIN Media SPEC 33429](https://dinmedia.de/de/technische-regel/din-spec-33429/387728031)
3. **Tense: do not convert, but do not ban Präteritum either.** Duden says Präteritum is the main tense for written narration and reports, Perfekt is the main tense in speech, and Perfekt is required when a past event still matters now. So the first analysis is half right: blind conversion is wrong in both directions. [Duden: Perfekt vs. Präteritum](https://www.duden.de/sprachwissen/sprachratgeber/Perfekt-vs-Pr%C3%A4teritum)
4. **Keep Partikelverben.** Replace the English phrasal-verb rule with a Satzklammer rule: keep the verb, keep the bracket short. tekom has a rule against far-apart verb parts, and DIN 8581-1 has a section on the Verbalklammer. [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf)
5. **Replace the noun-stack rule** with rules on long compounds, Genitiv chains and attribute chains. Use the hyphen rules of the Amtliches Regelwerk (§ 44 mandatory Durchkopplung, § 45 optional hyphen for clarity). [Amtliches Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf)
6. **The Gedankenstrich is correct German, but heavy dash use is still a tell.** Contradiction of the first analysis: German Wikipedia lists typographic en dashes as a weak sign of AI text. But the Regelwerk (§ 77 in 2024) defines four legitimate uses, and the en dash also serves as the bis-Strich, Streckenstrich, list dash and in Swiss money amounts (`Fr. 23.–`). Act on density, never on single dashes, and never touch the non-pause uses. [de.WP Anzeichen](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte), [Schreibweisungen BK](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf)
7. **Zero dashes is now a tell too.** English Wikipedia moved em-dash overuse to "Historical indicators" (2022 to September 2026). It says the newest models avoid dashes and lean on commas and periods instead. A rewrite that strips every dash copies that newer pattern. [en.WP Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
8. **Keep German quotation marks.** „…“ (Germany, Austria) and «…» (Switzerland) are standard in prose. The Swiss federal rules require «…» and forbid »…« in official texts. Only tekom offers "avoid typographic quotes" as a house-style option for technical docs. The checker today flags the German closing mark “ as a "curly quote". [Schreibweisungen BK, Rz. 202](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf), [Duden Anführungszeichen](https://www.duden.de/sprachwissen/rechtschreibregeln/anfuehrungszeichen)
9. **Keep §1 for German.** Contradiction of the first analysis: German Wikipedia names "nicht nur …, sondern auch" as a "negative Parallelismus" tell. The construction is grammatical, so act on density and context, like in English. [de.WP Anzeichen](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte)
10. **Add sourced German tells:** sentence-initial "Darüber hinaus", "Des Weiteren", "Zusätzlich", "Allerdings" (UZH corpus study); Partizip-I riders ("…, die Bedeutung unterstreichend"); German chatbot residue; calques like "Sinn machen" and "am Ende des Tages". [Shaitarova et al. 2024](https://aclanthology.org/2024.swisstext-1.9.pdf), [BK Anglizismen 2020](https://www.bk.admin.ch/dam/de/sd-web/74OxqPY0G4gH/empfehlungen-anglizismen-maerz-2020.pdf)
11. **Keep Modalpartikeln outside technical docs.** IDS grammis defines them as markers of the speaker's and hearer's attitudes and expectations, typical of speech. Cutting them changes the speech act, not just the length. In procedures, tekom's "avoid softeners" and "no superfluous words" rules still allow cuts. [grammis Abtönungspartikel](https://grammis.ids-mannheim.de/terminologie/2)
12. **Modals need a meaning check, not a swap list.** "muss nicht" means no obligation, "darf nicht" means a ban. "werden" can be future, passive or a guess ("Sie wird jetzt zu Hause sein"). [Duden Modalverben](https://duden.de/sprachwissen/sprachratgeber/modalverben), [grammis werden](https://grammis.ids-mannheim.de/verbvalenz/401217)
13. **"im/zum/beim" are not contractions.** They are standard fused forms. Some are fixed, and expanding them can change the meaning ("im Urlaub" vs "in dem Urlaub"). Only spoken-style forms with an apostrophe ("geht's") are the German equivalent of English contractions. [grammis: In Urlaub oder im Urlaub?](https://grammis.ids-mannheim.de/fragen/35), [Amtliches Regelwerk 2024, § 80](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf)
14. **Gender-fair forms: keep the writer's system and keep it consistent.** The Rat für deutsche Rechtschreibung does not include Genderstern, colon or underscore in the official rules. Swiss federal texts forbid them and also forbid the generic masculine. The skill must not add, remove or switch gender forms. It should treat a Paarform as one unit for sentence length. [Rat PM 15.12.2023](https://www.rechtschreibrat.com/DOX/rfdr_PM_2023-12-15_Geschlechtergerechte_Schreibung.pdf), [BK Leitfaden 2023](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf)
15. **The checker needs a German mode.** Confirmed by test: `[A-Za-z]` splits "Größe" into "Gr" and "e" and turns "Übersicht" into "bersicht". The splitter breaks after "z.", "3." (ordinals), "S." and "Kap." and never breaks before "Ä", "Ö", "Ü", „ or «. English regexes (passive, perfect, -ing, phrasal verbs) find nothing useful in German. Section 5 lists the fixes.

## 2. Findings by research question

### 2.1 German controlled-language and comprehensibility standards

#### tekom "Regelbasiertes Schreiben: Deutsch für die Technische Kommunikation"

- **Editions.** 1st edition January 2011, 2nd extended edition October 2013 (ISBN 978-3-9814055-9-0). Published by tcworld/tekom, developed with the ZVEI. No 3rd edition turned up in searches or in tekom's catalogs. [Leseprobe 2013](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf)
- **Status.** Paywalled. It is a catalog, not a recommendation: users pick rules for their own house style. Some rules come in a/b pairs with opposite choices (for example B 102a/b on hyphens in three-part compounds). A vendor whitepaper (secondary) says the guideline "spricht keine Empfehlungen aus". [Congree whitepaper](https://live.tekom.de/fileadmin/user_upload/conference-F21/exhibitors/Congree_Language_Technologies_GmbH/Congree-Whitepaper-Sprachpruefung-tekom-Leitlinie_de.pdf)
- **Advice on scope.** The sample pages say occasional authors should get no more than ten rules, and more than 20 rules need a checking tool. This supports a short German rule set.
- **Relevant rules (IDs and paraphrased titles from the public TOC):**

| Area | tekom rules |
|---|---|
| Ambiguity | S 101/S 102 pronoun references, S 103 misleading Genitiv constructions, S 104 to S 107 unclear syntactic roles and attributes |
| Incomplete sentences | S 201 conditions as "wenn"/"falls" clauses, S 202 no sentences without a verb, S 203 use articles, S 204 do not drop word parts |
| Complexity | S 301 piled-up noun phrases, S 302 overlong sentences, S 303 participle constructions, S 304 piled-up prepositional phrases, S 305 far-apart verb parts, S 308 "es" as placeholder, S 309 to S 311 brackets, insertions and stacked subordinate clauses, S 312 main-clause chains, S 313 at most two simultaneous actions, S 314 no double negation |
| Style | S 501 avoid Vorgangspassiv, S 502 avoid passive with agent, S 503 avoid passive with modal verbs, S 505 avoid nominalizations, S 506a direct address, S 506b instructions as imperative infinitive, S 507 use present tense, S 508 no Konjunktiv, S 509 avoid modal verbs, S 511 avoid "sein + zu + infinitive", S 512 no long sentences for important information |
| Compounds | B 101 to B 117: when to hyphenate compounds (by number of parts, with abbreviations, digits, units, product names, loanwords) |
| Words | L 101 vague verbs, L 103 avoid Funktionsverbgefüge, L 104 avoid impersonal pronouns, L 105 evaluative terms, L 108 superfluous words, L 109 colloquial words, L 110 softeners (Weichmacher), L 112 stock phrases (Floskeln), L 113 morphological variants |
| Punctuation | Z 103a avoid typographic quotes, Z 103b straight quotes for UI text, Z 106 no apostrophe, Z 109 no Gedankenstriche, Z 116 no semicolon |

Source for the whole table: [tekom Leseprobe 2013, pp. 3 to 8](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf). The rule bodies (thresholds, examples) are paywalled. The sentence-length number behind S 302 is not public: unverified.

Note: tekom Z 103a and Z 109 partly support the current §21 and §8 for technical documentation. That contradicts the first analysis, but only for that text type and only as a house-style choice.

#### DIN 8581-1:2024-05 "Einfache Sprache: Anwendung für das Deutsche, Teil 1"

- Current, 26 pages, by the DIN committee NAT (AK Einfache Sprache). It applies DIN ISO 24495-1 to German and targets general readers, not Leichte Sprache readers. Paywalled. [DIN Media](https://www.dinmedia.de/de/norm/din-8581-1/377238273)
- Its public TOC is the closest German match to Pass 2. Sentence level: 6.1 sentence length, 6.2 sentence structure, 6.3 references, 6.4 Verbalklammer, 6.5 Nominalklammer, 6.6 Genitiv, 6.7 attribute chains, 6.8 negation, 6.9 ellipses, 6.10 tenses, 6.11 Konjunktiv, 6.12 passive. Word level: 7.1.1 consistent use, 7.2 word length, 7.3 nominalizations, 7.4 Funktionsverbgefüge, 7.5 modal verbs, 7.7 abbreviations, 7.8 special characters, 7.9 numbers. Style: 5.2.2 direct address, 5.2.3 gender-fair language, 5.2.4 Nominalstil. [DIN 8581-1 TOC](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download)
- The actual numbers (sentence length, bracket length) are not public: unverified.
- ISO 24495-1:2023 is the parent standard. Its first principle is that readers get what they need ("relevant"). [ISO 24495-1](https://iso.org/standard/78907.html), [DIN TOC of DIN ISO 24495-1](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:370015899/toc-3456451/download)

#### Leichte Sprache

- **DIN SPEC 33429:2025-03** "Empfehlungen für Deutsche Leichte Sprache", 60 pages, free PDF from DIN Media. Its TOC has rules on synonyms (5.2.3), long words and special characters for word division (5.2.9, 5.2.10), Verbalstil, Genitiv, negation, passive, Konjunktiv, tenses (5.3.3 to 5.3.8), and a section on Helvetismen and Swiss Standard German (5.6). [DIN SPEC TOC](https://www.din.de/de/wdc-beuth:din21:387728031/toc-3594547/download), [DIN Media](https://dinmedia.de/de/technische-regel/din-spec-33429/387728031)
- **Netzwerk Leichte Sprache** rules: W4 always the same words, W5 short words and split long words with a hyphen, W7 use verbs, W8 active words, W9 avoid Genitiv, W10 avoid Konjunktiv, W11 positive wording, S1 short sentences with one statement each. [Regelwerk NLS](https://www.netzwerk-leichte-sprache.de/fileadmin/content/documents/regeln/Regelwerk_NLS_web.pdf)
- **Use for the skill:** an outer limit only. Splitting compounds with a hyphen ("Bundes-Tag") breaks standard orthography and must not leak into the Humanize mode.

#### Siemens-Dokumentationsdeutsch and Kontrolliertes Deutsch

- No primary or reliable secondary source for a "Siemens-Dokumentationsdeutsch" turned up: unverified. Kuhn's CNL survey excludes German CNLs on purpose. [Kuhn 2014](https://arxiv.org/abs/1507.01701)
- Verified related work: Anne Lehrndorfer, *Kontrolliertes Deutsch*, Narr 1996 (dissertation LMU 1995). [DDB record](https://www.deutsche-digitale-bibliothek.de/item/DIZBC5PMZABCF3MZ34HPYB5IRQ3E7KDF?lang=en)

#### DIN EN IEC/IEEE 82079-1

- Current standard for instructions for use (IEC/IEEE 82079-1:2019; German edition date differs by listing). Paywalled. A tekom slide deck names comprehensibility among the required qualities. No public clause text on sentence rules: unverified. [DIN listing](https://www.din.de/de/wdc-beuth:din21:309431420), [tekom slides](https://www.tekom.de/fileadmin/user_upload/Regionalgruppe_Bodensee/FolSatz-sg-82097-1_ed2-20607-V1-2.pdf)

#### Administrative style guides

- **Bundesverwaltungsamt "Bürgernahe Verwaltungssprache"** (BBB-Arbeitshandbuch, 4th ed. 2002): has sections on clear sentence structure, appropriate sentence length and avoiding nested sentences. The word numbers were not verified. [Bochum copy](https://www.ruhr-uni-bochum.de/vt/arbeitshandbuchBVamt.doc)
- **BMJ Handbuch der Rechtsförmlichkeit:** 4th edition 2024 (BAnz AT 31.10.2024), cited in a Bavarian regulation. [gesetze-bayern.de](https://www.gesetze-bayern.de/Content/Pdf/BayVwV312180-23?all=False). An older edition says one statement per sentence (Rz. 97), per Höfler 2011. [Höfler, LeGes 2011](https://simon.ifi.uzh.ch/hoefler/hoefler2011leges.pdf). No sentence-length number verified.
- **Austrian Legistisches Handbuch:** a search snippet shows a heading "Satzlänge bis zu 20 Wörtern". Not opened: unverified. [Steiermark PDF](https://www.eap.steiermark.gv.at/cms/dokumente/11682114_74838392/2e74bd7f/C_Gesamter_Abschnitt.pdf)
- **Swiss Bundeskanzlei:** "Schreibweisungen", 2nd ed. 2013, corrected 2015, binding for official federal texts, recommended for ordinary correspondence. Details in 2.3. [Schreibweisungen](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf), [BK Guidelines](https://www.bk.admin.ch/de/guidelines). The Swiss language law (Art. 7 Abs. 1 SpG) asks for "sachgerechte, klare und bürgerfreundliche Sprache". [BK Leitfaden 2023](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf)

#### Hamburger Verständlichkeitsmodell

- Langer, Schulz von Thun and Tausch, *Sich verständlich ausdrücken* (1970s, 10th ed. 2015). Four dimensions: Einfachheit (+2), Gliederung/Ordnung (+2), Kürze/Prägnanz (between 0 and +1), anregende Zusätze (between 0 and +1). [de.WP article](https://de.wikipedia.org/wiki/Hamburger_Verst%C3%A4ndlichkeitskonzept) (secondary)
- **Use for the skill:** the model wants brevity at a middle level, not at the maximum. That supports the 80% idea and argues against cutting every Modalpartikel or aside. Critics note weak theory and vague dimensions (same source).

#### Sentence length numbers

| Claim | Status | Source |
|---|---|---|
| dpa: 9 words is the upper limit for optimal comprehension | Unverified. Found only in a law-firm article table, no dpa document | [Harbst/Risse 2022](https://www.bakermckenzie.com/-/media/minisites/germany-careers/files/2022/harbst_risse_aufmerksamkeitsspanne_wif1_2022.pdf) |
| dpa 13 words "verständlich", 20 words limit | Unverified. No source found | none |
| Reiners, Wolf Schneider numbers | Unverified. No source with numbers found | none |
| ARD Tagesthemen average fell from about 20 to about 13 words | Secondary (search snippet of a Schlicker study) | [Spektrum](https://www.spektrum.de/news/deutsche-sprache-warum-behoerden-unverstaendlich-schreiben/2254713) |
| Hohenheim index uses average sentence length and share of sentences over 20 words | Secondary | [Hohenheim CEO-Klartext 2025](https://komm.uni-hohenheim.de/uploads/media/CEO-Klartext_2025.pdf) |
| Human German sentences in a UZH corpus: mean 18 words (SD 10) | Primary, corpus-specific | [Shaitarova et al. 2024](https://aclanthology.org/2024.swisstext-1.9.pdf) |

Decision: keep the S2 numbers (20/25) for German. German packs more meaning into fewer, longer words, so the same word limit is not looser. Do not cite dpa numbers in the skill.

#### German readability formulas

- **Amstad (1978)** German Flesch: `FRE = 180 − ASL − 58.5 × ASW` (ASL = words per sentence, ASW = syllables per word). Source: Amstad, *Wie verständlich sind unsere Zeitungen?*, diss. Zürich 1978. [de.WP Lesbarkeitsindex](https://de.wikipedia.org/wiki/Lesbarkeitsindex) (secondary)
- **Wiener Sachtextformel** (Bamberger and Vanecek 1984), e.g. WSTF1 = 0.1935·MS + 0.1672·SL + 0.1297·IW − 0.0327·ES − 0.875 (MS = % words with 3+ syllables, SL = sentence length, IW = % words over 6 letters, ES = % one-syllable words). Result is a school grade, 4 to 15. Same source.
- UZH researchers note that readability formulas built for English work poorly for German, which relies more on morphology. [Shaitarova et al. 2024](https://aclanthology.org/2024.swisstext-1.9.pdf)

#### Tense norms (Perfekt vs Präteritum)

- Duden: Präteritum is the main tense for chronological narration in written fiction, reports and non-fiction. Speakers narrate mostly in Perfekt. With modal verbs (three-part forms) even speech prefers Präteritum. Perfekt cannot be replaced when the past event affects the present ("Ich habe meinen Schlüssel verloren."). [Duden](https://www.duden.de/sprachwissen/sprachratgeber/Perfekt-vs-Pr%C3%A4teritum)
- Southern German and Swiss dialects lost the indicative Präteritum ("Präteritumschwund"). [Nübling, Konrad-Duden-Preis 2015](https://cdn.duden.de/public_files/2018-11/Konrad-Duden-Preis_N%C3%BCbling_Braucht_man_Sprachgeschichte_2015.pdf), [Linguistik online, Bern](https://bop.unibe.ch/linguistik-online/article/download/5931/8176)
- tekom S 507 (present tense) covers instructions, not narration.
- **Correction of the first analysis:** a Swiss or southern German writer's Perfekt in emails and changelogs is correct and natural. A Präteritum in a written report is also correct. The skill should keep the writer's tense, not push either way.

#### Modal verbs

- Duden: "darf nicht" = ban, "brauchst nicht" = not necessary. [Duden Modalverben](https://duden.de/sprachwissen/sprachratgeber/modalverben)
- grammis: "werden" + infinitive can express a guess about the present ("Sie wird jetzt zu Hause sein"). Whether "werden" is then a modal or a future auxiliary is disputed. [grammis werden](https://grammis.ids-mannheim.de/verbvalenz/401217), [grammis Futur](https://grammis.ids-mannheim.de/vggf/2229), [grammis Modalverb](https://grammis.ids-mannheim.de/vggf/2199)
- tekom S 509 avoids modal verbs in technical text. DIN 8581-1 has a section 7.5 on modal verbs (content paywalled).

### 2.2 Documented tells of AI-generated German text

#### German Wikipedia: "Wikipedia:Anzeichen für KI-generierte Inhalte"

The page exists and was last edited on 19 November 2026. It belongs to the "WikiProjekt KI". It says no single sign is proof and detectors are unreliable. [Anzeichen](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte), [WikiProjekt KI](https://de.wikipedia.org/wiki/Wikipedia:WikiProjekt_KI_und_Wikipedia)

German phrases it lists (exact wording, short):

| Category | Phrases |
|---|---|
| Chat residue | "Ich hoffe, das hilft", "Natürlich!", "Sicherlich!", "Möchten Sie …", "gibt es noch etwas", "lassen Sie mich wissen", "detailliertere Aufschlüsselung", "hier ist ein" |
| Letter style | "Ich hoffe, diese Nachricht erreicht Sie wohlauf", "Ich schreibe, um …", "Vielen Dank für Ihre Zeit" |
| Knowledge limits | "Bis zu meinem letzten Update", "Stand meines letzten Wissensupdates", "Obwohl spezifische Details begrenzt/rar sind", "basierend auf verfügbaren Informationen", "in den bereitgestellten/verfügbaren Quellen" |
| Inflated significance | "dient als Zeugnis", "spielt eine wichtige/bedeutende Rolle", "unterstreicht seine Bedeutung", "Wendepunkt", "Schlüsselmoment", "tief verwurzelt", "unerschütterliche Hingabe", "festigt" |
| Promotional | "reiches kulturelles Erbe", "reiche Geschichte", "atemberaubend", "unbedingt besuchen", "bleibendes Vermächtnis", "reicher kultureller Teppich", "eingebettet", "im Herzen von" |
| Editorial comment | "es ist wichtig zu bemerken/zu bedenken/zu beachten", "es ist bemerkenswert", "keine Diskussion wäre vollständig ohne" |
| Connectives | "andererseits", "darüber hinaus", "zusätzlich", "außerdem", "ferner" (used mechanically) |
| Section summaries | "zusammenfassend", "abschließend", "insgesamt", a "Fazit" section, a "Herausforderungen" section |
| Negative parallelism | "nicht nur …, sondern auch", "es geht nicht nur um …, sondern" |
| Rule of three | three adjectives or phrases, "sowohl … als auch … und" |
| Shallow analysis | Partizip-I forms "gewährleistend", "hervorhebend", "betonend", "widerspiegelnd". The page says German Wikipedia uses Partizip-I constructions less often than English uses "-ing" forms |
| Vague authority | "Branchenberichte", "Beobachter haben zitiert", "Einige Kritiker argumentieren" |
| False ranges | "von … bis" for members of a set (not for space or time) |
| Formatting | heavy bold, emoji, chatbot list markers, Markdown in wikitext, typographic en dashes (–) instead of hyphens (weak alone, LLMs use more dashes) |
| Writer signals | sudden error-free text, sudden register change, "Konstruktionen, die für das Englische typisch sind" |

The page does not discuss quotation marks.

#### English Wikipedia: "Signs of AI writing"

- Lists curly quotes and title-case headings under "Style". [en.WP](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Moves "Overuse of em dashes" to "Historical indicators (2022 to September 2026)". It says the newest models are often hard-coded to avoid em dashes, and that this makes commas and periods a new sign. It also says AI em dashes are "usually surrounded by spaces", which is the normal German Gedankenstrich style. Same source.
- Cites a 2025 study on German theses with a human recognition rate of 57% for AI texts and 64% for human texts. Same source (study not opened: unverified beyond the citation).
- No German-specific tells beyond that.

#### Academic studies

- **Shaitarova, Bauer, Vamvas, Volk (UZH), SwissText 2024.** ChatGPT texts in English and German, journalistic, scientific and clinical domains. Findings for German: "excessive morpho-syntactic standardization coupled with lexical simplification"; lower morphological diversity than human text; fewer punctuation marks; longer sentences than humans in all four journalistic corpora; academic personas overuse sentence-initial formal connectives "darüber hinaus", "des Weiteren", "allerdings", "zusätzlich", while humans start more often with "so", "seit", "aufgrund". [ACL Anthology](https://aclanthology.org/2024.swisstext-1.9.pdf)
- **No study found** that counts "nahtlos", "ganzheitlich", "maßgeschneidert", "essenziell" or "eintauchen" in German AI text. One vendor blog lists "umfassend", "tiefgreifend", "ganzheitlich", "nachhaltig", "maßgeschneidert". It sells an anti-detection tool, so treat it as weak secondary evidence. [Blog (secondary)](https://gpt-watermark-remover.com/de/blog/typische-ki-woerter-vermeiden)
- Max Planck study on spoken English ("delve" rose after ChatGPT), reported by t3n. It does not cover German words. [t3n (secondary)](https://t3n.de/news/chatgpt-einfluss-sprache-delve-effekt-1693866/)

#### Calques and anglicisms (sourced)

- The Swiss Bundeskanzlei names "Sinn machen" (from "to make sense"), "am Ende des Tages" (from "at the end of the day"), "der Elefant im Raum" and "realisieren" in the sense of "begreifen" as anglicisms built from German words. It advises restraint with anglicisms that only relabel known things (Meeting, Event, Location, canceln). [BK Anglizismen 2020](https://www.bk.admin.ch/dam/de/sd-web/74OxqPY0G4gH/empfehlungen-anglizismen-maerz-2020.pdf)
- Duden marks "etwas macht [k]einen Sinn" as colloquial and "nach englisch something makes sense". [Duden: Sinn](https://www.duden.de/rechtschreibung/Sinn)
- None of these sources says LLMs produce these calques more than people do. Their link to AI text is unverified. Treat them as weak tells and as plain-style fixes.

### 2.3 Typography and orthography the skill must not break

#### Gedankenstrich, Bindestrich, Ergänzungsstrich

- Amtliches Regelwerk 2024, § 77: the Gedankenstrich marks a change of speaker, topic, expectation or construction (an inserted addition, then paired). A comma follows the second dash if the sentence needs one without the insertion. The note after § 77 says the dash is longer than the Divis and, unlike the Divis, does not touch letters. [Amtliches Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf). (In the 2018 text these were § 82 to § 84. [Regeln 2016/2018](https://www.rechtschreibrat.com/DOX/rfdr_Regeln_2016_redigiert_2018.pdf))
- § 81 (2024): the Divis is the Trennstrich, Bindestrich and Ergänzungsstrich. Ergänzungsstrich examples: "Haupt- und Nebeneingang", "ein- und ausladen" (§ 98 in 2018).
- § 44 (2024 and 2018): mandatory hyphens throughout multi-part compounds that contain a word group or a hyphenated part ("A-Dur-Tonleiter", "40-Stunden-Woche", "Hals-Nasen-Ohren-Klinik"). § 45: optional hyphen for clarity or emphasis. The 2024 update adds rules for English compounds ("Facility-Management") and hyphenated colour adjectives. [Overview of 2024 changes](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024_UeberblickAenderungen.pdf)
- Swiss Schreibweisungen (Rz. 230 to 238): the Gedankenstrich is the en dash. It also serves as list dash, Streckenstrich ("Schaffhausen–Bülach–Zürich", no spaces), bis-Strich ("16–17 Uhr", "1939–1945", no spaces, and never "von 1939–1945"), minus sign, and zero replacement in amounts ("Fr. 23.–"; the em dash is not allowed there). Paired dashes with spaces for insertions. [Schreibweisungen](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf)
- DIN 5008:2020 (paywalled): a university summary says the bis-dash has spaces around it ("09:30 – 10:00 Uhr") and that "bis" should be written out when possible. This differs from the Swiss rule. [Uni Passau summary (secondary)](https://www.uni-passau.de/fileadmin/dokumente/beschaeftigte/kommunikation_marketing/webredaktion/DIN_5008.pdf), [DIN Media](https://www.dinmedia.de/de/norm/din-5008/318422674)

#### Quotation marks

- Regelwerk § 79 (2024) defines the uses (direct speech, quotes, mentioned expressions), not the glyph shapes. [Amtliches Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf)
- Duden shows „…“ and ‚…‘ as the standard forms. [Duden](https://www.duden.de/sprachwissen/rechtschreibregeln/anfuehrungszeichen)
- Switzerland: «…» and ‹…› are mandatory in federal texts. »…« (common in German books) is not allowed in Swiss official texts. [Schreibweisungen, Rz. 202](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf)
- tekom Z 103a/b: house-style option to avoid typographic quotes and use straight quotes for UI strings. [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf)

#### Abbreviations, numbers, ß

- Multi-part abbreviations take a space: "z. B.", "d. h.", "u. a.", "u. U.", with a non-breaking space in print. In Swiss legislation, "bzw.", "u. a.", "vgl." and "z. B." are not allowed in running text. [Schreibweisungen, Rz. 413, 438](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf), [Passau DIN 5008 summary](https://www.uni-passau.de/fileadmin/dokumente/beschaeftigte/kommunikation_marketing/webredaktion/DIN_5008.pdf)
- Ordinals take a period ("am 3. Mai", "das 19. Jahrhundert"). At the end of a sentence one period is enough. [Regeln 2016/2018, § 104, § 105](https://www.rechtschreibrat.com/DOX/rfdr_Regeln_2016_redigiert_2018.pdf)
- Digit groups: Swiss federal texts group digits in threes with a fixed space from five digits up ("22 333", "1234"). The apostrophe grouping ("1'000") "should no longer be used" there. Decimal comma, but decimal point for money ("Fr. 23.50"). [Schreibweisungen, Rz. 512, 514](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf). DIN 5008 also groups with spaces (secondary). [Passau summary](https://www.uni-passau.de/fileadmin/dokumente/beschaeftigte/kommunikation_marketing/webredaktion/DIN_5008.pdf)
- ß: in Switzerland and Liechtenstein "ss" can always replace ß (§ 25 E2). [Amtliches Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf). The Swiss federal spelling guide says ß has disappeared and "ss" is always used ("Strasse"). [BK Rechtschreibleitfaden 2017](https://www.bk.admin.ch/dam/de/sd-web/GApRW2tzdhqZ/rechtschreibleitfaden-2017.pdf)
- Letters: in Switzerland the salutation usually has no comma, and the next line starts with a capital (comma section of the 2024 rules, before § 74). [Amtliches Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf)
- Headings: only the first word is capitalized by the heading rule (§ 53). Nouns are capitalized anyway. English title case does not exist in German. [Regeln 2016/2018](https://www.rechtschreibrat.com/DOX/rfdr_Regeln_2016_redigiert_2018.pdf)

### 2.4 Modalpartikeln, register and gender-fair language

#### Modalpartikeln

- grammis (IDS): Abtönungspartikeln mark the expectations and attitudes of the speaker and hearer toward the stated fact. They cannot be asked about or negated, are sensitive to sentence type, cannot start a sentence, form a closed class (aber, auch, bloß, denn, doch, eben, ja, halt, mal, wohl and others) and are typical of spoken language. Example: "Die Läden sind doch schon geschlossen!" presents the fact as already known to the hearer. [grammis terminology](https://grammis.ids-mannheim.de/terminologie/2), [grammis Abtönungspartikeln](https://grammis.ids-mannheim.de/systematische-grammatik/769)
- Duden: they reveal more about the speaker than about the content. [Duden Modalpartikeln](https://www.duden.de/sprachwissen/sprachratgeber/Modalpartikeln)
- Linguistics literature (secondary summary in search results): in imperatives, mal, bloß, eben, ja, nur, doch shape the speech act (request, threat, suggestion, permission). Not verified in the original paper.
- **Effect of cutting:** "Schick mir mal die Datei" (casual request) vs "Schick mir die Datei" (plain order). "Das ist ja bekannt" (shared knowledge) vs "Das ist bekannt" (new claim). The first analysis is right.
- **Hypothesis, unverified:** LLM German may use fewer Modalpartikeln than human email or chat text. The UZH study's "morpho-syntactic standardization" fits this, but no study counted particles.

#### du and Sie

- tekom S 506a and DIN 8581-1 5.2.2 ask for direct address. Neither source decides du or Sie. The skill must keep the source's form of address and never switch it. (Editorial decision, consistent with the existing "keep the writer's voice" rule.)

#### Gender-fair language

- Rat für deutsche Rechtschreibung (14 July 2023, explained 15 December 2023): Genderstern, underscore, colon and other inner-word signs are not recommended for the official rules. Criteria for gender-fair texts: factually correct, understandable and readable, readable aloud, legally clear, transferable to other languages, focused on core facts, and easy to learn. [Rat PM 15.12.2023](https://www.rechtschreibrat.com/DOX/rfdr_PM_2023-12-15_Geschlechtergerechte_Schreibung.pdf). The 2024 rules add a note that these signs are not part of the "Kernbestand" of German orthography and may cause grammatical follow-up problems ("der*die Präsident*in"). [Overview 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024_UeberblickAenderungen.pdf)
- Swiss Bundeskanzlei, Leitfaden 3rd ed. 2023 (PDF June 2024), binding for federal texts: allowed means are Paarformen, nominalized participles ("Stimmberechtigte"), gender-neutral nouns, collective nouns and rewording. The generic masculine is not allowed. Slash short forms only in condensed text. Brackets, Binnen-I, asterisk and colon are not allowed. [BK Leitfaden](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf)
- Interaction with Pass 2 (same Leitfaden): many Paarformen hurt readability (Rz. 16). Keep the order of a Paarform the same through the text (Rz. 17). Do not use rewording without a person if it hides who acts (Rz. 57, example "Übertragbare Krankheiten sind der zuständigen Behörde zu melden"). This matches S6 and S11.

## 3. Mapping table

Decisions: **keep** (works as is), **adapt** (keep the goal, change the method or the word list), **drop** (does not apply to German).

### Pass 1

| Rule | Decision | Reason | Source |
|---|---|---|---|
| §1 Not X but Y | keep, density-based | de.WP lists "nicht nur …, sondern auch" and "es geht nicht nur um …, sondern" as a tell. It is grammatical, so one sighting in a real contrast is fine. Contradicts the first analysis. | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §2 One-line closers | keep | Same pattern in German ("Und genau das macht den Unterschied."). No German source: German list unverified. | none |
| §3 Fake depth | adapt word list | Add "im Kern", "letztlich geht es um", "am Ende des Tages" (BK calque). | [BK Anglizismen](https://www.bk.admin.ch/dam/de/sd-web/74OxqPY0G4gH/empfehlungen-anglizismen-maerz-2020.pdf) |
| §4 Staged run-up | adapt word list | "Lass uns eintauchen", "Tauchen wir ein", "Hier ist, was du wissen musst": plausible, unverified. | none |
| §5 Arguing with no one | keep | No German source. | none |
| §6 Forced triads | keep | de.WP lists "Trikolon" and "sowohl … als auch … und". | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §7 Repeated openings | adapt | Add sentence-initial "Darüber hinaus", "Des Weiteren", "Zusätzlich", "Allerdings", "Außerdem", "Ferner". | [Shaitarova et al.](https://aclanthology.org/2024.swisstext-1.9.pdf), [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §8 Dashes | adapt | The German Gedankenstrich is an en dash with spaces and has four legal uses. Act only on density (as a pause substitute). Never touch bis-Strich, Streckenstrich, list dash, minus, "Fr. 23.–", Ergänzungsstrich. Do not reach zero dashes on purpose: dash-free, comma-heavy text is a newer tell. A Geviertstrich (—) in German text is non-standard and can be fixed. | [Regelwerk § 77](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf), [BK Rz. 230 to 238](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf), [en.WP](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §9 Stacked qualifiers | adapt word list | "könnte möglicherweise", "unter Umständen eventuell", "potenziell möglicherweise". tekom L 110 (softeners) supports the goal. | [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| §10 Hyphenated pairs | drop, replace | The English predicative-hyphen logic has no German equivalent. Replace with a compound-spelling check: no open compounds from English style ("Software Entwicklung" → "Softwareentwicklung" or "Software-Entwicklung"), keep Durchkopplung ("E-Mail-Adresse"). Whether open compounds are an AI tell is unverified; they are an orthography error by § 44/§ 45. | [Regelwerk §§ 44, 45](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf) |
| §11 Passive, missing subject | adapt | Same goal. Allow "man" and Zustandspassiv when the actor does not matter. Watch "sein + zu" ("ist zu melden"). | [tekom S 501, S 502, S 511, L 104](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [BK Leitfaden Rz. 57](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf) |
| §12 AI words | adapt word list | Use the de.WP list plus the UZH connectives. Do not translate the English list one to one. "nahtlos", "maßgeschneidert", "ganzheitlich", "essenziell", "eintauchen": candidates only, unverified. | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §13 Inflated significance | adapt word list | "spielt eine zentrale/wichtige Rolle", "Meilenstein", "Wendepunkt", "Schlüsselmoment", "unterstreicht die Bedeutung", "Zeugnis". | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §14 Vague association | keep | "im Zusammenhang mit", "verbunden mit". German list unverified. | none |
| §15 -ing riders | adapt | German form: Partizip-I riders ("…, die Bedeutung unterstreichend") and relative add-ons (", was … unterstreicht"; unverified). | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte), [tekom S 303](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| §16 Sales language | adapt word list | "atemberaubend", "im Herzen von", "eingebettet", "reiches kulturelles Erbe". | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §17 Borrowed authority | adapt word list | "Branchenberichte", "Beobachter", "Einige Kritiker argumentieren", "Experten sind sich einig". | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §18 Avoiding is/has | adapt word list | "dient als", "steht als", "fungiert als". | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §19 Bold as decoration | keep | de.WP lists heavy bold. | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §20 Decorative headings | adapt | No title case in German; nouns stay capitalized. Flag capitalized adjectives and verbs in headings ("Die Neuen Funktionen" → "Die neuen Funktionen"). Two-part headings with a colon are also a de.WP sign. | [Regelwerk § 53 (2018)](https://www.rechtschreibrat.com/DOX/rfdr_Regeln_2016_redigiert_2018.pdf), [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §21 Curly quotes | adapt | In German prose keep „…“ or «…». Flag English-style “…” in German text and mixed systems. Straight quotes only in code, Markdown syntax or by house style (tekom Z 103). | [Duden](https://www.duden.de/sprachwissen/rechtschreibregeln/anfuehrungszeichen), [BK Rz. 202](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf) |
| §22 Chatbot residue | adapt word list | de.WP list (see 2.2). | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §23 Knowledge limits | adapt word list | de.WP list (see 2.2). | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §24 Heading repeated | keep | Language-neutral. | none |
| §25 Text about the document | adapt word list | "In diesem Artikel werden wir …", "Die folgende Tabelle zeigt". de.WP also lists "Zusammenfassend", "Abschließend", "Fazit" sections. | [de.WP](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| §26 Re-explaining | keep | Language-neutral. | none |

### Pass 2

| Rule | Decision | Reason | Source |
|---|---|---|---|
| S1 One idea per sentence | adapt | Keep the goal. A Nebensatz that carries the logic (weil, wenn, dass, obwohl) stays. Split chains of Nebensätze and inserted clauses instead. The first analysis is right that splitting every Nebensatz breaks German. | [tekom S 311, S 402, S 313](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [DIN 8581-1 6.2](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download) |
| S2 Sentence length | keep 20/25, adapt counting | Count a Paarform, a number with unit, "z. B." and a grouped number ("1 000") as one word. No German primary source gives a better number. | see 2.1 |
| S3 Condition first | keep | tekom S 201: conditions as "wenn"/"falls" clauses. | [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| S4 Keep articles and verb | keep | tekom S 202, S 203. Keep the Ergänzungsstrich ("Ein- und Ausgang"): it is standard (§ 81, § 98 in 2018). tekom S 204 (do not drop word parts) is a house-style option only. | [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf) |
| S5 Lists | keep | tekom S 306, S 307, T 603. Swiss list dash is the en dash. | [tekom TOC](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [BK Rz. 232](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf) |
| S6 Active voice | adapt | Name the actor when it matters. Allow "man", Zustandspassiv ("Die Datei ist gespeichert") and passive without agent when the actor is unknown. Convert passive with agent ("wird vom Server geprüft" → "Der Server prüft"). In instructions, use the Sie-imperative or the infinitive by house style. | [tekom S 501 to S 506b, L 104](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [BK Leitfaden Rz. 57](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf) |
| S7 Simple tenses | adapt | Allowed: Präsens, Präteritum, Perfekt, Futur I. Keep the writer's past tense. Perfekt is required for results that still hold. Präteritum for modal verbs and "sein"/"haben" is fine everywhere. Avoid Plusquamperfekt chains and Futur II. Präsens in instructions. | [Duden](https://www.duden.de/sprachwissen/sprachratgeber/Perfekt-vs-Pr%C3%A4teritum), [tekom S 507](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| S8 Verbs, not nouns | adapt | German Nominalstil and Funktionsverbgefüge. Keep FVG with their own meaning ("in Kraft treten", "zur Verfügung stellen"; editorial judgment, unsourced). "-ing chains" become Partizip-I constructions. | [tekom S 505, L 103, S 303](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [DIN 8581-1 5.2.4, 7.3, 7.4](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download) |
| S9 Honest modals | adapt | Keep the source's modal. Check negation: "muss nicht" ≠ "darf nicht". Check "werden": future, passive or guess. "sollte" carries advice, keep it. | [Duden](https://duden.de/sprachwissen/sprachratgeber/modalverben), [grammis](https://grammis.ids-mannheim.de/verbvalenz/401217) |
| S10 Plain words | adapt | Prefer the established German word over a Fremdwort or a new anglicism when they mean the same ("verwenden" over "utilisieren"; "absagen" over "canceln"). Keep established technical anglicisms and Fremdwörter that experts use. Drop the phrasal-verb clause: Partikelverben ("einrichten", "ausschalten") are the plain words. The first analysis is right. | [BK Anglizismen](https://www.bk.admin.ch/dam/de/sd-web/74OxqPY0G4gH/empfehlungen-anglizismen-maerz-2020.pdf), [tekom L 107](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| S11 One term per thing | keep, extend | Includes one gender-fair form per text and one Paarform order. | [NLS W4](https://www.netzwerk-leichte-sprache.de/fileadmin/content/documents/regeln/Regelwerk_NLS_web.pdf), [tekom L 113](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [BK Leitfaden Rz. 17](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf) |
| S12 Noun stacks | replace | German equivalents: long compounds, Genitiv chains, attribute chains, piled-up prepositional phrases. Fix with a hyphen (§ 45), a relative clause or a verb. Not "of"/"for". | [DIN 8581-1 6.6, 6.7](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download), [tekom S 103, S 301, S 304](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| S13 Paragraphs | keep | Language-neutral. | none |
| S14 Steps and warnings | keep | Language-neutral; IEC/IEEE 82079-1 covers warnings (paywalled). | [DIN listing](https://www.din.de/de/wdc-beuth:din21:309431420) |
| S15 Punctuation | adapt | Semicolon: keep "avoid" (tekom Z 116), though the Regelwerk allows it (§ 74). Contractions: "im/zum/beim/am/ins" are not contractions, never expand. Strict mode may ban spoken forms with apostrophe ("gibt's") and write "zum Beispiel" for "z. B." | [tekom Z 116, B 201](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [grammis](https://grammis.ids-mannheim.de/fragen/35), [BK Rz. 413](https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf) |

### Before and after pairs

All examples are written for this file.

| Rule | Before | After |
|---|---|---|
| S7 | `Wir behoben den Fehler im Login. Er tritt nicht mehr auf.` | `Wir haben den Fehler im Login behoben. Er tritt nicht mehr auf.` (result still holds, so Perfekt) |
| S7 | `Ich habe gestern nicht kommen können.` | `Ich konnte gestern nicht kommen.` (modal verb, Präteritum is the plain form) |
| S10 | `Implementieren Sie die Konfiguration gemäß der Dokumentation.` | `Richten Sie die Konfiguration nach der Anleitung ein.` |
| S10 + Klammer | `Richten Sie, bevor Sie den Server zum ersten Mal mit dem Netzwerk verbinden und die Benutzerkonten anlegen, die Firewall ein.` | `Richten Sie zuerst die Firewall ein. Verbinden Sie danach den Server mit dem Netzwerk und legen Sie die Benutzerkonten an.` |
| S12 | `die Überprüfung der Einhaltung der Vorgaben des Datenschutzes` | `prüfen, ob die Datenschutzvorgaben eingehalten werden` |
| S8 | `Die Durchführung der Migration erfolgt am Freitag.` | `Wir migrieren die Daten am Freitag.` (if the source names the actor) |
| S9 | `Sie müssen das Feld nicht ausfüllen.` → never `Sie dürfen das Feld nicht ausfüllen.` | (meaning changes from optional to forbidden) |
| §1 | `Das Tool ist nicht nur schnell, sondern auch sicher und skalierbar.` | `Das Tool baut ein Projekt in zehn Sekunden und verschlüsselt alle Daten.` (only with facts from the source) |
| §7 | `Darüber hinaus unterstützt es CSV. Zusätzlich gibt es eine API. Des Weiteren …` | `Es liest CSV und hat eine API.` |
| §8 | `Die Migration – die sechs Wochen dauerte – ist fertig – endlich.` | `Die Migration dauerte sechs Wochen und ist jetzt fertig.` but keep `Zürich–Bern`, `9–12 Uhr`, `Fr. 23.–` |
| §21 | `Er nannte das Feature “bahnbrechend”.` | `Er nannte die Funktion „bahnbrechend“.` (CH: `«bahnbrechend»`) |
| Modalpartikel | `Kannst du mir mal kurz die Datei schicken?` | keep as is in a chat or email. Do not cut "mal kurz". |

## 4. New German-specific tells and rules

### New tells (Pass 1-DE)

| Proposed | Watch for | Evidence |
|---|---|---|
| Formal connective openers | Sentence-initial "Darüber hinaus", "Des Weiteren", "Zusätzlich", "Allerdings", "Ferner", "Außerdem", several per paragraph | UZH corpus study, de.WP. [Shaitarova et al.](https://aclanthology.org/2024.swisstext-1.9.pdf) |
| Partizip-I riders | ", … unterstreichend", "gewährleistend", "hervorhebend", "widerspiegelnd" | de.WP. [Anzeichen](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) |
| English constructions in German | "macht Sinn", "am Ende des Tages", "der Elefant im Raum", "realisieren" for "merken"; possibly "in 2024" for "2024" or "im Jahr 2024" (unverified) | BK, Duden, de.WP ("Konstruktionen, die für das Englische typisch sind") |
| Wrong typography system | English “…” in German text, em dash (—) as Gedankenstrich, "z.B." without space, "1,000" for 1000 | Typography rules above. As an AI tell: unverified |
| False range | "von … bis …" across members of a set ("von Start-ups bis zu Konzernen") | de.WP |
| Letter clichés from English | "Ich hoffe, diese Nachricht erreicht Sie wohlauf" | de.WP |
| Fazit and Herausforderungen sections | a closing "Fazit" or "Herausforderungen" section in reference text | de.WP |
| Uniform, punctuation-poor text | few commas and dashes, steady sentence length, low word-form variety | UZH study (fewer punctuation marks, lower morphological diversity), en.WP (dash-free models) |

### New rules (Pass 2-DE)

| Proposed | Rule | Source |
|---|---|---|
| D1 Satzklammer | Keep the verb bracket short. Put long information outside the bracket (Ausklammerung) or in a new sentence. No public number exists; an editorial default is "about 10 words in the Mittelfeld" (unverified). | [tekom S 305](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [DIN 8581-1 6.4, 6.5](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download) |
| D2 Genitiv chains | At most two Genitiv attributes in a row. | DIN 8581-1 6.6, tekom S 103 (thresholds paywalled) |
| D3 Compounds | Write compounds as one word or with a hyphen (§ 44/§ 45), never open. Long compounds (house default: over about 20 letters, unverified) may get a clarifying hyphen. Never split in the Leichte Sprache style. | [Regelwerk 2024](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf) |
| D4 Modalpartikeln | Keep them in emails, chats, posts and personal text. Cut them only in procedures and reference text. | [grammis](https://grammis.ids-mannheim.de/terminologie/2), [tekom L 108, L 110](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |
| D5 Register | Keep du or Sie and the regional standard (de-DE, de-AT, de-CH). Do not convert ss to ß or back. | [Regelwerk § 25 E2](https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf) |
| D6 Gender-fair forms | Keep the writer's system. Do not add or remove gendering. Use one form per text. Count a Paarform as one unit for S2. | [Rat](https://www.rechtschreibrat.com/DOX/rfdr_PM_2023-12-15_Geschlechtergerechte_Schreibung.pdf), [BK Leitfaden](https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf) |
| D7 Konjunktiv | Keep Konjunktiv I in reported speech (it marks a source). Cut Konjunktiv II politeness only in procedures. | [tekom S 508](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [DIN 8581-1 6.11](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download). The reported-speech point is editorial. |
| D8 Negation | No double negation. Prefer a positive statement when it keeps the meaning. | [tekom S 314](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf), [DIN 8581-1 6.8](https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download) |
| D9 "sein + zu" and "es" | Avoid "ist zu prüfen" and placeholder "es" ("Es wird empfohlen, …") when the actor matters. | [tekom S 308, S 511](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) |

## 5. Checker changes for German

All behaviour below was tested against the current `scripts/ste_check.py` unless marked "proposed".

### Confirmed bugs

- `WORD_RE = [A-Za-z]…` gives `['Die', 'Gr', 'e', 'der', 'bersicht', 'ndert', 'sich']` for "Die Größe der Übersicht ändert sich." (7 words instead of 6, and broken tokens).
- `sentences()` splits "Das ist z. B. gut." after "z.", splits "Am 3. Mai" after "3.", splits "Siehe S. 4 bzw. Kap. 2." into four parts, and does not split before "Änderungen", „ or «, because the lookahead is `[A-Z0-9"'(]`.
- The curly-quote check `[“”‘’]` fires on correct German „Hallo“ (the closing mark is U+201C) and on the apostrophe ’. It ignores «…».
- The dash check flags only "—" and " -- ". It does not flag the en dash. So SKILL.md §8 (which bans en dashes) and the checker already disagree.
- The English tells, PASSIVE_RE, PERFECT_RE, PROGRESSIVE_RE, the "-ing" checks and PHRASAL find nothing in German. "nicht nur … sondern auch" goes undetected.

### Proposed changes

1. **Language switch.** Add `--lang {auto,en,de}` and `--variant {de-DE,de-AT,de-CH}`. Auto: count German function words (`der|die|das|und|ist|nicht|mit|für|auf|ein|eine|zu|von`) against English ones and pick the larger share. In `de` mode, skip PASSIVE_RE, PERFECT_RE, PROGRESSIVE_RE, the "-ing" checks, PHRASAL, CONTRACTION_RE and SWAPS.
2. **Word regex.** `WORD_RE = re.compile(r"[^\W\d_][\w'’\-]*|\d[\d.,:/%  -]*")`. Python 3 `str` patterns are Unicode-aware, so `[^\W\d_]` matches ä, ö, ü, ß and accented letters.
3. **Number groups and amounts as one word.** Before counting: `re.sub(r"\d{1,3}(?:[   ]\d{3})+(?:,\d+)?", "NUM", s)` and `re.sub(r"\b(?:Fr|CHF|EUR|€)\.?\s?[\d.–-]+", "NUM", s)`.
4. **German abbreviations.** Protect these before splitting (spaced and unspaced forms): `z. B.`, `z.B.`, `d. h.`, `u. a.`, `u. Ä.`, `o. Ä.`, `u. U.`, `i. d. R.`, `z. T.`, `m. E.`, `bzw.`, `vgl.`, `ca.`, `usw.`, `etc.`, `ggf.`, `evtl.`, `inkl.`, `exkl.`, `sog.`, `resp.`, `Nr.`, `S.`, `Kap.`, `Abs.`, `Art.`, `Ziff.`, `Rz.`, `Bd.`, `Hrsg.`, `Dr.`, `Prof.`, `Hr.`, `Fr.`, `St.`, `Mio.`, `Mrd.`, `Tsd.`, `Std.`, `Min.`, `Jh.`. Suggested pattern: `r"\b(?:[a-zA-ZÄÖÜäöü]\.\s?){1,3}(?=\s)"` for chains like "z. B." plus an explicit list for multi-letter ones.
5. **Ordinals and dates.** Do not split after `\b\d{1,2}\.` when the next word is a month name, a lowercase word, "Jahrhundert", "Kapitel", "Auflage" or another digit group. Keep splitting after four-digit years followed by a capital ("… seit 2023. Danach …").
6. **Split lookahead.** `(?=[A-ZÄÖÜ0-9"'(„«‹»‚])`.
7. **Quotes (de).** Accept „…“, ‚…‘, «…», ‹…›, »…«. Flag: an opening U+201C directly before a word in German text (English style), mixed systems in one file, and »…« when `--variant de-CH`. Never flag ’ as an apostrophe.
8. **Dashes (de).** Ignore: `\d\s?–\s?\d` (ranges), `\b\w+–\w+\b` without spaces (Streckenstrich), `^\s*–\s` (list dash), `\.–` (amounts), `–\d` (minus). Count the rest (spaced pause dashes). Flag when there is more than one per three sentences (house threshold, unverified). Flag every em dash "—" in German text as "not a German dash".
9. **German tells (regexes, case-insensitive).**
   - `\bnicht\s+nur\b[^.!?]{0,120}\bsondern\b` → not-x-but-y
   - `\bes\s+geht\s+nicht\s+(?:nur\s+)?(?:um|darum)\b[^.!?]{0,120}\bsondern\b` → not-x-but-y
   - `\bspielt\s+eine\s+(?:zentrale|wichtige|entscheidende|bedeutende|wesentliche|maßgebliche|massgebliche|Schlüssel)\s*-?\s*Rolle\b` → inflation
   - `\b(?:Meilenstein|Wendepunkt|Schlüsselmoment|Zeugnis|Vermächtnis|tief verwurzelt)\b` → inflation (weak)
   - `\bunterstreicht\s+(?:die|seine|ihre|deren)\s+Bedeutung\b` → inflation
   - `,\s+(?:\w+\s+){0,4}(?:unterstreichend|gewährleistend|hervorhebend|betonend|widerspiegelnd)\b` → ing-rider (Partizip I)
   - `\bes\s+ist\s+(?:wichtig|erwähnenswert|bemerkenswert)(?:,|\s+zu\s+(?:beachten|bemerken|bedenken|erwähnen))` → editorial
   - `\bich\s+hoffe,?\s+(?:das|dies)\s+hilft\b|\blass(?:en\s+Sie|t)?\s+(?:mich|uns)\s+wissen\b|\bmöchten\s+Sie,?\s+dass\s+ich\b|\bmöchtest\s+du,?\s+dass\s+ich\b|^(?:Natürlich|Sicherlich|Gerne|Gute Frage)[!,.]` → chatbot
   - `\b(?:bis\s+zu\s+meinem|stand\s+meines)\s+letzten\s+(?:Wissens)?[Uu]pdates?\b|\bbasierend\s+auf\s+(?:den\s+)?verfügbaren\s+Informationen\b` → knowledge-hedge
   - `\b(?:könnte|kann|dürfte)\s+(?:möglicherweise|eventuell|potenziell|unter\s+Umständen)\b` → stacked-hedge
   - `\b(?:Experten|Studien|Beobachter|Kritiker|Branchenberichte)\s+(?:sagen|zeigen|sind\s+sich\s+einig|argumentieren|betonen)\b` → vague-authority
   - `\b(?:dient|fungiert|steht)\s+als\b` → is-avoidance (weak)
   - `\b(?:atemberaubend\w*|im\s+Herzen\s+(?:von|der|des)|eingebettet\s+in)\b` → sales
   - `\bmacht\s+(?:keinen\s+|wenig\s+|viel\s+)?Sinn\b|\bam\s+Ende\s+des\s+Tages\b|\bElefant\s+im\s+Raum\b` → calque
   - `^(?:Zusammenfassend|Abschließend|Abschliessend|Insgesamt|Fazit)\b` → summary closer
   - Connective density: count sentences that start with `Darüber hinaus|Des Weiteren|Zusätzlich|Ferner|Außerdem|Ausserdem|Allerdings|Andererseits`. Flag when more than about one in five sentences in a paragraph does (threshold unverified).
10. **German structure checks (heuristic, proposed).**
    - Genitiv chain: `\b(?:des|der)\s+\w+(?:\s+\w+)?\s+(?:des|der)\s+\w+(?:\s+\w+)?\s+(?:des|der)\s+\w+` → three Genitiv-like links. It will over-match dative "der"; report as "look here".
    - Long compound: a token of letters only, starting uppercase, longer than 20 characters (threshold unverified).
    - Open compound from English style: two capitalized nouns in a row where the first is a common English loan (`Software|Daten|Cloud|Service|Projekt|Team|User`) and no article or verb between (high false-positive risk, report only).
    - Vorgangspassiv: `\b(?:wird|werden|wurde|wurden)\b(?:\s+\S+){0,10}?\s+(?:ge\w+(?:t|en)|\w+iert)\b` → "possible passive", weak.
    - "sein + zu": `\b(?:ist|sind|war|waren)\s+(?:\S+\s+){0,6}?zu\s+\w+en\b`.
    - Satzklammer: in sentences over 15 words, flag when the last word is a separable particle (`an|auf|aus|ein|mit|vor|zu|ab|zurück|weiter|fest|her|hin|los|fort|nach|dar`) or a Partizip II and the finite verb is more than 10 words before it (thresholds unverified).
    - Modal negation review (strict): flag `\bmuss\s+nicht\b|\bmüssen\s+nicht\b` with "check: no obligation, not a ban".
11. **German swap list (proposed, small).** "utilisieren" → "verwenden"; "generieren" → "erzeugen"; "fokussieren auf" → "sich konzentrieren auf"; "Sinn machen" → "sinnvoll sein, Sinn ergeben"; "zeitnah" → a date or "bald"; "Meeting" → "Sitzung"; "Event" → "Veranstaltung"; "canceln" → "absagen". The last four follow the BK anglicism note; the rest are editorial and unverified.
12. **Contractions (de, strict).** Flag `\b\w+[’']s\b` (geht's, gibt's) only. Never flag `im|am|zum|zur|beim|vom|ins|ans|aufs|übers`.
13. **ß (de-CH).** Flag any "ß" when `--variant de-CH`.
14. **Optional readability (proposed).** Amstad FRE-de with a syllable count by vowel groups (`[aeiouyäöü]+`, treating "ei", "ie", "au", "eu", "äu" as one). Report only, no limit.

## 6. Open questions and unverified points

- **dpa, Reiners, Schneider numbers:** not verified at the source. Only one law-firm article repeats "9 words, dpa". Do not cite them.
- **DIN 8581-1 thresholds:** the sentence-length, Verbalklammer and Genitiv numbers are paywalled. Buying the standard would settle D1 and D2.
- **tekom rule bodies:** the 2013 thresholds (S 302, S 305) and examples are paywalled. No 3rd edition found.
- **Siemens-Dokumentationsdeutsch:** no source found.
- **Handbuch der Rechtsförmlichkeit and BBB handbook:** sentence-length numbers not verified.
- **Austrian Legistisches Handbuch:** "up to 20 words" seen only in a search snippet.
- **German AI vocabulary:** no frequency study for "nahtlos", "ganzheitlich", "maßgeschneidert", "essenziell", "eintauchen". de.WP and the UZH study are the only solid sources.
- **Modalpartikeln in LLM output:** no study found. The claim that LLMs underuse them is a hypothesis.
- **Calques as AI tells:** BK and Duden document "Sinn machen" and "am Ende des Tages" as anglicisms, not as AI tells.
- **Dash direction:** de.WP treats en dashes as a weak AI sign, while en.WP says the newest models avoid dashes. The German mode should measure density against the writer's sample, not aim for zero.
- **Thresholds in section 5** (one pause dash per three sentences, 20-letter compounds, 10-word Mittelfeld, one in five connective openers) are proposals. Calibrate them on human German text, for example the UZH corpora (20 Minuten, Credit Suisse Bulletin, PubMed DE).
- **Austrian specifics** (Austrian quote use, vocabulary) were not researched.
- **Wiener Sachtextformel and Amstad coefficients** come from German Wikipedia, not from the original publications.
- **The 2025 German-thesis detection study** cited by en.WP was not opened.

## 7. Sources

### Standards and official bodies

- tekom: Regelbasiertes Schreiben, Deutsch für die Technische Kommunikation, 2nd ed. 2013, sample with TOC. https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf
- Congree whitepaper on the tekom guideline (vendor, secondary). https://live.tekom.de/fileadmin/user_upload/conference-F21/exhibitors/Congree_Language_Technologies_GmbH/Congree-Whitepaper-Sprachpruefung-tekom-Leitlinie_de.pdf
- DIN 8581-1:2024-05, DIN Media page. https://www.dinmedia.de/de/norm/din-8581-1/377238273
- DIN 8581-1 TOC. https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:377238273/toc-3523268/download
- DIN SPEC 33429:2025-03, DIN Media page. https://dinmedia.de/de/technische-regel/din-spec-33429/387728031
- DIN SPEC 33429 TOC. https://www.din.de/de/wdc-beuth:din21:387728031/toc-3594547/download
- ISO 24495-1:2023. https://iso.org/standard/78907.html
- DIN ISO 24495-1 TOC. https://www.din.de/de/mitwirken/normenausschuesse/nat/veroeffentlichungen/wdc-beuth:din21:370015899/toc-3456451/download
- DIN EN IEC/IEEE 82079-1 listing. https://www.din.de/de/wdc-beuth:din21:309431420
- tekom slides on IEC/IEEE 82079-1 ed. 2. https://www.tekom.de/fileadmin/user_upload/Regionalgruppe_Bodensee/FolSatz-sg-82097-1_ed2-20607-V1-2.pdf
- DIN 5008:2020, DIN Media page. https://www.dinmedia.de/de/norm/din-5008/318422674
- Universität Passau, DIN 5008 summary (secondary). https://www.uni-passau.de/fileadmin/dokumente/beschaeftigte/kommunikation_marketing/webredaktion/DIN_5008.pdf
- Rat für deutsche Rechtschreibung: Amtliches Regelwerk 2024. https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf
- Rat: overview of 2024 changes. https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024_UeberblickAenderungen.pdf
- Rat: rules 2016, edited 2018. https://www.rechtschreibrat.com/DOX/rfdr_Regeln_2016_redigiert_2018.pdf
- Rat: press release 15.12.2023 on gender-fair spelling. https://www.rechtschreibrat.com/DOX/rfdr_PM_2023-12-15_Geschlechtergerechte_Schreibung.pdf
- Schweizerische Bundeskanzlei: Schreibweisungen, 2nd ed. 2013, corr. 2015. https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf
- Bundeskanzlei: Guidelines page. https://www.bk.admin.ch/de/guidelines
- Bundeskanzlei: Rechtschreibleitfaden 2017. https://www.bk.admin.ch/dam/de/sd-web/GApRW2tzdhqZ/rechtschreibleitfaden-2017.pdf
- Bundeskanzlei: Empfehlungen Anglizismen, March 2020. https://www.bk.admin.ch/dam/de/sd-web/74OxqPY0G4gH/empfehlungen-anglizismen-maerz-2020.pdf
- Bundeskanzlei: Leitfaden geschlechtergerechte Sprache, 3rd ed. 2023. https://www.bk.admin.ch/dam/de/sd-web/Ahh8btiPHjjS/leitfaden-geschlechtergerechte-sprache.pdf
- Bundesverwaltungsamt: Bürgernahe Verwaltungssprache (copy). https://www.ruhr-uni-bochum.de/vt/arbeitshandbuchBVamt.doc
- Bavarian regulation citing Handbuch der Rechtsförmlichkeit, 4th ed. https://www.gesetze-bayern.de/Content/Pdf/BayVwV312180-23?all=False
- Höfler 2011, LeGes. https://simon.ifi.uzh.ch/hoefler/hoefler2011leges.pdf
- Austrian Legistisches Handbuch C (snippet only). https://www.eap.steiermark.gv.at/cms/dokumente/11682114_74838392/2e74bd7f/C_Gesamter_Abschnitt.pdf
- Netzwerk Leichte Sprache: Regeln. https://www.netzwerk-leichte-sprache.de/fileadmin/content/documents/regeln/Regelwerk_NLS_web.pdf

### Dictionaries and grammars

- Duden: Perfekt vs. Präteritum. https://www.duden.de/sprachwissen/sprachratgeber/Perfekt-vs-Pr%C3%A4teritum
- Duden: Modalverben. https://duden.de/sprachwissen/sprachratgeber/modalverben
- Duden: Modalpartikeln. https://www.duden.de/sprachwissen/sprachratgeber/Modalpartikeln
- Duden: Anführungszeichen. https://www.duden.de/sprachwissen/rechtschreibregeln/anfuehrungszeichen
- Duden: Sinn. https://www.duden.de/rechtschreibung/Sinn
- Nübling, Konrad-Duden-Preis 2015. https://cdn.duden.de/public_files/2018-11/Konrad-Duden-Preis_N%C3%BCbling_Braucht_man_Sprachgeschichte_2015.pdf
- grammis: Abtönungspartikel (terminology). https://grammis.ids-mannheim.de/terminologie/2
- grammis: Abtönungspartikeln (systematic grammar). https://grammis.ids-mannheim.de/systematische-grammatik/769
- grammis: werden (valency). https://grammis.ids-mannheim.de/verbvalenz/401217
- grammis: Futur. https://grammis.ids-mannheim.de/vggf/2229
- grammis: Modalverb. https://grammis.ids-mannheim.de/vggf/2199
- grammis: In Urlaub oder im Urlaub? https://grammis.ids-mannheim.de/fragen/35
- Linguistik online (Bern), Doppelperfekt und Plusquamperfekt. https://bop.unibe.ch/linguistik-online/article/download/5931/8176
- Lehrndorfer 1996, DDB record. https://www.deutsche-digitale-bibliothek.de/item/DIZBC5PMZABCF3MZ34HPYB5IRQ3E7KDF?lang=en

### Wikipedia project pages

- Wikipedia:Anzeichen für KI-generierte Inhalte. https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte
- Wikipedia:WikiProjekt KI. https://de.wikipedia.org/wiki/Wikipedia:WikiProjekt_KI_und_Wikipedia
- Wikipedia:Signs of AI writing. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Lesbarkeitsindex (article, secondary). https://de.wikipedia.org/wiki/Lesbarkeitsindex
- Hamburger Verständlichkeitskonzept (article, secondary). https://de.wikipedia.org/wiki/Hamburger_Verst%C3%A4ndlichkeitskonzept

### Studies

- Shaitarova, Bauer, Vamvas, Volk: Tracing Linguistic Footprints of ChatGPT Across Tasks, Domains and Personas in English and German. SwissText 2024. https://aclanthology.org/2024.swisstext-1.9.pdf
- Kuhn: A Survey and Classification of Controlled Natural Languages. https://arxiv.org/abs/1507.01701

### Secondary sources (labelled)

- Harbst and Risse 2022, Baker McKenzie (dpa figure). https://www.bakermckenzie.com/-/media/minisites/germany-careers/files/2022/harbst_risse_aufmerksamkeitsspanne_wif1_2022.pdf
- Spektrum (Tagesthemen sentence length). https://www.spektrum.de/news/deutsche-sprache-warum-behoerden-unverstaendlich-schreiben/2254713
- Universität Hohenheim, CEO-Klartext 2025. https://komm.uni-hohenheim.de/uploads/media/CEO-Klartext_2025.pdf
- t3n on the Max Planck "delve" study. https://t3n.de/news/chatgpt-einfluss-sprache-delve-effekt-1693866/
- Vendor blog with German "AI words". https://gpt-watermark-remover.com/de/blog/typische-ki-woerter-vermeiden
