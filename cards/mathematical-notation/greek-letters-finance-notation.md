# Greek Letters in Finance Notation

**Topic:** Mathematical Notation
**Tags:** notation, Greek letters, alpha, beta, sigma, delta, mu, rho, theta, lambda
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

Greek letters provide a compact vocabulary of symbols that are used consistently across quantitative finance. Each letter has one or two dominant meanings that practitioners rely on:

| Letter | Symbol | Primary finance meaning |
|---|---|---|
| Alpha | $\alpha$ | Excess return (Jensen's alpha); significance level in hypothesis testing |
| Beta | $\beta$ | Systematic risk (CAPM); regression slope; also option vega in some texts |
| Gamma | $\Gamma$ | Option gamma (second derivative of price w.r.t. spot); gamma function $\Gamma(n) = (n-1)!$ |
| Delta | $\Delta$ | Option delta (first derivative w.r.t. spot); also finite difference $\Delta x = x_1 - x_0$ |
| Epsilon | $\varepsilon$ | Regression error term; small positive number in $\varepsilon$-$\delta$ proofs |
| Eta | $\eta$ | Vol-of-vol parameter (SABR model); market impact coefficient |
| Theta | $\Theta$ | Option theta (time decay); also $\theta$ for mean-reversion level in Vasicek/CIR |
| Kappa | $\kappa$ | Mean-reversion speed in Ornstein-Uhlenbeck / Vasicek / CIR models |
| Lambda | $\lambda$ | Market price of risk ($\lambda = (\mu-r)/\sigma$); Poisson intensity; regularisation |
| Mu | $\mu$ | Drift (expected return); population mean |
| Nu | $\nu$ | Degrees of freedom ($t$-distribution); also used for vega |
| Rho | $\rho$ | Correlation; option rho (sensitivity to interest rate) |
| Sigma | $\sigma$ | Volatility (standard deviation); also $\Sigma$ for covariance matrix |
| Tau | $\tau$ | Time to maturity $\tau = T - t$; stopping time |
| Phi | $\phi$ | Standard normal PDF; also $\Phi$ for standard normal CDF |
| Chi | $\chi$ | Chi-squared distribution ($\chi^2$) |
| Psi | $\psi$ | Characteristic exponent of a Lévy process |
| Omega | $\omega$ | Sample outcome ($\omega \in \Omega$); long-run variance in GARCH |

## Key Formula

**CAPM in Greek:**

$$E[R_i] - r_f = \alpha_i + \beta_i (E[R_m] - r_f)$$

**GBM dynamics:**

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

**Ornstein-Uhlenbeck (mean-reversion):**

$$dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t$$

## Example

The Black-Scholes Greeks in one line: $\Delta = N(d_1)$, $\Gamma = N'(d_1)/(\sigma S\sqrt{T})$, $\Theta = -(\sigma S N'(d_1))/(2\sqrt{T}) - rKe^{-rT}N(d_2)$, $\rho = KTe^{-rT}N(d_2)$. Each Greek letter is the partial derivative of option value $V$ with respect to one parameter — the notation compresses a full sensitivity report into a handful of symbols.

## Remember

The **market price of risk** $\lambda = (\mu - r)/\sigma$ is the ratio of excess return to volatility — it appears in the Girsanov change-of-measure formula and explains why risk-neutral pricing does not depend on $\mu$. The Greeks $\Delta$, $\Gamma$, $\Theta$ are the most operationally important symbols in options trading: a market-maker hedges by keeping $\Delta = 0$ (delta-neutral), monitors $\Gamma$ for convexity risk, and earns/pays $\Theta$ as time value decays. Knowing the dominant meaning of each Greek letter prevents misreading formulae when context shifts between statistics, stochastic processes, and derivatives.
