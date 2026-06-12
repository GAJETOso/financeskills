# Worked Example - esg-reporting

## Ask

> Our factory used 1,000 MWh of electricity this year. Is this Scope 1 or Scope 2 emissions?

## What a correct response contains

Should identify purchased electricity as Scope 2. Should explain that Scope 1 is for direct on-site combustion. Should suggest reporting this as part of an ESG Performance Report.

## File-driven variant

With fixture(s) `evals/files/activity_data.csv`:

> Compute Scope 1 and Scope 2 (location-based) emissions in tCO2e from the attached activity data and factors (evals/files/activity_data.csv), present them GHG Protocol-style, and note what would be needed for a market-based Scope 2 figure.

Expected: Scope 1 804.4 tCO2e (diesel 482.4 + gas 183.3 + fleet 138.6); Scope 2 location-based 1,032.0 tCO2e; market-based needs supplier-specific/REC factors.
