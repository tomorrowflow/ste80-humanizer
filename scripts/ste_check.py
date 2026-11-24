#!/usr/bin/env python3
"""ste_check: a small heuristic linter for AI tells and STE-style (ASD-STE100-inspired) English and German.

Part of the ste80-humanizer skill. It finds places to look at.
It does not prove compliance with ASD-STE100 and it is not an AI detector.
No dependencies. Python 3.8+.

Usage:
    python ste_check.py FILE [FILE ...]
    python ste_check.py --strict FILE
    python ste_check.py --lang de FILE      (default: --lang auto)
    python ste_check.py --voice ~/.claude/voice/de.md FILE   (default: --voice auto)
    cat draft.txt | python ste_check.py -
    python ste_check.py --json FILE

Exit code: 0 if no findings, 1 if findings, 2 on usage error.
"""

from __future__ import annotations

import argparse
import os
import json
import re
import sys
from dataclasses import dataclass, asdict

# --- Word lists (short, paraphrased working lists; not the ASD dictionary) ---

SWAPS = {
    "utilize": "use", "utilise": "use", "leverage": "use", "employ": "use",
    "perform": "do", "conduct": "do", "accomplish": "do", "facilitate": "help, let",
    "ensure": "make sure", "verify": "make sure", "commence": "start",
    "initiate": "start", "terminate": "stop", "eliminate": "remove",
    "modify": "change", "indicate": "show", "demonstrate": "show",
    "obtain": "get", "acquire": "get", "provide": "give", "assist": "help",
    "attempt": "try", "retain": "keep", "observe": "monitor, see",
    "locate": "find", "determine": "find", "subsequently": "then",
    "however": "but", "therefore": "thus, as a result", "hence": "thus",
    "furthermore": "also", "moreover": "also", "additionally": "also",
    "whereas": "but", "via": "through", "whether": "if",
    "numerous": "many", "adequate": "sufficient", "identical": "same",
    "simultaneously": "at the same time", "prior to": "before",
    "due to": "because of", "in order to": "to", "in the event that": "if",
    "it is important to note": "(delete)", "it's important to note": "(delete)",
    "it should be noted": "(delete)",
    "delve": "examine", "robust": "strong, reliable", "seamless": "(delete)",
    "seamlessly": "(delete)", "comprehensive": "full", "crucial": "important",
    "pivotal": "important", "landscape": "field, area", "realm": "field, area",
    "showcase": "show", "streamline": "simplify", "empower": "let, help",
    "harness": "use", "foster": "help", "underscore": "show",
    "game-changer": "(delete)", "tapestry": "(delete)", "testament": "(delete) or say what it shows",
    "elevate": "improve", "unlock": "let, give", "intricate": "complex", "meticulous": "careful",
    "vibrant": "(delete)", "enhance": "improve", "groundbreaking": "(fact or delete)",
    "cutting-edge": "(fact or delete)", "world-class": "(fact or delete)", "best-in-class": "(fact or delete)",
    "renowned": "(fact or delete)", "stunning": "(delete)", "breathtaking": "(delete)",
    "serves as": "is", "stands as": "is", "boasts": "has",
}

STRICT_ONLY_SWAPS = {
    "need": "necessary (adj)", "may": "can", "might": "can", "could": "can",
    "should": "must", "shall": "must", "would": "will", "since": "because",
    "both": "the two", "further": "more", "additional": "more",
    "acceptable": "permitted", "main": "primary", "portion": "part",
    "required": "necessary", "insert": "put", "rotate": "turn",
    "avoid": "prevent", "follow": "obey", "inspect": "examine",
    "e.g.": "for example", "i.e.": "that is", "etc.": "and other",
}

TELLS = [
    (r"\b(?:it'?s|it is|this is|that'?s|is)\s+not\s+(?:just|only|merely|simply|about)\b", "not-x-but-y", "'not just X, but Y' framing: state the point"),
    (r"\bnot\s+(?:just|only|merely)\b[^.]{0,80}\bbut\b", "not-x-but-y", "'not just X but Y' framing: state the point"),
    (r"\bisn'?t\s+(?:just\s+)?about\b", "not-x-but-y", "'this isn't about X' framing: state the point"),
    (r"^(?:great question|certainly|of course|sure|absolutely)[!,.]", "chatbot", "chatbot opener: delete"),
    (r"\bi hope this helps\b|\blet me know if\b|\bwould you like me to\b|\bfeel free to\b|\bhappy to help\b", "chatbot", "chatbot closer: delete"),
    (r"\blet'?s (?:dive|delve|break (?:this|it) down|explore|unpack)\b|\bhere'?s the thing\b|\bwithout further ado\b", "run-up", "run-up before the point: start with the point"),
    (r"\bat its core\b|\bthe real question is\b|\bfundamentally\b|\bat the end of the day\b", "fake-depth", "fake depth: say the plain claim"),
    (r"\blet that sink in\b|\band that changes everything\b|\bthat'?s the real (?:win|story)\b|\bread that again\b", "closer", "dramatic closer: delete"),
    (r"\bdon'?t get me wrong\b|\bto be clear\b|\bone might be tempted\b", "strawman", "arguing with nobody: remove"),
    (r"\bas of my (?:last|latest) (?:update|training)\b|\bbased on (?:the )?available information\b", "knowledge-hedge", "knowledge-limit hedge: delete"),
    (r"\bin this (?:guide|article|section|post),? (?:we|i)(?:'ll| will)\b", "meta", "writing about the text: give the content"),
    (r"\b(?:could|may|might) (?:potentially|possibly|arguably)\b", "stacked-hedge", "stacked hedge: keep one hedge"),
    (r"\b(?:experts|studies|many people|observers) (?:say|agree|show|believe|suggest)\b", "vague-authority", "vague authority: name the source or delete"),
    (r",\s+(?:highlighting|underscoring|emphasizing|ensuring|reflecting|showcasing|fostering|cultivating|contributing to)\b", "ing-rider", "shallow '-ing' rider: delete or make it a sentence"),
    (r"\b(?:plays|play|played) a (?:pivotal|crucial|key|vital) role\b|\bmarks? a (?:significant|major) milestone\b|\bthe future looks bright\b", "inflation", "inflated significance: say what happened"),
    (r"\b(?:is|are|was|were) associated with\b|\b(?:in connection with|linked to|tied to)\b", "vague-association", "vague connection: name the relation (founded, caused, part of)"),
    (r"\b(?:is|are|was|were|be)(?:\s+\w+ly)?\s+(?:high-quality|well-known|well-documented|long-term|real-time|well-tested|client-facing)\b", "hyphen-pair", "drop the hyphen after the noun ('is well documented')"),
    (r"^(?:that'?s|this is) (?:the real|why it|what) ", "closer", "possible one-line closer: cut it if it repeats the point"),
    (r"\b(?:the\s+)?(?:numbers|data|figures|results)\s+speak\s+for\s+themselves\b", "closer", "'the numbers speak for themselves': give the number (§2)"),
    (r"(?:^|[.!?]\s+)(?:key\s+(?:point|takeaway)s?|bottom\s+line|tl;dr|the\s+short\s+(?:version|answer))\s*:|\bthe\s+(?:key|real|main)\s+point\s+(?:is|here)\b", "meta-label", "label before the point: delete the label (§4)"),
    (r"\b(?:decide\w*|check\w*|review\w*|assess\w*|determin\w*)\b[^.!?]{0,40}\bwhether\b[^.!?]{3,80}\bor\b", "both-branches", "both outcomes of a decision: name the action (weak alone, §6)"),
    (r"\bwhether\b[^.!?]{0,80}\bor\s+not\b|\bwith\s+or\s+without\b|\bregardless\s+of\s+whether\b", "both-branches", "'whether or not', 'with or without': the reader assumes both cases (weak alone, §6)"),
    (r"\b(?:document|description|spec|specification|policy|report|list|table)s?\s+(?:is|are|remains?|stays?)\s+(?:silent|vague|quiet)\b|\b(?:the\s+)?(?:data|numbers|figures)\s+(?:tells?|reveals?)\b", "personified-doc", "document as a speaker: write 'does not cover' (keep legal 'the contract is silent on', §18)"),
    (r"\b(?:each|per|every|this|that)\s+(?:row|column|line\s+item|cell)\b", "structure-noun", "'each row', 'this column': name the thing, unless the reader has the table (§25)"),
    (r"\b(?:a\s+(?:quarter|third|fifth|tenth)|half|most)\s+of\s+the\s+(?:list|table|rows|entries|items)\b", "structure-noun", "share of a list: give the count and name the things (§25)"),
]

PHRASAL = [
    "set up", "find out", "look into", "look at", "fill in", "fill out",
    "turn on", "turn off", "switch on", "switch off", "go through",
    "point out", "put together", "take out", "come up with", "give up",
    "carry out", "figure out", "check out", "back up", "shut down",
]

ING_NOUN_OK = {
    "during", "following", "opening", "remaining", "according", "something",
    "nothing", "anything", "everything", "thing", "things", "string", "strings",
    "bring", "ring", "spring", "king", "wing", "sing", "single", "logging",
    "caching", "routing", "testing", "debugging", "networking", "staging",
    "setting", "settings", "mapping", "warning", "warnings", "building",
    "meaning", "morning", "evening", "ceiling", "padding", "spacing",
    "rendering", "hosting", "tooling", "training", "pricing", "billing",
    "encoding", "streaming", "scheduling", "parsing", "linting", "formatting",
    "being", "missing", "existing", "incoming", "outgoing", "pending",
}

NOT_PARTICIPLE = {
    "different", "present", "absent", "current", "recent", "frequent", "silent",
    "independent", "efficient", "sufficient", "apparent", "consistent", "important",
    "relevant", "urgent", "evident", "excellent", "competent", "dependent", "transparent",
    "open", "even", "often", "golden", "hidden", "sudden", "wooden", "own", "down",
    "shown", "known", "unknown", "brown", "grown", "drawn", "built", "content",
    "intent", "event", "agent", "client", "point", "front", "want", "difficult",
    "permanent", "prominent", "convenient", "fluent", "patient", "resilient", "redundant",
}

AUX = r"(?:am|is|are|was|were|be|been|being)"
PASSIVE_RE = re.compile(rf"\b{AUX}\s+(?:\w+ly\s+)?(\w+(?:ed|en|wn|lt|nt|pt|ung|ade|one|ept|ought))\b", re.I)
PERFECT_RE = re.compile(r"\b(?:has|have|had)\s+(?:not\s+)?(?:been|\w+ed|\w+en|done|made|gone|seen|run|set|put)\b", re.I)
PROGRESSIVE_RE = re.compile(rf"\b{AUX}\s+(?:not\s+)?(\w+ing)\b", re.I)
MODAL_PASSIVE_RE = re.compile(r"\b(?:can|could|may|might|must|should|shall|will|would)\s+(?:not\s+)?be\s+\w+(?:ed|en)\b", re.I)
CONTRACTION_RE = re.compile(r"\b\w+(?:n't|'re|'ve|'ll|'d|'m)\b|\b(?:it|that|there|what|here)'s\b", re.I)
# Unicode letters, so that "Größe" and "Übersicht" count as one word each.
WORD_RE = re.compile(r"[^\W\d_][\w'’\-]*|\d[\w.,:/%-]*")

# --- Language detection ---

DE_FUNCTION = {
    "der", "die", "das", "und", "ist", "nicht", "mit", "für", "auf", "ein", "eine", "zu",
    "von", "sie", "wir", "ich", "es", "den", "dem", "sich", "auch", "wird", "werden",
    "bei", "oder", "dass", "wenn", "aber", "noch", "nur", "sind", "hat", "haben",
}
EN_FUNCTION = {
    "the", "and", "is", "of", "to", "a", "that", "it", "for", "with", "on", "are",
    "this", "be", "you", "not", "or", "if", "but", "was", "has", "have", "will", "can",
}


def detect_language(text: str) -> str:
    words = [w.lower() for w in WORD_RE.findall(text)]
    de = sum(w in DE_FUNCTION for w in words)
    en = sum(w in EN_FUNCTION for w in words)
    return "de" if de > en else "en"


# --- German lists (see references/german.md) ---

ABBR_DE = [
    "z. B.", "z.B.", "d. h.", "d.h.", "u. a.", "u.a.", "u. Ä.", "o. Ä.", "u. U.", "i. d. R.",
    "z. T.", "m. E.", "bzw.", "vgl.", "ca.", "usw.", "etc.", "ggf.", "evtl.", "inkl.", "exkl.",
    "sog.", "bspw.", "zzgl.", "Nr.", "S.", "Kap.", "Abs.", "Art.", "Ziff.", "Bd.", "Hrsg.",
    "Abb.", "Tab.", "Tel.", "Dr.", "Prof.", "St.", "Mio.", "Mrd.", "Std.", "Min.", "Jh.",
]
ABBR_DE_RE = re.compile(
    r"(?<![\w.])(?:" + "|".join(re.escape(a) for a in sorted(ABBR_DE, key=len, reverse=True)) + r")"
)
MONTHS_DE = r"Januar|Jänner|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember"
ORDINAL_DE_RE = re.compile(
    rf"\b(\d{{1,2}})\.(?=\s+(?:{MONTHS_DE}|Jahrhunderts?|Kapitel|Auflage|Mal|Platz|Stock|Klasse|Quartals?|[a-zäöü]))"
)

SWAPS_DE = {
    "utilisieren": "verwenden", "canceln": "absagen", "gecancelt": "abgesagt",
    "generieren": "erzeugen", "zeitnah": "a date, or 'bald'", "nahtlos": "(delete)",
    "maßgeschneidert": "(fact or delete)", "ganzheitlich": "(fact or delete)",
    "essenziell": "wichtig, nötig", "mehrwert": "say what it brings",
    "atemberaubend": "(delete)", "bahnbrechend": "(fact or delete)",
    "zur anwendung kommen": "angewendet werden, or a verb", "zum einsatz kommen": "eingesetzt werden, or a verb",
    "verwendung finden": "verwendet werden", "berücksichtigung finden": "berücksichtigt werden",
    "eine entscheidung treffen": "entscheiden", "in erwägung ziehen": "erwägen, prüfen",
    "unter beweis stellen": "zeigen, beweisen", "zur durchführung bringen": "durchführen",
}

TELLS_DE = [
    (r"\bnicht\s+nur\b[^.!?]{0,120}\bsondern\b", "not-x-but-y", "'nicht nur …, sondern auch': keep only a real contrast (§1)"),
    (r"\b(?:ist|sind|war|waren)\s+(?:das\s+|es\s+)?nicht\s+nur\s+\w+[.!]", "not-x-but-y", "'Das ist nicht nur X.': staged contrast, state the point (§1)"),
    (r"\bes\s+geht\s+nicht\s+(?:nur\s+)?(?:um|darum)\b", "not-x-but-y", "'es geht nicht um X': state the point (§1)"),
    (r"\b(?:im\s+kern|letztlich\s+geht\s+es\s+um)\b", "fake-depth", "fake depth: say the plain claim (§3)"),
    (r"\b(?:tauchen\s+wir\s+ein|lass(?:t)?\s+uns\s+(?:eintauchen|einen\s+blick\s+werfen)|hier\s+ist,?\s+was\s+(?:du|sie)\s+wissen\s+m)", "run-up", "run-up before the point: start with the point (§4)"),
    (r"\b(?:könnte|kann|dürfte)\s+(?:möglicherweise|eventuell|potenziell|unter\s+umständen)\b", "stacked-hedge", "stacked hedge: keep one hedge (§9)"),
    (r"\bspielt\s+eine\s+(?:zentrale|wichtige|entscheidende|bedeutende|wesentliche|maßgebliche|schlüssel)\s*-?\s*rolle\b", "inflation", "inflated significance: say what it does (§13)"),
    (r"\b(?:meilenstein|wendepunkt|schlüsselmoment|vermächtnis|tief\s+verwurzelt)\b", "inflation", "inflated significance (weak alone, §13)"),
    (r"\bunterstreicht\s+(?:die|seine|ihre|deren|dessen)\s+bedeutung\b|\bein\s+zeugnis\s+(?:für|von)\b", "inflation", "inflated significance: keep the fact (§13)"),
    (r",\s+(?:\w+\s+){0,4}(?:unterstreichend|gewährleistend|hervorhebend|betonend|widerspiegelnd)\b", "ing-rider", "Partizip-I rider: delete or make it a sentence (§15)"),
    (r"\bim\s+herzen\s+(?:von|der|des)\b|\beingebettet\s+in\b|\breiche[sn]?\s+kulturelle[sn]?\s+erbe\b", "sales", "sales language: say what it is (§16)"),
    (r"\b(?:experten|studien|beobachter|kritiker|branchenberichte)\s+(?:sagen|zeigen|sind\s+sich\s+einig|argumentieren|betonen)\b", "vague-authority", "vague authority: name the source or delete (§17)"),
    (r"\b(?:dient|dienen|fungiert|fungieren)\s+als\b", "is-avoidance", "'dient als': use 'ist' (weak alone, §18)"),
    (r"^(?:natürlich|sicherlich|gerne|gern|gute\s+frage|super\s+frage)[!,.]", "chatbot", "chatbot opener: delete (§22)"),
    (r"\bich\s+hoffe,?\s+(?:das|dies)\s+hilft\b|\blass(?:en\s+sie|t)?\s+(?:mich|uns)\s+wissen\b|\bmöchte(?:st|n)\s+(?:du|sie),?\s+dass\s+ich\b|\bdiese\s+nachricht\s+erreicht\s+(?:sie|dich|euch)\b", "chatbot", "chatbot residue: delete (§22)"),
    (r"\b(?:bis\s+zu\s+meinem|stand\s+meines)\s+letzten\s+(?:wissens)?updates?\b|\bbasierend\s+auf\s+(?:den\s+)?verfügbaren\s+informationen\b", "knowledge-hedge", "knowledge-limit hedge: delete (§23)"),
    (r"\bin\s+diesem\s+(?:artikel|beitrag|abschnitt|leitfaden)\s+(?:werden\s+wir|erfahren\s+sie|zeigen\s+wir)\b|\bdie\s+folgende\s+tabelle\s+zeigt\b", "meta", "writing about the text: give the content (§25)"),
    (r"^(?:zusammenfassend|abschließend|abschliessend|fazit)\b", "closer", "summary closer: cut it if it repeats (§25)"),
    (r"\bmacht\s+(?:es\s+|das\s+)?(?:keinen\s+|wenig\s+|viel\s+|absolut\s+)?sinn\b|\bam\s+ende\s+des\s+tages\b|\belefant\s+im\s+raum\b|\bin\s+(?:19|20)\d\d\b", "calque", "English calque: use the German phrase"),
    (r"\bes\s+wird\s+empfohlen\b|\b(?:ist|sind)\s+(?:\S+\s+){0,6}?zu\s+(?:prüfen|beachten|berücksichtigen|melden|erledigen)\b", "hidden-actor", "hidden actor: say who does it (S6)"),
    (r"\b(?:wird|werden|wurde|wurden)\b[^.!?]{0,60}?\b(?:von|vom)\s+(?:de[mnr]|einem|einer|ihr|ihm|uns|\w+)\b[^!?]{0,40}?\b(?:\w*ge\w+(?:t|en)|\w+iert)\b", "passive", "passive with an actor: make the actor the subject (S6)"),
    (r"\b(?:des|der)\s+\w+(?:\s+\w+)?\s+(?:des|der)\s+\w+(?:\s+\w+)?\s+(?:des|der)\s+\w+", "genitive-chain", "possible genitive chain: at most two in a row (S12)"),
    (r"\b(?:kein(?:e[mnrs]?)?)\s+[^,.!?]{1,40},\s*sondern\b", "not-x-but-y", "'kein X, sondern Y': keep only a real contrast (weak alone, §1)"),
    (r"\b(?:das|dies)\s+(?:heißt|heisst|bedeutet)\s+(?:aber\s+)?nicht,?\s+dass\b", "not-x-but-y", "'Das heißt nicht, dass …': state the point (§1)"),
    (r"\b(?:zahlen|fakten|daten|ergebnisse)\s+sprechen\s+(?:eine\s+\w+\s+sprache|für\s+sich)\b", "closer", "'Die Zahlen sprechen für sich': give the number (§2)"),
    (r"(?:^|[.!?]\s+)(?:kernpunkt|kernaussage|kernfrage|kurz\s+gesagt|kurzum|unterm\s+strich|kurzfassung|das\s+entscheidende)\s*:|\bder\s+(?:springende|entscheidende|eigentliche)\s+punkt\s+(?:ist|hier)\b", "meta-label", "label before the point: delete the label, keep the sentence (§4)"),
    (r"\b(?:entscheid\w*|prüf\w*|klär\w*|bewert\w*|festleg\w*|beurteil\w*)\b[^.!?]{0,40}\bob\b[^.!?]{3,80}\boder\b", "both-branches", "both outcomes of a decision: name the action ('prüft jede Antwort') unless each needs its own step (weak alone, §6)"),
    (r"\bob\b[^.!?]{1,80}\boder\s+nicht\b|\bmit\s+oder\s+ohne\b|\bunabhängig\s+davon,?\s+ob\b", "both-branches", "'ob … oder nicht', 'mit oder ohne': the reader assumes both cases (weak alone, §6)"),
    (r"\b(?:dokument|vertrag|angebot|beschreibung|description|spezifikation|richtlinie|policy|tabelle|liste|bericht|studie|analyse|daten|zahlen|quelle|unterlage|sla|agb)\w*\s+(?:schweig\w*|verrät|verraten|verschweig\w*|erzählt|erzählen|bleib\w*\s+(?:vage|stumm|still))\b", "personified-doc", "document as a person: write 'regelt nicht', 'enthält keine Regelung zu' (§18)"),
    (r"\bbleib\w*\s+(?:[\wäöüß]+\s+){1,4}ohne\s+\w+", "personified-doc", "'X bleibt ohne Y': write 'für X fehlt Y' and name the thing (weak alone, §18)"),
    (r"\b(?:je|pro|für\s+jede[nrs]?|in\s+jede[rm])\s+(?:zeile|spalte|zelle|position|eintrag|feld|posten)\b", "structure-noun", "'je Zeile', 'pro Eintrag': name the thing, unless the reader has the table (§25)"),
    (r"\b(?:ein(?:e[mnr]?)?\s+(?:viertel|drittel|fünftel|zehntel|großteil|grossteil)|die\s+hälfte|der\s+(?:groß|gross)teil)\s+(?:der|des)\s+(?:liste|tabelle|punkte|positionen|einträge|zeilen)\b", "structure-noun", "share of a list: give the count and name the things (§25)"),
]

CONNECTIVES_DE = re.compile(r"^(?:Darüber hinaus|Des Weiteren|Zusätzlich|Außerdem|Ausserdem|Ferner|Allerdings|Andererseits)\b")
PAUSE_DASH_DE = re.compile(r"(?<=[^\s\d])\s–\s(?=[^\d])")
LONG_COMPOUND_DE = re.compile(r"\b[A-ZÄÖÜ][a-zäöüß]{20,}\b")
DE_IMPERATIVE_RE = re.compile(r"^(?:(?:Wenn|Falls|Bevor|Nachdem|Sobald)\b[^,]*,\s*)?[A-ZÄÖÜ]\w*en\s+Sie\b")


@dataclass
class Finding:
    line: int
    rule: str
    message: str
    excerpt: str


def strip_markdown(text: str) -> list[tuple[int, str]]:
    """Return (line_no, line) for prose lines. Drop code blocks, tables, front matter."""
    out = []
    in_code = False
    in_front = False
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if i == 1 and line.strip() == "---":
            in_front = True
            continue
        if in_front:
            if line.strip() == "---":
                in_front = False
            continue
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        if in_code or line.lstrip().startswith("|") or line.startswith("    "):
            out.append((i, ""))
            continue
        line = re.sub(r"`[^`]*`", "CODE", line)            # inline code = 1 word
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)  # links
        line = re.sub(r"https?://\S+", "URL", line)
        if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", line):
            out.append((i, ""))                               # each list item = own paragraph
            line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        line = re.sub(r"^\s*>\s?", "", line)                   # quotes
        line = re.sub(r"^#+\s+", "", line)                     # headings
        line = re.sub(r"\*\*|__|\*|_", "", line)
        out.append((i, line))
    return out


def paragraphs(lines: list[tuple[int, str]]) -> list[tuple[int, str]]:
    paras, buf, start = [], [], None
    for no, line in lines:
        if line.strip():
            if start is None:
                start = no
            buf.append(line.strip())
        elif buf:
            paras.append((start, " ".join(buf)))
            buf, start = [], None
    if buf:
        paras.append((start, " ".join(buf)))
    return paras


HOLD = "\x00"  # stands in for a period that does not end a sentence


def sentences(paragraph: str, lang: str = "en") -> list[str]:
    protected = re.sub(r"\b(e\.g|i\.e|etc|vs|Dr|Mr|Ms|No)\.", lambda m: m.group(0).replace(".", HOLD), paragraph)
    if lang == "de":
        protected = ABBR_DE_RE.sub(lambda m: m.group(0).replace(".", HOLD), protected)
        protected = ORDINAL_DE_RE.sub(lambda m: m.group(1) + HOLD, protected)
    parts = re.split(r"(?<=[.!?:])\s+(?=[A-ZÄÖÜ0-9\"'(„«‚»])", protected)
    return [p.replace(HOLD, ".").strip() for p in parts if p.strip()]


def count_words(sentence: str, lang: str = "en") -> int:
    s = re.sub(r"\([^)]*\)", " PAREN ", sentence)         # parentheses = 1 word
    s = re.sub(r"\"[^\"]*\"|“[^”]*”|„[^“”]*[“”]|«[^»]*»", " QUOTE ", s)  # quoted text = 1 word
    if lang == "de":
        s = ABBR_DE_RE.sub(" ABBR ", s)                      # "z. B." = 1 word
        s = re.sub(r"\b\d{1,3}(?:[  .]\d{3})+(?:,\d+)?\b", "NUM", s)  # "1 000" = 1 word
        s = re.sub(r"\b(\w+innen) und (\w+)\b", r"\1", s)     # Paarform = 1 word
    s = re.sub(r"\b(\d[\d.,]*)\s*(%|ms|s|kb|mb|gb|tb|px|kg|g|m|cm|mm|km|h|min)\b", r"\1", s, flags=re.I)
    return len(WORD_RE.findall(s))


def is_imperative(sentence: str) -> bool:
    first = (WORD_RE.findall(sentence) or [""])[0].lower()
    return first in {
        "add", "apply", "attach", "click", "close", "configure", "connect", "copy",
        "create", "delete", "disconnect", "do", "download", "edit", "enter", "examine",
        "find", "get", "give", "install", "keep", "let", "make", "measure", "monitor",
        "move", "open", "push", "pull", "put", "read", "remove", "replace", "restart",
        "run", "select", "send", "set", "start", "stop", "turn", "type", "update",
        "upload", "use", "write", "if", "when", "before", "after", "to",
    }


def sentence_limit(sentence: str, lang: str, strict: bool) -> tuple[int, str]:
    """Return (word limit, kind). 80% mode allows longer descriptions joined by commas."""
    instruction = DE_IMPERATIVE_RE.match(sentence) if lang == "de" else is_imperative(sentence)
    if instruction:
        return (20 if strict else 23), "instruction"
    return (25 if strict else 35), "description"


def check(text: str, strict: bool, lang: str = "en", voice: dict | None = None) -> list[Finding]:
    """Without a voice profile: the general rules. With one: the writer's own phrases, words and
    dashes are not tells, and rhythm is measured against the profile."""
    if not voice:
        return check_general(text, strict, lang)
    lines = strip_markdown(text)
    raw_by_no = dict(enumerate(text.splitlines(), 1))
    general = check_general(mask_kept(text, voice), strict, lang)
    own_rules = {"dash"} | ({"rhythm"} if voice.get("sentence_avg") else set())
    kept = [x for x in general if x.rule not in own_rules]
    return sorted(kept + voice_findings(text, lines, raw_by_no, lang, voice), key=lambda x: (x.line, x.rule))


def check_general(text: str, strict: bool, lang: str = "en") -> list[Finding]:
    f: list[Finding] = []
    lines = strip_markdown(text)
    raw_by_no = dict(enumerate(text.splitlines(), 1))

    for start, para in paragraphs(lines):
        sents = sentences(para, lang)
        if len(sents) > 6:
            f.append(Finding(start, "paragraph-length", f"{len(sents)} sentences in one paragraph (max 6)", para[:80]))
        for s in sents:
            n = count_words(s, lang)
            limit, kind = sentence_limit(s, lang, strict)
            if n > limit:
                f.append(Finding(start, "sentence-length", f"{n} words ({kind} max {limit})", s[:100]))
        if lang == "de":
            openers = sum(bool(CONNECTIVES_DE.match(s)) for s in sents)
            if openers >= 2:
                f.append(Finding(start, "connective", f"{openers} sentences start with 'Darüber hinaus', 'Zusätzlich' or similar (§7)", para[:80]))
            dashes = len(PAUSE_DASH_DE.findall(para))
            if dashes >= 2:
                f.append(Finding(start, "dash", f"{dashes} Gedankenstriche in one paragraph: keep one at most (§8)", para[:80]))

    if not strict:
        f.extend(check_rhythm(lines, raw_by_no, lang))

    if lang == "de":
        return drop_if_table(text, sorted(f + check_lines_de(lines, raw_by_no, strict), key=lambda x: (x.line, x.rule)))

    for no, line in lines:
        if not line.strip():
            continue
        low = line.lower()
        if ";" in line:
            f.append(Finding(no, "semicolon", "semicolon: write two sentences or a list", line.strip()[:100]))
        if "—" in line or " -- " in line or " – " in line:
            f.append(Finding(no, "dash", "dash as sentence glue: use a period, comma or colon", line.strip()[:100]))
        for m in PASSIVE_RE.finditer(line):
            if m.group(1).lower() in NOT_PARTICIPLE:
                continue
            f.append(Finding(no, "passive", f"possible passive voice: '{m.group(0)}'", line.strip()[:100]))
        for m in MODAL_PASSIVE_RE.finditer(line):
            f.append(Finding(no, "modal-passive", f"modal + passive: '{m.group(0)}'", line.strip()[:100]))
        for m in PERFECT_RE.finditer(line):
            f.append(Finding(no, "perfect-tense", f"perfect tense: '{m.group(0)}'", line.strip()[:100]))
        for m in PROGRESSIVE_RE.finditer(line):
            if m.group(1).lower() not in ING_NOUN_OK:
                f.append(Finding(no, "progressive", f"progressive tense: '{m.group(0)}'", line.strip()[:100]))
        for m in re.finditer(r"(?:^|[.,;:]\s+|\b(?:by|while|when|after|before)\s+)(\w+ing)\b", line, re.I):
            w = m.group(1).lower()
            if w not in ING_NOUN_OK and len(w) > 4:
                f.append(Finding(no, "ing-form", f"'-ing' verb form: '{m.group(1)}'", line.strip()[:100]))
        for p in PHRASAL:
            if re.search(rf"\b{re.escape(p)}\b", low):
                f.append(Finding(no, "phrasal-verb", f"phrasal verb '{p}'", line.strip()[:100]))
        for pat, rule, msg in TELLS:
            if re.search(pat, line, re.I):
                f.append(Finding(no, rule, msg, line.strip()[:100]))
        if re.search(r"[“”‘’]", raw_by_no.get(no, "")):
            f.append(Finding(no, "curly-quotes", "curly quotes: use straight quotes in Markdown and code", line.strip()[:100]))
        swaps = dict(SWAPS)
        if strict:
            swaps.update(STRICT_ONLY_SWAPS)
            if CONTRACTION_RE.search(line):
                f.append(Finding(no, "contraction", "contraction (not permitted in strict mode)", line.strip()[:100]))
            if re.search(r"\b(?:check|test)(?:s|ed)?\s+(?:the|a|an|that|if|your|all)\b", low):
                f.append(Finding(no, "noun-only", "'check'/'test' used as a verb (STE: noun only)", line.strip()[:100]))
        for word, alt in swaps.items():
            if re.search(rf"(?<![\w-]){re.escape(word)}(?![\w-])", low):
                f.append(Finding(no, "word", f"'{word}' -> {alt}", line.strip()[:100]))
    f.sort(key=lambda x: (x.line, x.rule))
    return drop_if_table(text, f)


TABLE_OR_ATTACHMENT_RE = re.compile(
    r"^\s*\|.*\|\s*$|\b(?:anhang|anbei|angehängt|attached|attachment|enclosed)\b", re.I | re.M
)


def drop_if_table(text: str, findings: list[Finding]) -> list[Finding]:
    """'each row' is fine when the reader has the table: in the text or attached."""
    if TABLE_OR_ATTACHMENT_RE.search(text):
        return [x for x in findings if x.rule != "structure-noun"]
    return findings


LIST_OR_HEADING_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)]|#+|\|)\s")


def prose_average(lines: list[tuple[int, str]], raw_by_no: dict, lang: str) -> tuple[float, int, int | None]:
    """Average words per sentence in prose. Lists, headings, tables, greetings and sign-offs do not count."""
    counts, first = [], None
    for start, para in paragraphs(lines):
        if LIST_OR_HEADING_RE.match(raw_by_no.get(start, "")):
            continue
        sents = sentences(para, lang)
        if len(sents) == 1 and count_words(sents[0], lang) <= 4:
            continue
        for s in sents:
            counts.append(count_words(s, lang))
            first = start if first is None else first
    return (sum(counts) / len(counts) if counts else 0.0), len(counts), first


# --- Voice profile (references/voice-profile.md) ---

VOICE_DIR = os.path.expanduser("~/.claude/voice")
DASHES = {" - ": r"(?<=[^\s\d])\s-\s(?=[^\s\d])", " – ": r"(?<=[^\s\d])\s–\s(?=[^\s\d])", "—": r"—", " -- ": r"\s--\s"}


def load_voice(path: str) -> dict:
    """Read the `overrides:` block from a profile's front matter. No YAML dependency: flat keys,
    numbers, quoted strings and [lists] only."""
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    block = re.search(r"^overrides:[^\n]*\n((?:[ \t]+.*\n?)*)", m.group(1) + "\n", re.M) if m else None
    voice: dict = {"path": path}
    for line in (block.group(1).splitlines() if block else []):
        km = re.match(r"\s+(\w+):\s*(.*?)\s*(?:#.*)?$", line)
        if not km:
            continue
        key, raw = km.groups()
        if raw.startswith("["):
            items = re.findall(r'"([^"]*)"|\'([^\']*)\'|([^,\[\]\s][^,\[\]]*)', raw)
            val = [next(x for x in it if x).strip() for it in items]
            val = [float(v) if re.fullmatch(r"\d+(?:\.\d+)?", v) else v for v in val]
        elif re.fullmatch(r"\d+(?:\.\d+)?", raw):
            val = float(raw)
        else:
            val = raw.strip("\"'")
        voice[key] = val
    return voice


def find_voice(arg: str, lang: str) -> dict | None:
    if arg == "none":
        return None
    path = os.path.join(VOICE_DIR, f"{lang}.md") if arg == "auto" else arg
    return load_voice(path) if os.path.isfile(path) else None


def mask_kept(text: str, voice: dict) -> str:
    """Hide the writer's own phrases and words from the tell checks. Keeps the word count."""
    for phrase in sorted(voice.get("keep_phrases", []) + voice.get("keep_words", []), key=len, reverse=True):
        text = re.sub(rf"(?<!\w){re.escape(phrase)}(?!\w)",
                      lambda m: " ".join("qq" for _ in m.group(0).split()), text, flags=re.I)
    return text


def voice_findings(text: str, lines: list[tuple[int, str]], raw_by_no: dict, lang: str, voice: dict) -> list[Finding]:
    f: list[Finding] = []
    own = voice.get("dash_char")
    words = max(len(WORD_RE.findall(text)), 1)
    total = sum(len(re.findall(p, text)) for p in DASHES.values())
    target = voice.get("dash_per_1k")
    if target and (words >= 300 or total >= 3) and total * 1000 / words > 1.5 * target:
        f.append(Finding(1, "dash", f"{total * 1000 / words:.1f} dashes per 1,000 words: your profile writes about {target:g} (§8)", ""))
    if own:
        for no, line in lines:
            for ch, p in DASHES.items():
                if ch != own and re.search(p, line):
                    f.append(Finding(no, "dash", f"dash '{ch.strip()}': your profile writes '{own.strip()}' (§8)", line.strip()[:100]))
    bounds = voice.get("sentence_avg")
    if isinstance(bounds, list) and len(bounds) == 2:
        avg, n, first = prose_average(lines, raw_by_no, lang)
        lo, hi = bounds
        if n >= 5 and avg < lo - 3:
            f.append(Finding(first, "rhythm", f"prose averages {avg:.1f} words per sentence: your profile writes {lo:g} to {hi:g}, so join sentences that share a thought", ""))
        elif n >= 5 and avg > hi + 5:
            f.append(Finding(first, "rhythm", f"prose averages {avg:.1f} words per sentence: your profile writes {lo:g} to {hi:g}, so split the longest sentences", ""))
    return f


def check_rhythm(lines: list[tuple[int, str]], raw_by_no: dict, lang: str) -> list[Finding]:
    """80% mode: flag prose that is a row of short sentences. Lists, headings and tables do not count."""
    counts, first = [], None
    for start, para in paragraphs(lines):
        if LIST_OR_HEADING_RE.match(raw_by_no.get(start, "")):
            continue
        sents = sentences(para, lang)
        if len(sents) == 1 and count_words(sents[0], lang) <= 4:
            continue  # greeting, sign-off or label
        for s in sents:
            counts.append(count_words(s, lang))
            first = start if first is None else first
    if len(counts) >= 5:
        avg = sum(counts) / len(counts)
        if avg < 12:
            return [Finding(first, "rhythm", f"prose averages {avg:.1f} words per sentence: join sentences that share a thought (aim for 15 to 20)", "")]
    return []


def check_lines_de(lines: list[tuple[int, str]], raw_by_no: dict, strict: bool) -> list[Finding]:
    f: list[Finding] = []
    for no, line in lines:
        if not line.strip():
            continue
        low = line.lower()
        excerpt = line.strip()[:100]
        if ";" in line:
            f.append(Finding(no, "semicolon", "Semikolon: zwei Sätze oder eine Liste (S15)", excerpt))
        if "—" in line or " -- " in line:
            f.append(Finding(no, "dash", "em dash is not a German dash: use ' – ' or a comma (§8)", excerpt))
        raw = raw_by_no.get(no, "")
        if re.search(r"(?:^|[\s(])“\w|\w”", raw):
            f.append(Finding(no, "quotes", "English quotes in German text: use „…“ (§21)", excerpt))
        elif re.search(r"(?:^|\s)\"[^\"`]+\"", line):
            f.append(Finding(no, "quotes", "straight quotes in German prose: use „…“ (§21, weak alone)", excerpt))
        for m in LONG_COMPOUND_DE.finditer(line):
            f.append(Finding(no, "compound", f"long compound '{m.group(0)}': a hyphen can help (S12)", excerpt))
        for pat, rule, msg in TELLS_DE:
            if re.search(pat, line, re.I):
                f.append(Finding(no, rule, msg, excerpt))
        for word, alt in SWAPS_DE.items():
            if re.search(rf"(?<![\w-]){re.escape(word)}\w*", low):
                f.append(Finding(no, "word", f"'{word}' -> {alt}", excerpt))
        if strict:
            if re.search(r"\b\w+['’]s\b", line):
                f.append(Finding(no, "contraction", "spoken form with apostrophe (gibt's): not in strict mode (S15)", excerpt))
            if re.search(r"\bz\.\s?B\.", line):
                f.append(Finding(no, "abbreviation", "'z. B.' -> 'zum Beispiel' in strict mode (S15)", excerpt))
            if re.search(r"\b(?:muss|müssen|musst)\s+(?:\S+\s+)?nicht\b", low):
                f.append(Finding(no, "modal", "'muss nicht' = not required, not a ban ('darf nicht'): check the meaning (S9)", excerpt))
    return f


def summary(text: str, lang: str = "en") -> dict:
    paras = paragraphs(strip_markdown(text))
    sents = [s for _, p in paras for s in sentences(p, lang)]
    counts = [count_words(s, lang) for s in sents] or [0]
    return {
        "lang": lang,
        "sentences": len(sents),
        "avg_words_per_sentence": round(sum(counts) / max(len(sents), 1), 1),
        "max_words_per_sentence": max(counts),
        "paragraphs": len(paras),
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Heuristic linter for AI tells and STE-style English or German (not a compliance checker, not an AI detector).")
    ap.add_argument("files", nargs="+", help="files to check, or - for stdin")
    ap.add_argument("--strict", action="store_true", help="strict mode: exact limits, more word rules")
    ap.add_argument("--lang", choices=["auto", "en", "de"], default="auto", help="text language (default: auto, per file)")
    ap.add_argument("--voice", default="auto", metavar="PATH|auto|none",
                    help="voice profile: auto uses ~/.claude/voice/<lang>.md if it exists (default), none ignores it")
    ap.add_argument("--json", action="store_true", help="output JSON")
    args = ap.parse_args(argv)

    total = 0
    report = []
    for path in args.files:
        if path == "-":
            text = sys.stdin.read()
        else:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        lang = detect_language(text) if args.lang == "auto" else args.lang
        voice = find_voice(args.voice, lang)
        findings = check(text, args.strict, lang, voice)
        total += len(findings)
        stats = summary(text, lang)
        stats["voice"] = voice["path"] if voice else None
        if args.json:
            report.append({"file": path, "stats": stats, "findings": [asdict(x) for x in findings]})
            continue
        vtag = f" | voice {os.path.basename(voice['path'])}" if voice else ""
        print(f"{path}: {len(findings)} finding(s) | lang {lang}{vtag} | {stats['sentences']} sentences, "
              f"avg {stats['avg_words_per_sentence']} words, max {stats['max_words_per_sentence']}")
        for x in findings:
            print(f"  {x.line:>4}  {x.rule:<16} {x.message}")
    if args.json:
        print(json.dumps(report, indent=2))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
