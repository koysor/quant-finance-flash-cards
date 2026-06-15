# Hazard Rate Bootstrapping

**Topic:** Fixed Income
**Tags:** hazard rate, bootstrapping, credit default swap, survival probability, credit curve, cds spread
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Hazard rate bootstrapping** extracts a piecewise constant default intensity (hazard rate) curve from quoted CDS spreads. Each maturity's CDS strips the hazard rate for that interval by solving a single equation that exactly reprices the instrument, conditional on the rates already determined at shorter maturities.

## Key Formula

Under piecewise constant hazard rates $\lambda_i$ on $[t_{i-1}, t_i)$, the survival probability is:

$$Q(T) = \exp\!\left(-\sum_{i=1}^{k-1}\lambda_i\,(t_i - t_{i-1}) - \lambda_k\,(T - t_{k-1})\right), \quad t_{k-1} \leq T < t_k$$

A CDS with spread $c$, recovery $R$, and maturity $T_k$ prices at par when:

$$c \cdot \underbrace{\sum_j P(t_j)\,Q(t_j)\,\Delta t_j}_{\text{premium leg (RPV01)}} = (1 - R)\cdot \underbrace{\int_0^{T_k} P(t)\,Q(t)\,\lambda(t)\,dt}_{\text{protection leg}}$$

Solving for $\lambda_k$ given $\lambda_1, \ldots, \lambda_{k-1}$ completes the bootstrap.

## Example

Suppose the 1-year CDS spread is 100 bp and the 3-year CDS spread is 200 bp, with recovery $R = 40\%$ and flat risk-free rate 5%.

**Step 1** (1Y): solve for $\lambda_1$ from the 1Y CDS alone. Approximate: $\lambda_1 \approx c/(1-R) = 0.01/0.6 \approx 0.0167$.

**Step 2** (3Y): given $\lambda_1$ from Step 1, solve for $\lambda_2$ from the 3Y CDS. The two unknowns decouple exactly because $\lambda_1$ governs $[0,1)$ and $\lambda_2$ governs $[1,3)$.

## Remember

Hazard rate bootstrapping is the credit analogue of yield curve bootstrapping: both strip a piecewise constant parameter sequentially from quoted instruments, with each new maturity introducing exactly one unknown. The resulting credit curve directly gives survival probabilities $Q(T)$ used to price CDS, credit-linked notes, and CVA adjustments. In practice, a flat recovery assumption of 40% is standard; changing it shifts the hazard rate level but not the shape of the curve.
