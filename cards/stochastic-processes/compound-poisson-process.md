# Compound Poisson Process

**Topic:** Stochastic Processes
**Tags:** compound Poisson, jump process, Poisson, insurance, credit risk, stochastic processes
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **compound Poisson process** is a stochastic process that models the cumulative effect of random-sized jumps arriving at random Poisson times. Each jump has a random magnitude drawn independently from a common distribution, and the number of jumps up to time $t$ follows a Poisson process. Unlike a standard Poisson process — which counts events — the compound version sums their random sizes, making it the natural model for aggregate losses, claim totals, or sudden price moves.

## Key Formula

$$X(t) = \sum_{i=1}^{N(t)} Y_i$$

where:

| Symbol | Meaning |
|---|---|
| $N(t)$ | Poisson process with intensity $\lambda$ (number of jumps by time $t$) |
| $Y_i$ | Independent, identically distributed jump sizes with mean $\mu_Y$ and variance $\sigma_Y^2$ |

**Expected value** (by the law of total expectation):

$$E[X(t)] = \lambda t \, \mu_Y$$

**Variance** (by the law of total variance):

$$\text{Var}[X(t)] = \lambda t \left( \sigma_Y^2 + \mu_Y^2 \right) = \lambda t \, E[Y^2]$$

## Example

An insurer faces claims arriving at $\lambda = 5$ per month, with each claim size averaging $\mu_Y = £20{,}000$ and $\sigma_Y = £8{,}000$. Over one quarter ($t = 3$ months):

$$E[X(3)] = 5 \times 3 \times 20{,}000 = £300{,}000$$

$$\text{Var}[X(3)] = 5 \times 3 \times (8{,}000^2 + 20{,}000^2) = 15 \times 464{,}000{,}000 = 6{,}960{,}000{,}000$$

$$\text{Std Dev} = \sqrt{6.96 \times 10^9} \approx £83{,}426$$

So total claims over the quarter are expected to be £300,000 with a standard deviation of roughly £83,400, giving the insurer a concrete basis for setting reserves.

## Remember

The compound Poisson process is the **jump component** inside Merton's jump-diffusion model — in that setting, $N(t)$ counts the number of sudden price moves and each $Y_i$ is the random jump size. Beyond option pricing, compound Poisson processes are foundational in **credit risk** (modelling aggregate default losses in a loan portfolio), **operational risk** (the loss distribution approach under Basel), and **insurance mathematics** (the classical Cramér–Lundberg ruin model). Whenever you need to model a running total of discrete random events — as opposed to continuous diffusion — a compound Poisson process is the starting point.
