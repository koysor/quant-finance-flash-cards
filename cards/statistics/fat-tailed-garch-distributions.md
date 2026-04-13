# Fat-Tailed Conditional Distributions for GARCH

**Topic:** Statistics
**Tags:** garch, fat tails, student-t, kurtosis, tail risk, maximum likelihood
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

A standard GARCH model assumes that the standardised residuals $z_t = \varepsilon_t / \sigma_t$ are drawn from a standard normal distribution. In practice, even after GARCH removes volatility clustering, $z_t$ still exhibits **excess kurtosis** — the tails are heavier than normal. Two parametric solutions replace the Gaussian innovation with a fat-tailed distribution fitted jointly with the GARCH parameters:

- **Student-$t_\nu$**: parameterised by degrees of freedom $\nu$; as $\nu \to \infty$ it converges to the normal. The tail parameter $\zeta = 1/\nu$ is estimated via maximum likelihood alongside $\omega$, $\alpha$, $\beta$.
- **Generalised Error Distribution (GED)**: parameterised by shape $\nu$; $\nu = 2$ is normal, $\nu < 2$ gives fat tails, $\nu = 1$ is Laplace.

Both distributions allow the model to assign higher probability to large standardised shocks, capturing the residual non-normality that GARCH alone cannot eliminate.

## Key Formula

**Student-$t_\nu$ kurtosis** (defined only for $\nu > 4$):

$$\text{Kurt}[z_t] = 3 + \frac{6}{\nu - 4}$$

Excess kurtosis $= \dfrac{6}{\nu - 4}$, which is always positive for $\nu > 4$ and $\to \infty$ as $\nu \to 4^+$.

**GED density** (zero mean, unit variance form):

$$f(z;\,\nu) \propto \exp\!\left(-\tfrac{1}{2}\left|\frac{z}{\lambda}\right|^{\!\nu}\right), \qquad \lambda = \left(\frac{2^{-2/\nu}\,\Gamma(1/\nu)}{\Gamma(3/\nu)}\right)^{1/2}$$

**Distribution comparison:**

| Distribution | Shape param | Excess kurtosis | Tail behaviour |
|---|---|---|---|
| Normal | — | 0 | Light (thin) |
| Student-$t$ ($\nu = 8$) | $\nu = 8$ | 1.5 | Moderate fat |
| Student-$t$ ($\nu = 6$) | $\nu = 6$ | 3 | Fat |
| Student-$t$ ($\nu = 4$) | $\nu \to 4^+$ | $\to \infty$ | Very heavy |
| GED ($\nu = 1.5$) | $\nu = 1.5$ | — | Fat |
| GED ($\nu = 1$, Laplace) | $\nu = 1$ | 3 | Fat |

**Likelihood ratio test** of $\zeta = 0$ (normality) vs $\zeta > 0$ (Student-$t$ tails):

$$LR = -2\left(\ell_{\text{normal}} - \ell_{t}\right) \sim \chi^2_1 \text{ under } H_0$$

For S&P 100 data: $LR = 257$, far exceeding the $\chi^2_1$ critical value of 3.84 at the 5% level.

## Example

Suppose a GARCH(1,1) model is fitted to daily S&P 500 returns, and the estimated degrees of freedom are $\hat{\nu} = 6$.

**Kurtosis of standardised residuals:**

$$\text{Kurt}[z_t] = 3 + \frac{6}{6 - 4} = 3 + 3 = 6$$

This is double the normal kurtosis of 3, indicating substantially heavier tails.

**Effect on 99% VaR** (one-day, for $\sigma_t = 1\%$):

- Normal: $\text{VaR} = 2.326 \times 1\% = 2.33\%$
- Student-$t_6$: critical value $\approx 3.143$, so $\text{VaR} = 3.143 \times 1\% = 3.14\%$

The Student-$t$ model increases the VaR estimate by roughly 35% — a material difference for capital allocation.

If instead $\hat{\nu} = 4.1$ (near the boundary):

$$\text{Kurt}[z_t] = 3 + \frac{6}{4.1 - 4} = 3 + 60 = 63$$

The kurtosis is enormous; the distribution has extremely heavy tails and variance only barely exists.

## Remember

When fitting GARCH to equity return data, always test the Student-$t$ innovation against the normal using the likelihood ratio test. An LR statistic of 257 (as observed for the S&P 100) is overwhelming evidence against normality — the $p$-value is effectively zero. A normal GARCH model will systematically understate tail VaR and Expected Shortfall because it assigns far too little probability to large standardised shocks. For risk management, this is not a minor modelling nuance: it translates directly into inadequate capital buffers and underpriced tail-risk hedges. The Student-$t$ or GED GARCH is the industry standard precisely because it matches the empirical kurtosis of standardised residuals that plain GARCH leaves unexplained.
