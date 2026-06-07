# Intensity-Based Credit Model

**Topic:** Stochastic Processes
**Tags:** intensity-based model, reduced-form model, hazard rate, default time, credit risk, survival probability
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

An **intensity-based credit model** (also called a **reduced-form model**) treats default as the first jump of a Cox process: default occurs at a random time $\tau$ driven by a stochastic hazard rate $\lambda(t)$, without modelling the borrower's asset value explicitly. The hazard rate $\lambda(t)$ is calibrated to market credit spreads and can be driven by macroeconomic factors. In contrast to structural models (which require knowing asset values), intensity-based models are directly fitted to bond prices and CDS spreads, making them the standard approach for credit derivatives pricing.

## Key Formula

**Default time** $\tau$ is defined via the integrated hazard:

$$\tau = \inf\!\left\{t > 0 : \int_0^t \lambda(s)\,ds \geq E\right\}, \quad E \sim \operatorname{Exp}(1)$$

**Survival probability** (probability of no default before $T$):

$$P(\tau > T \mid \mathcal{F}_t) = E\!\left[\exp\!\left(-\int_t^T \lambda(s)\,ds\right) \Bigg| \mathcal{F}_t\right]$$

**Defaultable zero-coupon bond price** (risk-neutral, zero recovery):

$$P^D(t, T) = E^Q\!\left[\exp\!\left(-\int_t^T (r(s) + \lambda(s))\,ds\right) \Bigg| \mathcal{F}_t\right]$$

so the credit spread $s(t,T) \approx E^Q[\lambda]$ — the intensity is directly the spread.

**Affine model** (CIR intensity $\lambda$ for tractable closed form):

$$d\lambda = \kappa(\theta - \lambda)\,dt + \sigma\sqrt{\lambda}\,dW$$

$$P(\tau > T \mid \lambda_t) = A(T-t)\,e^{-B(T-t)\lambda_t}$$

where $A(\cdot)$ and $B(\cdot)$ are deterministic functions (same as bond pricing in the Cox–Ingersoll–Ross rate model).

## Example

A IG-rated corporate with CIR intensity: $\kappa = 0.5$, $\theta = 0.01$, $\sigma = 0.05$, current $\lambda_0 = 0.02$ (200 bps spread).

| Horizon | Survival probability | Spread (approx) |
|---|---|---|
| 1 year | 98.0% | 200 bps |
| 3 years | 94.2% | 198 bps |
| 5 years | 90.6% | 196 bps |
| 10 years | 83.3% | 183 bps |

The mean-reversion pulls long-tenor spreads toward the long-run level $\theta = 100$ bps (1%), so the term structure of credit spreads is downward sloping from 200 bps — a common pattern for investment-grade names whose current spread exceeds the long-run average.

## Remember

Intensity-based models became the industry standard for **CDS pricing** because the hazard rate $\lambda(t)$ maps directly to the observable CDS spread: a 5-year CDS paying $s$ per annum approximately satisfies $s \approx \lambda \times (1 - R)$, where $R$ is the recovery rate. Stripping the term structure of CDS spreads bootstraps the piecewise-constant hazard rate curve $\lambda(t)$, exactly as stripping swap rates bootstraps the discount curve. The model's weakness is that it treats default as a pure surprise (the hazard rate can never be zero right before default), which is realistic for liquid credits but less so for distressed issuers where the market anticipates default. The CQF application is **risky bond pricing**: the defaultable bond price formula $P^D = P\cdot P(\tau > T)$ (for independent rates and intensity) decomposes cleanly into a riskless bond times a survival probability, allowing credit and rates to be modelled separately before combining.
