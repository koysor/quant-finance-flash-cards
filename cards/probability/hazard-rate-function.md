# Hazard Rate Function

**Topic:** Probability
**Tags:** survival analysis, default probability, credit risk, intensity, CDS
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **hazard rate** (or **intensity**) $h(t)$ is the instantaneous rate of failure at time $t$, conditional on survival up to that point. It is defined as the ratio of the probability density function to the survival function. Unlike the PDF, the hazard rate directly answers: "given that an entity has survived until now, how likely is it to fail in the next instant?"

## Key Formula

$$h(t) = \frac{f(t)}{1 - F(t)} = -\frac{d}{dt}\ln\bigl(1 - F(t)\bigr)$$

**Survival function** from the hazard rate:

$$S(t) = 1 - F(t) = \exp\!\left(-\int_0^t h(u)\,du\right)$$

**Constant hazard** $h(t) = \lambda$ gives the exponential distribution:

$$S(t) = e^{-\lambda t}, \qquad f(t) = \lambda e^{-\lambda t}$$

| Hazard rate $\lambda$ | 1-year survival $S(1)$ | 5-year survival $S(5)$ |
|---|---|---|
| $0.01$ | $99.0\%$ | $95.1\%$ |
| $0.05$ | $95.1\%$ | $77.9\%$ |
| $0.10$ | $90.5\%$ | $60.7\%$ |

## Example

A corporate bond issuer has a constant hazard rate of $\lambda = 0.03$ (3% per annum). What is the probability of default within 5 years?

$$P(\text{default} \leq 5) = 1 - S(5) = 1 - e^{-0.03 \times 5} = 1 - e^{-0.15} = 1 - 0.8607 = 0.1393$$

There is approximately a 13.9% chance of default within 5 years.

## Remember

The hazard rate is the language of credit modelling. In reduced-form credit models (Jarrow–Turnbull, Duffie–Singleton), the default intensity $\lambda(t)$ is the fundamental input — it can be calibrated directly from credit default swap (CDS) spreads using the approximation $\text{CDS spread} \approx \lambda \times (1 - R)$, where $R$ is the recovery rate. The exponential survival function $e^{-\lambda t}$ is the credit analogue of the discount factor $e^{-rt}$ — just as interest rates discount cash flows for the time value of money, hazard rates discount them for the probability of default. When the hazard rate is stochastic (Cox process), it drives the correlation structure in portfolio credit models used for CDO pricing.
