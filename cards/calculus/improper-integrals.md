# Improper Integrals

**Topic:** Calculus
**Tags:** calculus, integration, infinity, convergence, probability
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **improper integral** is a definite integral with at least one infinite limit of integration, or an integrand that becomes unbounded within the integration interval. Because the standard Fundamental Theorem of Calculus requires a closed, bounded interval, improper integrals are evaluated as limits of ordinary definite integrals. The integral **converges** if the limit exists and is finite; otherwise it **diverges**.

## Key Formula

**Infinite upper limit:**

$$\int_a^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx$$

**Both limits infinite:**

$$\int_{-\infty}^{\infty} f(x) \, dx = \lim_{a \to -\infty} \int_a^0 f(x) \, dx + \lim_{b \to \infty} \int_0^b f(x) \, dx$$

**Useful result — exponential decay ($\lambda > 0$):**

$$\int_0^{\infty} e^{-\lambda x} \, dx = \frac{1}{\lambda}$$

**Gaussian integral (fundamental to normal distribution):**

$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$

## Example

Compute the expected payoff of a European call under a simplified model where the terminal stock price $S$ follows an exponential distribution with rate $\lambda = 0.1$, and strike $K = 5$.

$$\mathbb{E}[\max(S - K, 0)] = \int_5^{\infty} (s - 5) \cdot 0.1 \, e^{-0.1s} \, ds$$

Using integration by parts with $u = s - 5$, $dv = 0.1 e^{-0.1s} \, ds$:

$$= \bigl[-(s-5)e^{-0.1s}\bigr]_5^{\infty} + \int_5^{\infty} e^{-0.1s} \, ds = 0 + \bigl[-10 e^{-0.1s}\bigr]_5^{\infty} = 10 e^{-0.5} \approx \textbf{6.07}$$

## Remember

Every continuous probability distribution is normalised by an improper integral: $\int_{-\infty}^{\infty} f(x) \, dx = 1$. In Black-Scholes option pricing, the expected payoff is an improper integral of the form $\int_K^{\infty} (S_T - K) \, \phi(S_T) \, dS_T$ over the risk-neutral density — it converges precisely because the lognormal density decays fast enough in the tail. When a model uses a heavy-tailed distribution (such as a power law), checking whether this integral converges is equivalent to asking whether the option has a finite fair value.
