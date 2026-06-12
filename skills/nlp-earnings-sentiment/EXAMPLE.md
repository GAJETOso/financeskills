# Worked Example - nlp-earnings-sentiment

## Ask

> Analyze the sentiment of this earnings call transcript. Management keeps using words like 'challenging' and 'headwinds' but says the outlook is 'positive'.

## What a correct response contains

Should identify a potential 'Tone Shift' or mismatch between specific negative descriptors and general positive outlook. Should focus on the Q&A section for reveal. Should mention uncertainty mapping (tracking 'challenging', 'headwinds'). Should provide a Sentiment Scorecard.

## File-driven variant

With fixture(s) `evals/files/earnings_call_excerpt.txt`:

> Analyze the attached earnings-call excerpt (evals/files/earnings_call_excerpt.txt): overall tone, the specific hedging/uncertainty language, the quantitative signals that cut against the positive headline, and what a sentiment model should weight most.

Expected: Surface tone positive (record OCF, 18% growth, guidance reiterated) but hedged: 'prudent to assume', 'admittedly uncertain', 'yet'. Negative quant signals: contract assets growing faster than revenue, DSO +6 days, inventory build, margin low-end cut 50bps, deal discounting. Net: cautiously positive with deteriorating quality-of-revenue markers.
