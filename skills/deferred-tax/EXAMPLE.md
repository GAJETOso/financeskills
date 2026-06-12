# Worked Example - deferred-tax

## Ask

> Equipment carrying amount 90M, tax written-down value 65M, tax rate 30%. What's the deferred tax and which side?

## What a correct response contains

Taxable temporary difference 25M (carrying exceeds tax base on an asset) -> deferred tax LIABILITY of 7.5M.

## File-driven variant

With fixture(s) `evals/files/temporary_differences.csv`:

> Tax rate 30%. For each temporary difference in the attached file (evals/files/temporary_differences.csv), classify it as taxable or deductible, compute the DTL/DTA, and note that the warranty provision is a LIABILITY (carrying 250,000, tax base nil) and the revaluation difference goes through OCI.

Expected: PP&E: taxable TD 300,000 -> DTL $90,000. Warranty: deductible TD 250,000 -> DTA $75,000. Revaluation: taxable TD 200,000 -> DTL $60,000 recognized in OCI.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
