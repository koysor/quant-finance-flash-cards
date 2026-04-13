# Expected Exposure

**Topic:** Banking Regulation
**Tags:** expected exposure, counterparty risk, cva, derivatives, mark-to-market
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Expected Exposure (EE) at a future time $t$ is the probability-weighted average of the positive mark-to-market value of a derivatives portfolio — the amount a bank would lose if the counterparty defaulted at exactly that moment. EE is unilateral: when the portfolio has negative value to the bank (i.e., the bank owes money), the exposure is zero because the bank would not lose anything on the default.

## Key Formula

Let $V_t$ be the mark-to-market portfolio value at time $t$. Then:

$$EE(t) = \mathbb{E}[\max(V_t,\; 0)]$$

The **Expected Positive Exposure (EPE)** averages EE over all future dates up to maturity $T$:

$$EPE = \frac{1}{T}\int_0^T EE(t)\, dt$$

For an interest rate swap with maturity $T$ and annualised volatility $\sigma$, EE peaks midway through the trade (the "hump"):

$$EE(t) \approx \sigma \sqrt{t} \cdot \phi(0) \cdot \text{(notional)}$$

where $\phi(0)$ is the standard normal density at zero.

## Example

A 5-year interest rate swap has a notional of £100 m and an annualised rate volatility of 1% per year. At year 2, the standard deviation of the mark-to-market is approximately $0.01 \times \sqrt{2} \times 100\text{m} \approx £1.41\text{m}$. The EE at year 2 (using the half-normal approximation) is roughly $£1.41\text{m} / \sqrt{2\pi} \approx £0.56\text{m}$.

## Remember

EE is the primary input for CVA: $\text{CVA} \approx (1-R)\sum_i EE(t_i) \cdot PD(t_i)$. The characteristic "hump" shape of EE for an interest rate swap — rising from zero at inception, peaking at roughly one-third of maturity, then falling back to zero at expiry — directly shapes the CVA profile. Understanding this shape helps quants decide which maturities dominate counterparty credit risk and therefore where CDS hedges should be concentrated.
