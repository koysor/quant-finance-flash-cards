# Credit Spread

**Topic:** Fixed Income
**Tags:** credit spread, corporate bond, default risk, yield spread, hazard rate, credit risk
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **credit spread** is the additional yield a risky bond must offer over a risk-free benchmark of the same maturity to compensate investors for the possibility of default. It is the market's price for bearing credit risk, embedding both the probability of default and the expected loss given default.

## Key Formula

$$\text{Credit spread} = y_{\text{risky}} - y_{\text{risk-free}}$$

Under a reduced-form model with constant hazard rate $\lambda$ and recovery rate $R$:

$$\text{Credit spread} \approx \lambda(1 - R)$$

So a bond with a 2% credit spread, assuming $R = 40\%$:

$$\lambda \approx \frac{0.02}{1 - 0.40} = \frac{0.02}{0.60} \approx 3.33\%\text{ per year}$$

The risky bond price is:

$$P_{\text{risky}} = P_{\text{risk-free}} \cdot Q(0, T)$$

where $Q(0,T) = e^{-\lambda T}$ is the survival probability.

## Example

A 5-year investment-grade corporate bond yields 5.20%. The 5-year government bond yields 4.00%. The credit spread is 120 bp (1.20%).

Using $R = 40\%$, the implied annual default probability is:

$$\lambda = \frac{0.012}{0.60} = 2.00\%\text{ per year}$$

The 5-year survival probability is $e^{-0.02 \times 5} = e^{-0.10} \approx 90.5\%$, so there is roughly a 9.5% implied probability the issuer defaults before year 5.

## Remember

Credit spreads are the primary metric for monitoring credit health in bond portfolios. During the 2008 crisis, investment-grade spreads widened from 100–200 bp to over 600 bp — implying default probabilities far beyond historical experience. The formula $\text{spread} \approx \lambda(1-R)$ is used constantly: to convert quoted CDS spreads into default probabilities for pricing, to estimate CVA adjustments, and to judge whether a bond's spread adequately compensates for its credit risk relative to peer issuers.
