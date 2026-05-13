# Utility Function

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** utility function, risk aversion, expected utility, investor preferences, wealth
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

A utility function $U(W)$ maps a level of wealth (or return) to a real number representing the investor's subjective satisfaction, allowing different outcomes to be ranked and compared. Under the **expected utility hypothesis**, a rational investor chooses the portfolio that maximises $\mathbb{E}[U(W)]$ — the probability-weighted average utility across all possible outcomes.

## Key Formula

For a portfolio with random final wealth $W$, the investor maximises:

$$\mathbb{E}[U(W)] = \sum_{s} p_s \, U(W_s) \quad \text{(discrete)}$$

$$\mathbb{E}[U(W)] = \int_{-\infty}^{\infty} U(w) \, f(w) \, dw \quad \text{(continuous)}$$

**Risk aversion** is characterised by a concave utility function: $U''(W) < 0$. The **Arrow-Pratt measure of absolute risk aversion** quantifies the degree of concavity:

$$A(W) = -\frac{U''(W)}{U'(W)}$$

## Example

Suppose an investor has log utility $U(W) = \ln(W)$ and faces two portfolios:
- Portfolio A: pays £120 with certainty, so $U = \ln(120) \approx 4.787$
- Portfolio B: pays £200 with probability 0.5 and £50 with probability 0.5

$$\mathbb{E}[U_B] = 0.5\ln(200) + 0.5\ln(50) = 0.5(5.298) + 0.5(3.912) = 4.605$$

Despite Portfolio B having higher expected wealth ($\mathbb{E}[W_B] = £125 > £120$), the investor prefers A because $4.787 > 4.605$ — a direct consequence of concavity (risk aversion).

## Remember

Every portfolio optimisation framework rests on a utility function assumption. The mean-variance framework is theoretically valid only if either returns are normally distributed or the investor's utility is quadratic — in all other cases, $\mathbb{E}[U(W)]$ depends on higher moments (skewness, kurtosis) that mean-variance ignores. This is why practitioners using non-normal return distributions (e.g. hedge funds with option-like payoffs) sometimes replace mean-variance with utility-based optimisation, using CRRA or CARA utility to capture the true shape of investor preferences.
