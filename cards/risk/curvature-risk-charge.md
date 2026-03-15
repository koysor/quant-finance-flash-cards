# Curvature Risk Charge

**Topic:** Risk
**Tags:** FRTB, curvature, convexity, sensitivity-based method, market risk, regulation
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **Curvature Risk Charge** is a capital add-on in the FRTB Sensitivity-Based Method (SBM) that captures the **second-order (convexity) risk** not covered by the delta sensitivity charge. It is computed by applying large upward and downward stress shifts to each risk factor and measuring how much the actual portfolio P&L deviates from the linear delta approximation, after netting off the delta hedge gain.

## Key Formula

For each risk factor $k$, apply a stress shift $s_k$ up and down. The curvature loss for shift direction $i \in \{+, -\}$ is:

$$CVR_k^{(i)} = -\left[ V(x_k^{(i)}) - V(x_k) - s_k^{(i)} \cdot \delta_k \right]$$

where $V(x_k)$ is the current portfolio value, $V(x_k^{(i)})$ is the revalued portfolio after the stress, $s_k^{(i)}$ is the signed shift ($\pm$), and $\delta_k$ is the net delta sensitivity (the linear hedge).

The **Curvature Risk Charge** aggregates across risk factors using the prescribed correlation matrix $\rho$:

$$\text{CRC} = \max\!\left(K_{\text{high}},\, K_{\text{medium}},\, K_{\text{low}}\right)$$

where each scenario $K$ is:

$$K = \max\!\left(0,\; \sum_k CVR_k + \sqrt{\sum_k CVR_k^2 + \sum_{k \neq l} \rho_{kl}\, CVR_k\, CVR_l}\right)$$

The three scenarios use different prescribed correlation scalings (high, medium, low) and the worst-case capital charge is taken.

## Example

A trading book holds a long call option with delta $\delta = 0.50$ and gamma $\Gamma = 0.04$. The regulator's prescribed stress shift is $s = +20\%$ of the spot price ($\Delta S = £20$ on a £100 stock).

- **Revalued option gain (actual):** $\approx 0.50 \times 20 + \frac{1}{2} \times 0.04 \times 400 = £10 + £8 = £18$
- **Delta hedge gain (linear):** $0.50 \times 20 = £10$
- **Curvature loss:** $CVR^{(+)} = -(18 - 10 - 10) = -£(-2)$, i.e. a **gain of £8** for a long gamma position.

For a **short gamma** position (sold option), the curvature loss would be $+£8$, generating a positive CVR and hence a capital charge.

## Remember

The Curvature Risk Charge targets instruments with **non-linear payoffs** — options, structured products, bonds with embedded optionality. A purely linear book (cash equities, plain vanilla swaps) has zero curvature charge. In FRTB, curvature is distinct from delta and vega: regulators require separate sensitivity calculations for all three. Firms with large short-gamma books (e.g., option sellers) face the biggest curvature capital charges, incentivising them to manage convexity exposure carefully.
