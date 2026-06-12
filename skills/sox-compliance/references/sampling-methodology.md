# SOX Sampling Methodology

## Sample Size Logic
Attribute sampling at 90% confidence, 0 expected deviations, ~10% tolerable rate yields ~22–25 items for large populations — the source of the common "25 for daily controls" convention. Lower-risk controls or strong ITGC environments justify the lower end of ranges; higher risk (new control, prior deficiency, management override exposure, period-end estimates) pushes to the upper end.

## Risk-Tiering Adjustments
| Factor | Effect on sample |
|---|---|
| Prior-year exception on this control | +50–100%, no benchmarking |
| New/changed control or system | Test post-change period only, full sample within it |
| High judgment/estimation control | Upper end + senior reviewer |
| Strong, tested ITGCs + automated control | 1 per configuration; benchmark up to 2 future years if no change |

## Exception Handling Protocol
1. Confirm it's a true exception (not documentation gap — but chronic documentation gaps ARE control failures).
2. Root cause with the control owner, in writing.
3. Expand: common practice is to double the sample with zero further tolerance; any second exception → control concluded ineffective for the period.
4. Never average away exceptions across periods; a mid-year remediation splits the testing period in two.

## Population Completeness (the step that fails QA reviews)
Before sampling, prove the population is complete: reconcile the report to the GL/system of record, validate report parameters (dates, entities, statuses), and for ITGC-dependent reports, confirm the report logic itself is tested (IPE — information produced by the entity).

## Interim vs. Year-End (Rollforward)
Interim testing (e.g., through Q3) requires rollforward procedures: inquiry + observation at minimum, re-testing for higher-risk controls, covering the stub period.

## Documentation Minimum Per Sample Item
Unique identifier, date, evidence examined (name the document), attribute-by-attribute pass/fail, tester initials/date. "No exceptions noted" without item-level detail is not evidence.
