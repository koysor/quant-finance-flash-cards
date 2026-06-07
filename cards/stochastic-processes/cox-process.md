# Cox Process

**Topic:** Stochastic Processes
**Tags:** cox process, doubly stochastic poisson, stochastic intensity, credit risk, default modelling, hazard rate
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Cox process** (also called a **doubly stochastic Poisson process**) is a Poisson process whose intensity $\lambda(t)$ is itself a stochastic process rather than a fixed constant. Events arrive according to a Poisson process conditional on the realised path of $\lambda(t)$, but $\lambda(t)$ evolves randomly — so both the timing of events *and* the underlying arrival rate are uncertain. In credit risk, the Cox process is the standard model for the random default intensity of a bond issuer.

## Key Formula

Conditional on the path $\{\lambda(s) : 0 \leq s \leq t\}$, the number of arrivals $N(t)$ is Poisson with mean $\Lambda(t) = \int_0^t \lambda(s)\,ds$ (the **integrated intensity**):

$$P\!\left(N(t) = k \;\Big|\; \Lambda(t)\right) = \frac{e^{-\Lambda(t)}\,\Lambda(t)^k}{k!}$$

**Survival probability** (no event by time $t$) — averaging over all paths of $\lambda$:

$$P(N(t) = 0) = \mathbb{E}\!\left[e^{-\Lambda(t)}\right] = \mathbb{E}\!\left[\exp\!\left(-\int_0^t \lambda(s)\,ds\right)\right]$$

For credit pricing, if $\lambda(t)$ follows a CIR process with mean-reversion speed $\kappa$, long-run mean $\bar{\lambda}$, and volatility $\nu$, the survival probability has a closed-form exponential-affine expression:

$$P(\tau > t) = A(t)\,e^{-B(t)\,\lambda_0}$$

where $A(t)$ and $B(t)$ are deterministic functions of $\kappa$, $\bar{\lambda}$, $\nu$, and $t$.

## Example

A corporate bond issuer has a stochastic default intensity modelled as a CIR process with $\lambda_0 = 0.02$, $\kappa = 0.5$, $\bar{\lambda} = 0.03$, $\nu = 0.1$.

| Horizon | Survival probability $P(\tau > t)$ |
|---|---|
| 1 year | 98.0% |
| 3 years | 91.4% |
| 5 years | 84.6% |
| 10 years | 73.1% |

Compare to a flat-intensity Poisson process with constant $\lambda = 0.03$: $P(\tau > 5) = e^{-0.15} = 86.1\%$. The Cox process gives a lower survival probability because the stochastic intensity occasionally spikes above 0.03, creating additional default risk not captured by the flat-rate model.

## Remember

The Cox process resolves the key deficiency of a plain Poisson process for credit modelling: a constant $\lambda$ cannot capture the fact that credit spreads — and hence default risk — change over time as macroeconomic conditions evolve. With a Cox process driven by a CIR intensity, the credit default swap (CDS) pricing formula remains analytically tractable (the exponential-affine structure), yet the model captures spread volatility and the tendency of defaults to cluster during recessions (when $\lambda$ is elevated for all issuers simultaneously). This clustering, called **default correlation**, is the central challenge in CDO tranche pricing and was at the heart of the 2008 structured-credit crisis: models that used flat Poisson intensities dramatically underpriced the probability of multiple simultaneous defaults, while Cox process models with correlated intensities would have produced far higher senior-tranche spreads.
