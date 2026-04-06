# Pareto Distribution

**Topic:** Probability
**Tags:** Pareto, power law, heavy tails, 80-20 rule, extreme value, wealth distribution
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Pareto distribution** is a heavy-tailed, power-law distribution on $[x_m, \infty)$ parameterised by minimum value $x_m > 0$ and tail index $\alpha > 0$. The smaller $\alpha$, the heavier the tail. It formalises the **Pareto principle** (80-20 rule): a small fraction of observations accounts for the majority of the total. The mean only exists for $\alpha > 1$; the variance only for $\alpha > 2$.

## Key Formula

**PDF and CDF:**

$$f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}, \quad F(x) = 1 - \left(\frac{x_m}{x}\right)^\alpha, \quad x \geq x_m$$

**Mean and variance:**

$$\mathbb{E}[X] = \frac{\alpha x_m}{\alpha - 1} \; (\alpha > 1), \qquad \text{Var}(X) = \frac{x_m^2 \alpha}{(\alpha-1)^2(\alpha-2)} \; (\alpha > 2)$$

**Tail probability:** $P(X > x) = (x_m/x)^\alpha$ — decays as a power law, much slower than exponential.

## Example

Operational risk losses above a threshold of £1m follow Pareto with $\alpha = 1.5$, $x_m = 1$.

$$\mathbb{E}[X] = 1.5/(1.5-1) = £3\text{m}, \qquad P(X > 10) = (1/10)^{1.5} \approx 3.2\%$$

For comparison, an exponential with the same mean would give $P(X > 10) \approx e^{-10/3} \approx 3.6 \times 10^{-2}$. The Pareto assigns far more weight to extreme losses.

## Remember

The Pareto distribution is the theoretical model behind the **Generalised Pareto Distribution (GPD)** used in Extreme Value Theory, and directly models **large operational risk losses**, insurance claims, and wealth distributions. The Pareto principle in finance manifests as: a small number of positions drive most of the portfolio's P&L, a small number of counterparties account for most credit exposure, a few operational events cause most of the total loss. Tail index estimation ($\hat{\alpha}$ via Hill estimator) is a core task in EVT-based capital modelling — $\hat{\alpha} < 2$ implies infinite variance and signals extreme model risk.
