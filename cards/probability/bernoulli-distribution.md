# Bernoulli Distribution

**Topic:** Probability
**Tags:** Bernoulli, binary outcome, trial, success, failure, indicator variable
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Bernoulli distribution** models a single trial with two outcomes: success (1) with probability $p$ and failure (0) with probability $1-p$. It is the simplest discrete distribution and the building block of the binomial distribution ($n$ independent Bernoulli trials). A Bernoulli random variable is also called an **indicator variable** $\mathbf{1}_A$, which equals 1 if event $A$ occurs.

## Key Formula

$$P(X = 1) = p, \qquad P(X = 0) = 1 - p, \qquad X \sim \text{Bernoulli}(p)$$

$$\mathbb{E}[X] = p, \qquad \text{Var}(X) = p(1-p)$$

**PMF:** $P(X = x) = p^x (1-p)^{1-x}$ for $x \in \{0, 1\}$

**Connection to binomial:** if $X_1, \ldots, X_n \overset{\text{iid}}{\sim} \text{Bernoulli}(p)$ then $\sum_{i=1}^n X_i \sim B(n,p)$.

## Example

A bond either defaults (1) or survives (0) over one year. With annual probability of default $\text{PD} = 0.02$:

$$\mathbb{E}[\text{default}] = 0.02, \qquad \text{Var}(\text{default}) = 0.02 \times 0.98 = 0.0196$$

For a portfolio of 100 independent such bonds, the total defaults $\sim B(100, 0.02)$, expected value = 2, by the Bernoulli building-block argument.

## Remember

The Bernoulli distribution is the **atomic unit of credit risk modelling**. Every obligor in a credit portfolio has a Bernoulli default indicator; the correlation between those indicators — not the marginal PDs — drives portfolio loss tail risk. A key identity: $\mathbb{E}[\mathbf{1}_A] = P(A)$, so expected value of an indicator equals probability. This is used constantly in derivatives pricing: $\mathbb{E}[\mathbf{1}_{S_T > K}] = Q(S_T > K) = N(d_2)$ is exactly the risk-neutral probability that a European call expires in the money.
