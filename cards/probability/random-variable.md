# Random Variable

**Topic:** Probability
**Tags:** random variable, function, outcome, realisation, probability distribution
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **random variable** $X$ is a function that assigns a numerical value to each outcome of a random experiment. It maps outcomes from the sample space $\Omega$ to the real numbers, turning qualitative events into quantities we can calculate with.

$$X : \Omega \to \mathbb{R}, \qquad \omega \mapsto X(\omega)$$

Random variables come in two types:

| Type | Support | Described by | Example |
|---|---|---|---|
| **Discrete** | Countable set $\{x_1, x_2, \ldots\}$ | PMF $p_X(k) = P(X=k)$ | Number of defaults in a portfolio |
| **Continuous** | Interval or $\mathbb{R}$ | PDF $f_X(x)$ | Tomorrow's asset log-return |

## Key Formula

**Expectation** (the probability-weighted average):

$$E[X] = \begin{cases} \displaystyle\sum_k k\,p_X(k) & \text{discrete} \\[6pt] \displaystyle\int_{-\infty}^{\infty} x\,f_X(x)\,dx & \text{continuous} \end{cases}$$

**Variance** (expected squared deviation from the mean):

$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

## Example

Let $X$ = the daily P&L of a trading desk. The experiment is "observe tomorrow's market"; each possible market scenario $\omega$ produces a P&L figure $X(\omega)$. We never know in advance which $\omega$ will occur, but we can model the distribution of $X$ — say $X \sim \mathcal{N}(\mu, \sigma^2)$ — and compute probabilities such as $P(X < -£1\text{m}) = \Phi((-1\text{m} - \mu)/\sigma)$.

## Remember

The power of random variables is that they reduce every probability problem to real-number arithmetic. Once $X$ has a known distribution, all questions about the experiment — "what is the probability of a large loss?", "what is the average outcome?", "how spread out are outcomes?" — become calculations involving $f_X$, $F_X$, $E[X]$, and $\text{Var}(X)$. Every quantitative finance model — from Black-Scholes to credit risk — is ultimately a statement about the distribution of one or more random variables.
