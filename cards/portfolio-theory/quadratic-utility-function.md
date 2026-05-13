# Quadratic Utility Function

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** utility function, quadratic utility, mean-variance, risk aversion, portfolio optimisation
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

The quadratic utility function models investor preferences as $U(W) = W - \tfrac{b}{2}W^2$ where $b > 0$. It is the only utility form for which expected utility depends **solely** on the mean and variance of wealth — providing the exact theoretical justification for mean-variance portfolio optimisation without requiring any assumption about the shape of the return distribution.

## Key Formula

$$U(W) = W - \frac{b}{2}W^2, \quad b > 0$$

Taking expectations:

$$\mathbb{E}[U(W)] = \mathbb{E}[W] - \frac{b}{2}\mathbb{E}[W^2] = \mu_W - \frac{b}{2}(\sigma_W^2 + \mu_W^2)$$

This confirms $\mathbb{E}[U]$ is a function of $\mu_W$ and $\sigma_W^2$ only — higher moments (skewness, kurtosis) are irrelevant. The **satiation point** — beyond which more wealth reduces utility — occurs at $W^* = 1/b$, since $U'(W) = 1 - bW = 0$ there.

## Example

Let $b = 0.01$, so satiation occurs at $W^* = 100$.

Two portfolios: A gives £80 with certainty; B gives £60 or £100 with equal probability.

- $\mathbb{E}[W_B] = 80$, $\text{Var}(W_B) = 400$

$$\mathbb{E}[U_A] = 80 - \frac{0.01}{2}(80^2) = 80 - 32 = 48$$

$$\mathbb{E}[U_B] = 80 - \frac{0.01}{2}(400 + 80^2) = 80 - 34 = 46$$

Same expected wealth, but the investor strictly prefers A because of the variance penalty — a direct reflection of risk aversion.

## Remember

The quadratic utility function is the theoretical bridge between expected utility theory and Markowitz mean-variance optimisation. In practice it has two well-known limitations: **increasing absolute risk aversion** (IARA) — as wealth grows, the investor becomes proportionally *more* risk averse, which contradicts empirical evidence — and the satiation point, above which the investor prefers less wealth. These drawbacks motivate using CRRA utility (e.g. log or power utility) in models where wealth levels vary widely, while mean-variance methods remain standard in portfolio construction precisely because they are computationally tractable.
