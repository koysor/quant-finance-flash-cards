# Collective Risk Model

**Topic:** Stochastic Processes
**Tags:** collective risk model, aggregate claims, compound poisson, actuarial, insurance, stop-loss
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **collective risk model** (also called the **aggregate claims model**) describes the total losses $S$ incurred by an insurance portfolio over a fixed period as the sum of a random number $N$ of individual claim amounts $X_i$:

$$S = X_1 + X_2 + \cdots + X_N$$

where $N$ (claim count) and $X_i$ (individual claim sizes) are mutually independent. When $N \sim \operatorname{Poisson}(\lambda)$, $S$ follows a **compound Poisson distribution**. The model is the foundation of insurance ratemaking, reserving, and the pricing of stop-loss reinsurance contracts.

## Key Formula

**Mean and variance of aggregate claims:**

$$E[S] = E[N]\cdot E[X], \qquad \operatorname{Var}(S) = E[N]\cdot\operatorname{Var}(X) + \operatorname{Var}(N)\cdot(E[X])^2$$

For the compound Poisson case ($N \sim \operatorname{Poisson}(\lambda)$, so $\operatorname{Var}(N) = E[N] = \lambda$):

$$E[S] = \lambda\mu_X, \qquad \operatorname{Var}(S) = \lambda E[X^2]$$

**Moment generating function** (compound Poisson):

$$M_S(t) = \exp\!\left(\lambda(M_X(t) - 1)\right)$$

**Normal approximation** for large portfolios ($n$ policies, each with Poisson$(\lambda)$ claims):

$$S \approx N\!\left(n\lambda\mu_X,\; n\lambda E[X^2]\right)$$

**Stop-loss premium** (insurer pays excess above retention $d$):

$$\Pi_{\text{stop-loss}} = E[\max(S - d, 0)] = \int_d^\infty (s - d)\,f_S(s)\,ds$$

## Example

A motor insurer has $n = 1{,}000$ policyholders. Each policyholder makes claims at Poisson rate $\lambda = 0.15$ per year. Individual claims $X \sim \operatorname{Exp}(\mu_X = \pounds2{,}000)$ so $E[X^2] = 2\mu_X^2 = 8{,}000{,}000$.

$$E[S] = 1{,}000 \times 0.15 \times 2{,}000 = \pounds300{,}000$$

$$\operatorname{Var}(S) = 1{,}000 \times 0.15 \times 8{,}000{,}000 = 1.2 \times 10^9$$

$$\sigma_S = \pounds34{,}641$$

Using the normal approximation, the 99.5% VaR (Solvency II standard):

$$\operatorname{VaR}_{99.5\%}(S) \approx E[S] + 2.576\,\sigma_S = 300{,}000 + 2.576 \times 34{,}641 \approx \pounds389{,}200$$

So the insurer needs approximately \$89,200 in capital above expected claims to meet Solvency II requirements.

## Remember

The collective risk model is the **actuarial analogue of portfolio loss distribution models** in banking. The aggregate claims $S$ plays the same role as portfolio credit losses: $E[S]$ is the expected loss (covered by premiums), and $\operatorname{VaR}_{99.5\%}(S) - E[S]$ is the unexpected loss (covered by capital). The compound Poisson MGF $M_S(t) = \exp(\lambda(M_X(t)-1))$ is the same function that appears in the **Cramér–Lundberg exponent**: the Lundberg coefficient $R$ solves $M_S(R) = e^{cR/\lambda}$, connecting aggregate claims to the insurer's ruin probability. In practice, actuaries fit the claim count distribution (Poisson, negative binomial) and claim size distribution (lognormal, Pareto for heavy tails) separately, then combine them via simulation or Panjer recursion to obtain the full aggregate claims distribution for pricing stop-loss reinsurance.
