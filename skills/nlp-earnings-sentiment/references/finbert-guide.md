# FinBERT and Financial NLP Models

## Why Domain Models
General sentiment models misread finance: "liability decreased" is positive; "beat expectations despite headwinds" is positive; "in line with guidance" is neutral-positive. Finance-tuned models (FinBERT variants, e.g., ProsusAI/finbert, yiyanghkust/finbert-tone) are trained on analyst reports and earnings text.

## Usage Pattern
```python
from transformers import pipeline
clf = pipeline("text-classification", model="yiyanghkust/finbert-tone")
scores = clf(sentences)   # labels: Positive / Negative / Neutral
```
- Sentence-level scoring, then aggregate: `net tone = (pos − neg) / total sentences`.
- Chunk transcripts ≤ 512 tokens; split on sentence boundaries, never mid-sentence.

## Earnings Call Structure Matters
- **Prepared remarks**: scripted, uniformly positive — low signal. Compare vs. the company's own historical baseline, not absolute tone.
- **Q&A section**: highest signal. Analyze separately. Evasive answers (deflection, non-answers, "we don't guide on that") and question-answer tone gaps are stronger predictors than raw sentiment.
- Track **tone delta vs. prior quarters**, not levels.

## Beyond Sentiment
- Hedging density: counts of "approximately", "we believe", "subject to" per 100 words.
- Numeric specificity: ratio of quantified statements to total claims (specificity drops before bad news).
- Topic shift: new risk topics vs. prior call (embedding distance per section).

## Validation
Backtest tone deltas against post-call abnormal returns or subsequent guidance revisions before trusting any signal. Report correlation, not causation.
