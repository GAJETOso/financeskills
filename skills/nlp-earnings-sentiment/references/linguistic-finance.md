# Linguistic Markers in Financial Disclosure

## Loughran-McDonald Word Lists (the finance standard)
General-purpose lexicons (Harvard-IV) misclassify ~75% of finance "negative" words (e.g., "tax", "cost", "liability" are routine). Use L-M categories:
- **Negative** (loss, impairment, litigation, restated), **Positive** (achieve, improve, strong), **Uncertainty** (approximately, contingent, may), **Litigious** (claimant, plaintiff), **Weak/Strong modal** (could/might vs. will/must), **Constraining** (covenant, restrict).

Metric: `category density = category word count / total words`, compared against the same company's history and sector peers.

## Documented Red-Flag Patterns (research-backed)
1. **Rising uncertainty + weak modal density** ahead of negative revisions.
2. **Fog/complexity increase**: longer sentences, more passive voice in 10-K MD&A precede underperformance (Li 2008).
3. **Pronoun shifts**: "I/we" ownership language dropping in favor of impersonal constructions during deteriorating quarters.
4. **Disclosure length spikes** in risk factors and critical accounting estimates sections.
5. **Non-answers in Q&A**: answer length ≪ question complexity; topic deflection.
6. **Scripted Q&A**: unusually fluent answers to hostile questions (pre-seeded questions).

## Quantitative Measures
- Gunning Fog index on MD&A year-over-year.
- Cosine similarity of consecutive 10-K risk sections: a sudden DROP means new risks added — read the diff.
- Negation handling: "not expecting growth" — apply 3-word negation windows when using lexicons.

## Caveats
Language signals are weak individually; combine ≥ 3 markers and always tie to the numbers (does tone diverge from reported results? divergence IS the signal).
