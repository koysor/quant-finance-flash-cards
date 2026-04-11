# Random Variable Notation

**Topic:** Mathematical Notation
**Tags:** notation, random variable, realisation, support, measurable function
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **random variable** $X$ is a measurable function from a sample space $\Omega$ to the real line $\mathbb{R}$. The notation distinguishes the random variable itself (a function) from a specific value it takes (a realisation).

| Symbol | Read as | Meaning |
|---|---|---|
| $X, Y, Z$ | "capital X, Y, Z" | Random variables — functions defined on $\Omega$ |
| $x, y, z$ | "lowercase x, y, z" | Realisations — specific values the RV takes |
| $X : \Omega \to \mathbb{R}$ | "X maps omega to the reals" | Formal definition of a random variable as a function |
| $X(\omega)$ | "X of omega" | The value of $X$ at outcome $\omega \in \Omega$ |
| $\mathcal{X}$ or $\text{supp}(X)$ | "support of X" | The set of all values $X$ can take |
| $P(X = x)$ | "probability that X equals x" | Probability that the RV $X$ takes value $x$ |
| $P(X \leq x)$ | "probability that X is at most x" | CDF evaluated at $x$: $F_X(x)$ |
| $X_t$ | "X at time t" | A stochastic process — a random variable for each $t$ |

## Key Formula

**Event defined by a random variable:**

$$\{X \leq x\} = \{\omega \in \Omega : X(\omega) \leq x\}$$

This is the event "the outcome is one where $X$ takes a value $\leq x$" — a subset of $\Omega$.

**Indicator random variable:**

$$\mathbf{1}_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{if } \omega \notin A \end{cases}$$

## Example

Let $X$ = the log-return of an equity over one day. Then $\Omega$ is the set of all possible market scenarios, and for each scenario $\omega$, $X(\omega) = \ln(S_1(\omega)/S_0)$ is a real number. Writing $P(X \leq -0.05)$ means the probability the log-return falls below $-5\%$, corresponding to the set of scenarios $\{\omega : X(\omega) \leq -0.05\} \subseteq \Omega$.

## Remember

The uppercase/lowercase convention — $X$ for the random variable, $x$ for a specific value — is essential for reading probability statements correctly. $P(X \leq x)$ makes sense because $X$ is a function (random) and $x$ is a fixed number; writing $P(x \leq x)$ would be either 0 or 1. In finance, $X$ might represent a future asset price, a portfolio return, or a credit loss — the notation works identically in all cases.
