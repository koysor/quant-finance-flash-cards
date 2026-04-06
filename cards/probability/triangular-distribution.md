# Triangular Distribution

**Topic:** Probability
**Tags:** triangular distribution, bounded, three-point estimate, project finance, scenario
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **triangular distribution** is a continuous distribution on $[a, b]$ with a single peak at mode $c$ ($a \leq c \leq b$). It is fully specified by three parameters: minimum $a$, most likely value $c$, and maximum $b$. Unlike the normal distribution, it is bounded and requires no statistical estimation — the parameters are supplied directly as expert judgements. This makes it the simplest distribution for **three-point estimates** in risk and project modelling.

## Key Formula

**PDF:**

$$f(x) = \begin{cases} \dfrac{2(x-a)}{(b-a)(c-a)} & a \leq x \leq c \\[6pt] \dfrac{2(b-x)}{(b-a)(b-c)} & c < x \leq b \end{cases}$$

**Mean and variance:**

$$\mathbb{E}[X] = \frac{a + b + c}{3}, \qquad \text{Var}(X) = \frac{a^2+b^2+c^2 - ab - ac - bc}{18}$$

**CDF:** piecewise quadratic, easily inverted for Monte Carlo simulation.

## Example

A project finance model estimates construction cost: minimum £80m, most likely £100m, maximum £150m.

$$\mathbb{E}[X] = (80+100+150)/3 = £110\text{m}, \qquad \sigma = \sqrt{(6400+10000+22500-8000-12000-15000)/18} = £14.2\text{m}$$

Monte Carlo simulation using 10,000 draws from this triangular distribution estimates the probability of cost exceeding £130m, informing contingency reserves.

## Remember

The triangular distribution is used in **project finance and operational risk** Monte Carlo models when data is limited but expert opinion can bound the range and identify the most likely outcome. The **PERT distribution** (a smooth variation of the triangular) is standard in infrastructure project modelling. In insurance **risk aggregation models** (e.g. Solvency II internal models), triangular distributions are used for risk components where only scenario estimates are available. The key advantage over the uniform distribution is that the mode at $c$ makes the distribution **asymmetric** when $c \neq (a+b)/2$, capturing the typical situation where the worst case is further from the most likely than the best case.
