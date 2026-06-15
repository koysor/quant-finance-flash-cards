# Completely Affine vs Essentially Affine

**Topic:** Fixed Income
**Tags:** market price of risk, term premium, duffee, affine model, risk-neutral, stochastic discount factor
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **completely affine** model (Dai–Singleton, 2000) restricts the market price of risk to be $\lambda_t = \Sigma(X_t)^{-1}(\lambda_0 + \lambda_1 X_t)$, keeping the physical dynamics in the affine class but forcing Sharpe ratios to scale with instantaneous volatility. An **essentially affine** model (Duffee, 2002) instead sets $\lambda_t = \lambda_0 + \lambda_1 X_t$ freely, decoupling the risk compensation from the volatility level.

## Key Formula

**Completely affine market price of risk:**

$$\lambda_t^{\text{CA}} = \Sigma(X_t)^{-1}(\lambda_0 + \lambda_1 X_t)$$

**Essentially affine market price of risk:**

$$\lambda_t^{\text{EA}} = \lambda_0 + \lambda_1 X_t$$

Both give physical dynamics:

$$dX_t = \bigl(K_0^{\mathbb{P}} + K_1^{\mathbb{P}} X_t\bigr)\,dt + \Sigma(X_t)\,dW_t^{\mathbb{P}}$$

For a CIR factor with $\Sigma = \sigma\sqrt{x}$, the completely affine choice forces $\lambda \propto 1/\!\sqrt{x}$, making the Sharpe ratio $\mu/\sigma\sqrt{x}$ constant — risk compensation must grow precisely as volatility falls. The essentially affine choice allows $\lambda = \lambda_0 + \lambda_1 x$, so the Sharpe ratio is free to vary with $x$ independently.

## Example

Suppose $x_t$ is a CIR factor with high values corresponding to high-volatility regimes. Under completely affine specification, the excess return on a bond is $\sigma\sqrt{x_t}\lambda_t = \lambda_0 + \lambda_1 x_t$ — so the term premium is a linear function of $x_t$ and peaks exactly during high-volatility periods. Under essentially affine, $\lambda_0 = 1.2$ and $\lambda_1 = -0.3$: at $x_t = 0.01$ (calm), the premium is $1.2 - 0.003 = 1.197\%$; at $x_t = 0.09$ (volatile), it is $1.2 - 0.027 = 1.173\%$ — virtually unchanged. Term premia can now be high in calm regimes and low in volatile ones, matching empirical patterns.

## Remember

The completely affine constraint was identified empirically as a major failure: it predicts that the term premium should spike during every volatility episode (1987, 2008) and collapse during calm periods. In reality, the US 10-year term premium was persistently negative in 2014–2019 despite low volatility. Duffee (2002) showed that relaxing the constraint — keeping $\lambda_t$ affine in $X_t$ rather than tying it to $\Sigma^{-1}$ — dramatically improves forecasts of excess bond returns and is now the standard assumption in central-bank term premium models such as ACM and Kim–Wright.
