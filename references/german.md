# German mode

Read this file when the text is German. It changes some rules of SKILL.md and adds German tells. Where this file and SKILL.md disagree, this file wins for German text. Sources and open questions are in `german-research.md`.

ASD-STE100 is an English standard. For German, Pass 2 follows the same goals, but it takes its German rules from the tekom guideline "Regelbasiertes Schreiben" (2013) and DIN 8581-1:2024 (Einfache Sprache), as far as their public tables of contents show them.

## What to keep

These features are normal German. Do not remove or "fix" them.

| Keep | Why |
|---|---|
| Subordinate clauses with weil, wenn, dass, damit, obwohl, sodass, der/die/das | They carry the logic. Splitting them makes German sound like a children's book. |
| Perfekt and Präteritum as the writer uses them | Perfekt is normal for results that still hold and in speech. Präteritum is normal in written reports and for sein, haben and modal verbs. Never convert in either direction. |
| Separable verbs (einrichten, anlegen, ausschalten, anfangen) | They are the plain German words. The stiff ones are Fremdwörter like implementieren, initialisieren, evaluieren. |
| Modal particles (doch, ja, eben, halt, mal, schon, wohl) in emails, chats, posts and personal text | They carry the attitude of the writer. "Schick mir mal die Datei" is a request, "Schick mir die Datei" is an order. Cut them only in procedures and reference text. |
| im, am, zum, zur, beim, vom, ins | Standard forms, not contractions. Expanding them can change the meaning. |
| du or Sie, and the gender-fair forms of the source | Keep the register and the writer's system. Do not add, remove or switch gender forms. Use one form per text. |
| Konjunktiv I in reported speech | It marks that someone else said it. |
| German quotation marks „…“ and ‚…‘ | Standard in German prose. Straight quotes only in code, Markdown syntax and UI strings. |
| The Gedankenstrich (en dash with spaces) used now and then, the bis-Strich (9–17 Uhr), the Streckenstrich (Berlin–Hamburg), the Ergänzungsstrich (Ein- und Ausgang) | Correct German typography. |
| Hyphenated compounds (E-Mail-Adresse, 40-Stunden-Woche) | Required by the spelling rules. |
| Spaced abbreviations (z. B., d. h., u. a.) | Correct German form. |
| ß and ss as the source writes them | Do not change the spelling standard. |

## Sentence rhythm

German prose lives on connected sentences: a main clause, a comma, a subordinate clause. Write that way. One sentence may hold a main clause and one or two subordinate clauses when they belong to one thought.

The German problem is not the number of clauses. It is the distance between the two parts of the verb (the Satzklammer). Keep that distance short. If a long block of information sits between "hat" and "behoben", or between "richten" and "ein", move the block behind the verb or into a new sentence.

> Richten Sie, bevor Sie den Server zum ersten Mal mit dem Netzwerk verbinden und die Benutzerkonten anlegen, die Firewall ein.
> → Richten Sie zuerst die Firewall ein, bevor Sie den Server mit dem Netzwerk verbinden und die Benutzerkonten anlegen.

> Beim Export gibt es gerade ein Problem. Sobald es mehr als 10 000 Zeilen sind, schlägt er fehl.
> → Der Export schlägt gerade fehl, sobald es mehr als 10 000 Zeilen sind.

Prose paragraphs average 15 to 20 words per sentence, as in English. Split a sentence when it holds a chain of three or more subordinate clauses, or a clause inside a clause inside a clause. In German, a comma may join two main clauses ("Der Server startet neu, danach ist die Seite wieder erreichbar."). In English, it may not.

## Pass 1 changes

| § | German rule |
|---|---|
| 1 | "nicht nur …, sondern auch" is correct German, but German Wikipedia lists it as an AI tell. Act when it repeats or when the contrast is staged. One real contrast stays. Also watch "Es geht nicht um X. Es geht um Y." and the half form "Das ist nicht nur ärgerlich." without a "sondern": it still stages a contrast, so state the point ("Das ist ärgerlich und …"). |
| 7 | Watch sentences that start with "Darüber hinaus", "Des Weiteren", "Zusätzlich", "Außerdem", "Ferner", "Allerdings". ChatGPT starts German sentences with them much more often than people do. More than one per paragraph is a tell. |
| 8 | Do not ban the Gedankenstrich. Act on density: more than about one pause dash per paragraph is a tell. Replace an em dash (—) with a German en dash or a comma. Never touch ranges, routes, list dashes or hyphens. Do not remove every dash: dash-free text is a newer AI tell. |
| 10 | Drop the English hyphen rule. Instead, fix open compounds from English style: "Software Entwicklung" → "Softwareentwicklung". |
| 15 | German form of the rider: a Partizip I after a comma ("…, die Bedeutung unterstreichend") or ", was … unterstreicht". |
| 20 | German has no title case. Nouns keep their capital, adjectives and verbs in headings do not ("Die Neuen Funktionen" → "Die neuen Funktionen"). |
| 21 | Turn English quotes in German text (“…”, "…" in prose) into „…“. Keep the source's system if it is consistent. |

All other tells (§2 to §6, §9, §11 to §14, §16 to §19, §22 to §26) apply as in SKILL.md. Use the German word lists below.

## German tells

| § | Watch for |
|---|---|
| 3 | im Kern, letztlich geht es um, am Ende des Tages |
| 4 | Tauchen wir ein, Lass uns eintauchen, Hier ist, was du wissen musst |
| 9 | könnte möglicherweise, kann unter Umständen eventuell, potenziell möglicherweise |
| 12 | nahtlos, maßgeschneidert, ganzheitlich, essenziell, vielfältig, umfassend, innovativ (weak alone) |
| 13 | spielt eine wichtige / zentrale / entscheidende Rolle, Meilenstein, Wendepunkt, Schlüsselmoment, unterstreicht die Bedeutung, tief verwurzelt, ein Zeugnis für |
| 16 | atemberaubend, im Herzen von, eingebettet in, reiches kulturelles Erbe, unbedingt besuchen |
| 17 | Experten sind sich einig, Branchenberichte, Beobachter, Einige Kritiker argumentieren |
| 18 | dient als, fungiert als, stellt … dar, verfügt über, bietet (where "ist" or "hat" fits) |
| 22 | Natürlich!, Sicherlich!, Gerne!, Gute Frage!, Ich hoffe, das hilft, Lass mich wissen, Möchtest du, dass ich …, Ich hoffe, diese Nachricht erreicht Sie wohlauf |
| 23 | Bis zu meinem letzten Update, Stand meines letzten Wissensupdates, basierend auf verfügbaren Informationen, Obwohl spezifische Details begrenzt sind |
| 25 | In diesem Artikel werden wir …, Die folgende Tabelle zeigt …, a closing "Fazit" or "Herausforderungen" section, Zusammenfassend lässt sich sagen, Abschließend |
| new | English calques: "macht Sinn" (→ ist sinnvoll, ergibt Sinn), "am Ende des Tages" (→ letztlich), "der Elefant im Raum", "realisieren" for "merken", "in 2024" (→ 2024, im Jahr 2024) |
| new | False ranges: "von Start-ups bis zu Konzernen" for members of a set |
| new | Uniform text: steady sentence length, few commas, the same connectors |

## Pass 2 changes

| S | German rule |
|---|---|
| 1 | Keep a subordinate clause that carries the reason, condition or result. Split chains of subordinate clauses and nested clauses. |
| 2 | Same limits. A Paarform ("Nutzerinnen und Nutzer"), a number with its unit and "z. B." count as one word. A compound counts as one word. |
| 6 | Name the actor when it matters: "Die Daten werden vom Server geprüft" → "Der Server prüft die Daten". "man", the Zustandspassiv ("Die Datei ist gespeichert") and a passive with an unknown actor are fine. Avoid "ist zu prüfen" and "Es wird empfohlen, …" when the reader is the actor. |
| 7 | Allowed: Präsens, Präteritum, Perfekt, Futur I. Avoid Plusquamperfekt chains and Futur II. Präsens in instructions. |
| 8 | German Nominalstil: "Die Durchführung der Migration erfolgt am Freitag" → "Wir migrieren die Daten am Freitag". Replace empty Funktionsverbgefüge: zur Anwendung kommen, zum Einsatz kommen, Verwendung finden, Berücksichtigung finden, eine Entscheidung treffen, in Erwägung ziehen. Keep the ones with their own meaning: in Kraft treten, zur Verfügung stellen, in Betrieb nehmen. |
| 9 | Keep the source's modal verb. "muss nicht" means "not required", "darf nicht" means "forbidden". Never swap one for the other. "werden" can mean future, passive or a guess ("Sie wird jetzt zu Hause sein"). Keep "sollte" for advice. |
| 10 | Prefer the German word to a Fremdwort or a new anglicism with the same meaning: verwenden (not utilisieren), absagen (not canceln), Sitzung (not Meeting), erzeugen (not generieren). Keep technical terms that experts use (Deployment, Cache, Commit). Drop the phrasal-verb rule. |
| 11 | One term per thing. Also one gender-fair form and one order of a Paarform per text. |
| 12 | Replace the noun-stack rule. At most two genitives in a row ("die Prüfung der Einhaltung der Vorgaben des Datenschutzes" → "prüfen, ob die Datenschutzvorgaben eingehalten werden"). Give a long compound a hyphen for clarity (Datenbank-Verbindungsfehler). Do not split compounds into word groups. |
| 15 | Semicolons: avoid, as in English. Strict mode: no spoken forms with an apostrophe (gibt's, geht's) and "zum Beispiel" for "z. B.". Never expand im, zum, beim. |

S3 to S5, S11, S13 and S14 apply as in SKILL.md. Strict mode: "can, must, will" become "können, müssen, werden", but check the negation and the meaning of "werden" every time.

## Examples

> Wir behoben den Fehler im Login. Er tritt nicht mehr auf.
> → Wir haben den Fehler im Login behoben, er tritt nicht mehr auf.

> Implementieren Sie die Konfiguration gemäß der Dokumentation.
> → Richten Sie die Konfiguration so ein, wie es die Anleitung beschreibt.

> Darüber hinaus unterstützt das Tool CSV-Dateien. Zusätzlich bietet es eine API. Des Weiteren ist es nicht nur schnell, sondern auch sicher.
> → Das Tool liest CSV-Dateien und hat eine API, mit der Sie die Daten auch automatisch abrufen können.

(The last example drops "schnell" and "sicher" only because the source gives no facts for them. Keep both if the source gives facts.)

> Kannst du mir mal kurz die Datei schicken?
> → Keep as is in a chat or an email.

## Checker

`python scripts/ste_check.py --lang de FILE` uses German word counting, German abbreviations, the German tells above and German typography. `--lang auto` (the default) picks German when German function words dominate.
