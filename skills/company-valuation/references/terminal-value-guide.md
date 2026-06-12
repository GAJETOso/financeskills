# Terminal Value Discipline & the EV-to-Equity Bridge

## Terminal Value Sanity Rules
1. **Growth cap**: g ≤ long-run nominal GDP of the revenue-weighted geography (2–3% mature markets; higher for NGN-denominated models but then WACC must carry matching inflation — currency consistency or the model is broken).
2. **Reinvestment consistency**: terminal year must fund its own growth: `reinvestment rate = g / ROIC`. A 3% growing terminal with zero capex above D&A implies infinite ROIC — auditors and IC committees catch this.
3. **Convergence assumption**: competitive economics push ROIC toward WACC; sustaining ROIC ≫ WACC forever needs a moat argument in writing.
4. **Cross-check**: implied exit EV/EBITDA = TV / terminal EBITDA. Compare to today's comps; explain any premium.
5. **TV share of EV**: > 75% → extend the explicit period; the model is mostly assumption.

## Normalized Terminal Year Checklist
- EBITDA margin: mid-cycle, not peak/trough.
- Capex ≈ D&A × (1 + g adjustment); capex < D&A in perpetuity is impossible.
- NWC investment scales with g.
- Tax rate: statutory long-run, not this year's ETR quirks.

## EV-to-Equity Bridge (itemize ALL of these)
```
Enterprise Value
−  Gross debt (incl. overdrafts, current portion)
+  Cash & equivalents (haircut trapped/restricted cash)
−  Preferred equity, shareholder loans (terms decide debt vs equity)
−  Minority interest (at fair value if material, not book)
+  Associates/JVs and non-core investments (at fair value)
−  Pension/gratuity deficit (net of tax)
−  Lease liabilities (IF the multiple/FCF was pre-IFRS-16 consistent — match numerator and denominator!)
−  Provisions that are debt-like (decommissioning/ARO funded portion, litigation reserves)
−  Earnouts/contingent consideration payable
±  FX: bridge items at the same date and rate as EV
=  Equity value  → per share: dilute for options/warrants (treasury stock method)
```

## The IFRS 16 Trap
EV/EBITDA post-IFRS-16 (EBITDA excludes rent) vs. pre-IFRS-16 comps (EBITDA includes rent) differ systematically. Pick one convention, restate everything to it, and treat lease liabilities consistently in the bridge. Mixed conventions are the most common comps error since 2019.
