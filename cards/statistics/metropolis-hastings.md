# Metropolis–Hastings Algorithm

**Topic:** Statistics
**Tags:** metropolis-hastings, MCMC, acceptance ratio, detailed balance, Bayesian, sampling
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **Metropolis–Hastings algorithm** is an MCMC method that generates a Markov chain whose stationary distribution equals a target distribution $\pi(x)$ — typically a Bayesian posterior — without requiring $\pi$ to be normalised. At each step a candidate state is drawn from a proposal distribution and accepted or rejected according to an acceptance ratio that enforces detailed balance.

## Key Formula

At step $t$, given current state $x$:

1. Draw proposal $x^* \sim q(x^* \mid x)$.
2. Compute the **acceptance probability**:

$$\alpha(x, x^*) = \min\!\left(1,\; \frac{\pi(x^*)\, q(x \mid x^*)}{\pi(x)\, q(x^* \mid x)}\right)$$

3. Set $x_{t+1} = x^*$ with probability $\alpha$; otherwise set $x_{t+1} = x$.

For a **symmetric** proposal ($q(x \mid x^*) = q(x^* \mid x)$), this simplifies to $\alpha = \min\!\bigl(1,\, \pi(x^*)/\pi(x)\bigr)$ — the original Metropolis rule.

## Example

Suppose $\pi(x) \propto e^{-x^2/2}$ (standard normal, unnormalised) and the proposal is $q(x^* \mid x) = \mathcal{N}(x, 1)$ (symmetric). Starting at $x = 3$, propose $x^* = 3.5$:

$$\alpha = \min\!\left(1,\; \frac{e^{-3.5^2/2}}{e^{-3^2/2}}\right) = e^{-(12.25 - 9)/2} = e^{-1.625} \approx 0.197$$

Accept with probability 19.7%; otherwise stay at $x = 3$. Moves towards the high-density region are always accepted; moves further into the tails are accepted with probability equal to the density ratio.

## Remember

Metropolis–Hastings is the workhorse behind Bayesian calibration of interest rate models. When fitting the Vasicek or CIR model to yield curve data, the posterior of $(\kappa, \theta, \sigma)$ has no closed form — M–H generates samples from it directly. The key insight is that only the **ratio** $\pi(x^*)/\pi(x)$ is needed: the normalising constant (the marginal likelihood, which is notoriously hard to compute) cancels out. This makes M–H applicable even when the posterior is known only up to a proportionality constant.
