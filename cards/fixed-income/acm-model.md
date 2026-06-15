# Adrian–Crump–Moench (ACM) Model

**Topic:** Fixed Income
**Tags:** term premium, acm model, ny fed, principal components, essentially affine, treasury yields
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The Adrian–Crump–Moench (ACM, 2013) model is a five-factor, discrete-time, essentially affine Gaussian term structure model that decomposes US Treasury yields into a risk-neutral rate expectation and a time-varying term premium, estimated by the Federal Reserve Bank of New York from principal components of the yield curve.

## Key Formula

**State vector:** $X_t \in \mathbb{R}^5$ — the first five principal components of the Treasury yield curve.

**Measurement equation** (yields affine in state):

$$y_t(\tau) = A_\tau + B_\tau^\top X_t + \varepsilon_t(\tau)$$

**Transition equation** (VAR(1) under $\mathbb{P}$):

$$X_{t+1} = \mu + \Phi X_t + v_{t+1}, \quad v_{t+1} \sim \mathcal{N}(0, \Sigma)$$

**Essentially affine pricing kernel** (log SDF):

$$m_{t+1} = -r_t - \tfrac{1}{2}\lambda_t^\top\lambda_t - \lambda_t^\top v_{t+1}$$

**Market price of risk:** $\lambda_t = \lambda_0 + \lambda_1 X_t$

**Term premium decomposition:**

$$y_t(\tau) = \underbrace{\frac{1}{\tau}\sum_{k=0}^{\tau-1}\mathbb{E}_t^{\mathbb{P}}[r_{t+k}]}_{\text{rate expectations}} + \underbrace{tp_t(\tau)}_{\text{term premium}}$$

## Example

Based on the NY Fed's ACM estimates for the US 10-year Treasury:

| Period | Yield | Rate Expectation | Term Premium |
|---|---|---|---|
| Jan 2014 | 2.86% | 3.10% | $-0.24\%$ |
| Jan 2019 | 2.72% | 2.90% | $-0.18\%$ |
| Jan 2023 | 3.88% | 3.20% | $+0.68\%$ |
| Jan 2024 | 3.97% | 3.55% | $+0.42\%$ |

From 2014 to 2019 the term premium was negative: the QE-driven demand for long bonds compressed yields below expected short rates. The 2022–23 QT cycle reversed this, pushing the term premium above zero even as rate expectations rose more modestly.

## Remember

When journalists report that "bond yields rose due to inflation expectations," the ACM decomposition often tells a different story: a significant fraction of the move may be in the term premium, not rate expectations. Central banks monitor ACM specifically because the term premium component reflects supply-demand dynamics, liquidity conditions, and investor risk appetite — factors that monetary policy affects differently than it affects short-rate expectations. A rising term premium can tighten financial conditions independently of any Fed rate decision.
