# Radon–Nikodým Derivative

**Topic:** Stochastic Processes
**Tags:** measure change, risk-neutral, radon-nikodym, density, expectation
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Radon–Nikodým derivative** is the density function $\Lambda = d\mathbb{Q}/d\mathbb{P}$ that converts expectations under one probability measure to expectations under another. It acts as a reweighting factor: to compute an expectation under $\mathbb{Q}$, multiply the integrand by $\Lambda$ and take the expectation under $\mathbb{P}$.

## Key Formula

If $\mathbb{Q} \ll \mathbb{P}$, there exists a non-negative random variable $\Lambda$ such that for any random variable $Y$:

$$E^{\mathbb{Q}}[Y] = E^{\mathbb{P}}[\Lambda \cdot Y], \qquad \Lambda = \frac{d\mathbb{Q}}{d\mathbb{P}}$$

For equivalent measures: $\Lambda > 0$ a.s. and $E^{\mathbb{P}}[\Lambda] = 1$.

In the Brownian setting, $\Lambda$ takes the exponential martingale form:

$$\Lambda_t = \exp\!\left(-\int_0^t \theta_s\,dX_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)$$

## Example

In a one-period model with $\mathbb{P}(\text{up}) = 0.7$ and $\mathbb{Q}(\text{up}) = 0.5$:

$$\Lambda(\text{up}) = \frac{0.5}{0.7} = 0.714, \qquad \Lambda(\text{down}) = \frac{0.5}{0.3} = 1.667$$

Check: $E^{\mathbb{P}}[\Lambda] = 0.7 \times 0.714 + 0.3 \times 1.667 = 0.5 + 0.5 = 1$ ✓

To price a claim paying £20 in the up state: $E^{\mathbb{Q}}[Y] = E^{\mathbb{P}}[\Lambda Y] = 0.7 \times 0.714 \times 20 + 0.3 \times 1.667 \times 0 = £10$.

## Remember

The Radon–Nikodým derivative is the "exchange rate" between probability measures in derivative pricing. When a quant moves from the physical measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$, every expectation is reweighted by $\Lambda$ — bad states (where the market falls) receive higher weight, and good states receive lower weight, reflecting the market price of risk. In continuous time, $\Lambda$ is constructed as an exponential martingale via Girsanov's theorem, and its form determines the relationship between the real-world drift $\mu$ and the risk-free rate $r$.
