# FRTB Sensitivity-Based Method

**Topic:** Risk
**Tags:** frtb, market risk, capital, sensitivities, regulation, basel
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **Sensitivity-Based Method (SBM)** is the standardised approach under Basel IV's Fundamental Review of the Trading Book (FRTB) that calculates market risk capital by aggregating weighted delta, vega, and curvature sensitivities across prescribed risk factor classes: interest rates (GIRR), credit spreads (CSR), foreign exchange (FX), equity, and commodity.

## Key Formula

Capital for each risk class is computed in three stages. First, sensitivities are risk-weighted. For delta, the weighted sensitivity for position $i$ in bucket $b$ is:

$$WS_{k} = RW_{k} \times s_{k}$$

where $s_k$ is the net sensitivity (e.g. DV01 for interest rates) and $RW_k$ is the prescribed risk weight. Bucket-level capital aggregates across positions using a correlation matrix $\rho$:

$$K_b = \sqrt{\left(\sum_k WS_k\right)^2 + \sum_k \sum_{k \neq l} \rho_{kl} \cdot WS_k \cdot WS_l}$$

Total risk class capital then aggregates across buckets $b$ using inter-bucket correlations $\gamma$:

$$\text{Capital}_{\text{delta}} = \sqrt{\sum_b K_b^2 + \sum_b \sum_{b \neq c} \gamma_{bc} \cdot S_b \cdot S_c}$$

The same aggregation structure applies to vega (sensitivity to implied volatility) and curvature (the second-order residual not captured by delta), with the final SBM capital equal to the sum of delta, vega, and curvature charges across all risk classes.

## Example

A trading desk holds an interest rate swap with a DV01 of £10,000 (sensitivity to a 1 bp shift in rates). The FRTB GIRR risk weight for a 5-year tenor bucket is 1.15%.

**Weighted sensitivity:**

$$WS = 1.15\% \times \frac{£10{,}000}{0.0001} = 1.15\% \times £100{,}000{,}000 = £1{,}150{,}000$$

If this is the only position in the bucket, $K_b = £1{,}150{,}000$. This bucket capital feeds into the overall GIRR delta charge, which — combined with vega and curvature — contributes to total SBM capital.

## Remember

FRTB SBM replaced the Basel 2.5 standardised approach because regulators found that simple notional-based charges bore no relation to actual portfolio risk. The three-layer structure (delta captures linear sensitivity, vega captures volatility risk, curvature captures option non-linearity) mirrors how banks already think about Greeks-based risk management. For quant analysts, the key insight is that the aggregation formula with intra- and inter-bucket correlations is a stylised portfolio variance calculation — the prescribed correlation matrices are calibrated by the Basel Committee and cannot be substituted with internal estimates under the standardised approach. Banks with large derivatives books often find that running SBM alongside the Internal Models Approach (IMA) is necessary to demonstrate capital efficiency to regulators.
