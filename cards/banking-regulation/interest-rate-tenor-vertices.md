# Interest Rate Tenor Vertices

**Topic:** Banking Regulation
**Tags:** frtb, interest rate risk, sensitivity, delta, capital charge, regulation
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

Under the **Fundamental Review of the Trading Book (FRTB)**, interest rate tenor vertices are the ten prescribed maturity points — 0.25Y, 0.5Y, 1Y, 2Y, 3Y, 5Y, 10Y, 15Y, 20Y, and 30Y — to which all interest rate delta sensitivities must be mapped when computing the Sensitivity-Based Method (SBM) capital charge. Every position's rate sensitivity is bucketed into the nearest prescribed vertex, and the resulting per-vertex sensitivities are then aggregated using a prescribed correlation matrix to produce the IR delta risk charge.

## Key Formula

The IR delta risk charge for a single currency is computed as:

$$K_b = \sqrt{\sum_k s_k^2 \cdot \text{RW}_k^2 + \sum_{k} \sum_{k \neq l} \rho_{kl} \cdot s_k \cdot \text{RW}_k \cdot s_l \cdot \text{RW}_l}$$

where:
- $s_k$ is the net sensitivity at tenor vertex $k$ (sum of risk factor sensitivities mapped to that bucket)
- $\text{RW}_k$ is the prescribed risk weight for vertex $k$ (e.g. 1.13% at 0.25Y, 1.00% at 30Y for most currencies)
- $\rho_{kl}$ is the prescribed inter-vertex correlation: $\rho_{kl} = e^{-\alpha |t_k - t_l| / \min(t_k, t_l)}$, with $\alpha = 3\%$ under FRTB

The capital charge across currencies uses an inter-bucket aggregation step with prescribed cross-currency correlations.

## Example

A rates desk holds two positions in a single currency: a 4-year interest rate swap (sensitivity $s = \text{£200k}$ per bp) and a 9-year bond (sensitivity $s = \text{£150k}$ per bp). Under FRTB mapping:

- The 4-year swap sensitivity is assigned entirely to the **5Y vertex** (nearest prescribed point).
- The 9-year bond sensitivity is assigned entirely to the **10Y vertex**.

With risk weights $\text{RW}_{5Y} = 0.70\%$ and $\text{RW}_{10Y} = 0.70\%$, and inter-vertex correlation $\rho_{5Y,10Y} = e^{-0.03 \times |5-10|/5} \approx 0.741$:

$$K_b = \sqrt{(200 \times 0.007)^2 + (150 \times 0.007)^2 + 2 \times 0.741 \times (200 \times 0.007)(150 \times 0.007)}$$

$$= \sqrt{1.96 + 1.1025 + 2.205} \approx \text{£2,318k capital charge}$$

## Remember

Tenor vertices exist because regulators need a standardised, bank-agnostic grid for aggregating sensitivities — without fixed buckets, banks could exploit granularity differences to reduce their capital charge. The prescribed correlation formula ($\rho_{kl} = e^{-\alpha |t_k - t_l| / \min(t_k, t_l)}$) captures the empirical observation that adjacent points on the yield curve move together more than distant points, whilst the square-root aggregation (rather than simple summation) gives partial diversification credit across vertices. In practice, a position that does not sit exactly on a vertex must be interpolated across its two neighbouring vertices, conserving the total sensitivity but splitting it proportionally by maturity distance.
