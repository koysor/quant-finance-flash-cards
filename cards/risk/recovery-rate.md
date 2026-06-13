# Recovery Rate

**Topic:** Risk
**Tags:** recovery rate, loss given default, LGD, credit risk, bond pricing, seniority
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **recovery rate** $R$ is the fraction of a defaulted obligation's face value that creditors ultimately receive, expressed as a percentage. The complement $(1 - R)$ is the **loss given default (LGD)**. Recovery is not received immediately at default — it arrives after a bankruptcy process that can take months or years — so the economically relevant quantity is the **present value of recovery**, discounted back to the default date. Recovery rates are highly uncertain, vary by seniority and collateral, and are negatively correlated with default rates (recoveries fall precisely when defaults spike).

## Key Formula

**Credit loss decomposition** (the fundamental credit risk identity):

$$\text{Expected Loss} = \text{PD} \times \text{LGD} \times \text{EAD}$$

where PD is the probability of default, LGD $= 1 - R$, and EAD is the exposure at default.

**Risky bond price** with recovery $R$ and risk-neutral default probability $\lambda\,dt$ (constant hazard rate $\lambda$):

$$P(0, T) = e^{-rT}\!\left[N(d_2) + R\cdot N(-d_2)\right] = e^{-rT}\!\left[1 - (1-R)\,N(-d_2)\right]$$

More generally, with stochastic recovery arriving at default time $\tau$:

$$P(0, T) = E^{\mathbb{Q}}\!\left[e^{-r\tau} R\,\mathbf{1}_{\tau \leq T}\right] + e^{-rT}\Pr^{\mathbb{Q}}(\tau > T)$$

**Credit spread** under constant hazard rate $\lambda$ and constant recovery $R$:

$$s \approx \lambda(1-R) \qquad \text{(credit triangle)}$$

Doubling $\lambda$ and doubling $(1-R)$ both double the spread, but they do so in fundamentally different ways — default timing vs. loss severity.

## Example

Senior secured bond, face £100m, maturity 3 years, coupon 0% (zero-coupon for simplicity), $r = 4\%$, hazard rate $\lambda = 2\%$ p.a., recovery rate $R = 60\%$ (LGD = 40%).

**Credit spread:** $s \approx 0.02 \times 0.40 = 80\,\text{bps}$

**Survival probability:** $\Pr(\tau > 3) = e^{-\lambda \times 3} = e^{-0.06} \approx 94.2\%$

**Bond price:**
$$P = e^{-(r+s) \times 3} \approx e^{-0.048 \times 3} \approx £86.5\text{m}$$

Compared with a risk-free bond at $£88.7\text{m}$ — the £2.2m difference is the credit risk premium. If recovery fell from 60% to 30% (LGD doubles to 70%), the spread doubles to 140 bps and the bond price falls to £83.7m, a £5m loss for the same default probability.

## Remember

The credit triangle $s \approx \lambda(1-R)$ is one of the most important identities in fixed income: it says the spread compensates for the **rate** of loss, not just the probability of default. This is why recovery rate assumptions dominate the pricing of **senior vs. subordinated** debt from the same issuer — two bonds with the same PD can have very different spreads if seniority changes LGD from 30% to 70%. In the 2008 financial crisis, AAA-rated mortgage tranches that seemed safe (low PD) turned out to have catastrophically low recoveries (high LGD) because housing price falls destroyed the collateral value simultaneously with the default wave. Assuming independence between PD and LGD — the standard simplification — understated losses precisely when it mattered most.
