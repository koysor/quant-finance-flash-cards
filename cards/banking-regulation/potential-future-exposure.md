# Potential Future Exposure

**Topic:** Banking Regulation
**Tags:** potential future exposure, pfe, counterparty risk, var, credit limit
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Potential Future Exposure (PFE) at time $t$ is the high-confidence quantile (e.g., 95th or 99th percentile) of the positive mark-to-market distribution of a derivatives portfolio — the worst-case credit exposure the bank would face at that future date. While Expected Exposure (EE) gives the average exposure, PFE measures the tail exposure used for credit limit management and regulatory capital.

## Key Formula

$$PFE_q(t) = \text{Quantile}_q\bigl[\max(V_t,\; 0)\bigr]$$

For a single trade with zero current value and portfolio value distributed as $\mathcal{N}(0, \sigma_t^2)$:

$$PFE_{95\%}(t) \approx 1.645\,\sigma_t, \qquad PFE_{99\%}(t) \approx 2.326\,\sigma_t$$

where $\sigma_t = \sigma_1\sqrt{t}$ under constant volatility. For an interest rate swap, $\sigma_t$ typically peaks at mid-life, giving PFE a "hump" profile like EE but at a higher level.

## Example

A 3-year FX forward has a notional of £50 m and a daily price volatility of 0.5%. Over 1 year, $\sigma_t = 0.5\% \times \sqrt{250} \approx 7.9\%$.

$$PFE_{95\%}(1\text{ yr}) = 1.645 \times 0.079 \times £50\text{m} \approx £6.5\text{m}$$

This £6.5 m represents the maximum loss the bank would face if the counterparty defaulted in one year's time under a 95% confidence scenario — used to check whether the trade fits within the counterparty's credit limit.

## Remember

Credit desks use PFE profiles — plotted across the entire life of a trade — as the primary tool for managing counterparty credit limits: the limit must not be breached by the PFE at any future date. Banks with tight limits on a counterparty can reduce PFE by adding collateral triggers (CSA thresholds), by shortening trade tenor, or by entering offsetting trades in the same netting set. SA-CCR, the regulatory capital framework for counterparty credit risk, approximates PFE using supervisory add-ons rather than a full Monte Carlo, making PFE a direct input into the capital charge.
