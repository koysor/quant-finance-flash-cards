# Cramér–Lundberg Ruin Model

**Topic:** Stochastic Processes
**Tags:** ruin theory, ruin probability, insurance, compound poisson, surplus process, solvency
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Cramér–Lundberg model** is the classical model of an insurer's surplus: premiums arrive at a constant rate $c$ and insurance claims arrive as a compound Poisson process, causing the surplus $U(t)$ to drift upward between claims and jump downward at each claim. **Ruin** occurs if the surplus ever falls below zero — the insurer cannot pay a claim. The model gives the probability of eventual ruin as a function of the initial surplus $u$ and the system parameters.

## Key Formula

**Surplus process:**

$$U(t) = u + ct - \sum_{i=1}^{N(t)} X_i$$

where $u$ is initial surplus, $c$ is the premium rate, $N(t) \sim \text{Poisson}(\lambda)$ counts claims, and $X_i > 0$ are i.i.d. claim sizes with mean $\mu_X$.

**Net profit condition** (required for ruin probability $< 1$): $c > \lambda\mu_X$, i.e. premiums exceed expected claims per unit time.

**Lundberg exponent** $R > 0$ — the positive root of the **Cramér–Lundberg equation**:

$$\lambda + cR = \lambda\, M_X(R), \qquad M_X(R) = \mathbb{E}[e^{RX}]$$

where $M_X$ is the moment generating function of claim sizes.

**Ruin probability** with initial surplus $u$:

$$\psi(u) = P\!\left(\min_{t \geq 0} U(t) < 0\;\Big|\; U(0) = u\right) \leq e^{-Ru}$$

The **Cramér–Lundberg bound** $\psi(u) \leq e^{-Ru}$ decays exponentially in $u$: the more initial capital an insurer holds, the lower the probability of ever being ruined.

## Example

An insurer receives premiums at rate $c = 12$ per year. Claims arrive at rate $\lambda = 10$ per year, each exponentially distributed with mean $\mu_X = 1$ (so $M_X(R) = 1/(1-R)$ for $R < 1$).

**Net profit condition:** $c = 12 > \lambda\mu_X = 10$ ✓, safety loading $\theta = (c - \lambda\mu_X)/(\lambda\mu_X) = 20\%$.

**Lundberg equation:** $10 + 12R = 10/(1-R)$. Solving: $12R(1-R) = 10R$, so $12(1-R) = 10$, giving $R = 1/6 \approx 0.167$.

**Ruin probability bound** with initial surplus $u = 10$:

$$\psi(10) \leq e^{-10/6} = e^{-1.667} \approx 18.9\%$$

For exponential claims the bound is exact: $\psi(u) = \frac{\lambda\mu_X}{c}\,e^{-Ru} = \frac{10}{12}\,e^{-u/6}$.

With $u = 30$: $\psi(30) = 0.833 \times e^{-5} \approx 0.56\%$ — tripling the initial capital reduces ruin probability by a factor of 34.

## Remember

The Cramér–Lundberg model is the mathematical foundation of **insurance solvency regulation**: Solvency II and the Swiss Solvency Test both require insurers to hold enough capital that ruin probability over a one-year horizon does not exceed 0.5% (a 1-in-200 year event). The Lundberg exponent $R$ plays the same role as the Sharpe ratio in portfolio theory — it is the single number that summarises the insurer's safety margin, combining premium loading, claim frequency, and claim severity into one figure. Practitioners extend the basic model to incorporate **reinsurance** (which modifies the claim size distribution), **stochastic premiums**, and **correlated claims** (relevant to natural catastrophe risk), but the exponential decay structure $\psi(u) \approx C\,e^{-Ru}$ survives in approximate form under all these extensions.
