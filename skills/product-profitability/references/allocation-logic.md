# Cost Allocation Logic

## Allocation Hierarchy (best to worst)
1. **Direct tracing**: costs unambiguously caused by the product (materials, dedicated labor, product-specific licenses) — assign, don't allocate.
2. **Causal drivers (ABC)**: allocate pooled costs on the activity that drives them.
3. **Ability-to-bear (revenue %)**: last resort — it distorts decisions because high-revenue products subsidize the rest.

## Activity-Based Costing in Five Steps
1. Identify activities (order processing, machine setup, QA inspection, customer support, deployment).
2. Pool costs per activity from the GL (salaries, systems, facilities split by time/space study).
3. Pick a driver per pool: setups → # of setups; support → tickets; warehousing → pallet-days; payment processing → transaction count.
4. Rate = pool cost / driver volume.
5. Charge products: usage × rate.

## Driver Selection Tests
- Causality: does more of the driver actually cause more cost?
- Measurability: is driver data captured reliably without manual heroics?
- Materiality: pools < 5% of overhead can use a simple driver; don't gold-plate.

## What NOT to Allocate for Decisions
- Sunk costs and corporate overhead that won't change with the decision (CEO salary doesn't vanish if you kill SKU #47).
- Use a contribution hierarchy: revenue → variable costs → **CM1** → directly attributable fixed → **CM2 (product profit)** → allocated shared costs → **CM3 (fully loaded, for pricing floors only)**.
- Kill/keep decisions: CM2 + avoidable cost test. Pricing floors: CM3. Never reverse them.

## Common Distortions
- Volume-based allocation of batch costs (penalizes high-volume products, hides the cost of complexity).
- Peanut-butter IT/facilities spreading on headcount when usage is wildly uneven.
- Ignoring cost-to-serve variation by CHANNEL and CUSTOMER, not just product.
