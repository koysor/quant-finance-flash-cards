# Interest Rate Market Price of Risk

**Topic:** Fixed Income
**Tags:** market price of risk, interest rate, non-traded, risk premium, risk-neutral, measure change
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **market price of interest rate risk** $\lambda(r,t)$ measures the excess expected return per unit of short-rate randomness that investors demand for bearing interest rate risk. It appears in the fixed-income pricing PDE because the short rate $r$ — unlike a stock price — is not a traded asset and therefore cannot self-hedge.

## Key Formula

From the bond hedging argument, $\lambda$ is the universal function satisfying:

$$\lambda(r,t) = \frac{\frac{\partial V}{\partial t} + \frac{1}{2}w^2\frac{\partial^2 V}{\partial r^2} + u\frac{\partial V}{\partial r} - rV}{w\frac{\partial V}{\partial r}}$$

for any bond $V$. Its effect is to shift the real-world drift to the **risk-neutral drift**:

$$u^{\mathbb{Q}}(r,t) = u(r,t) - \lambda(r,t)\,w(r,t)$$

| Measure | Drift of $r$ | Use |
|---|---|---|
| $\mathbb{P}$ (real world) | $u(r,t)$ | Historical simulation |
| $\mathbb{Q}$ (risk-neutral) | $u - \lambda w$ | Pricing and Monte Carlo |

For Vasicek, $\lambda$ is commonly taken as constant, which simply shifts the long-run mean: $\eta^{\mathbb{Q}} = \eta - \lambda\sqrt{\beta}$.

## Example

Suppose the Vasicek real-world parameters are $\eta = 0.03$, $\gamma = 0.4$, $\beta = 0.0001$ and the market price of risk is $\lambda = -0.5$. Then $\lambda\sqrt{\beta} = -0.5 \times 0.01 = -0.005$, and the risk-neutral long-run level shifts to $\eta^{\mathbb{Q}}/\gamma = (0.03 + 0.005)/0.4 = 8.75\%$ — higher than the real-world mean of 7.5%, reflecting the risk premium demanded by investors.

## Remember

$\lambda$ is the interest rate analogue of the Sharpe ratio in equity markets but with one key difference: in equity Black–Scholes, $\lambda$ cancels from the option price because the stock hedges itself. In interest rate models, $\lambda$ does **not** cancel — it must be estimated from the cross-section of bond prices or historically, and uncertainty in $\lambda$ is a major source of model risk in fixed-income derivatives pricing.
