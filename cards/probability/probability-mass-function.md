# Probability Mass Function

**Topic:** Probability
**Tags:** PMF, discrete distribution, probability mass, support, discrete random variable
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **probability mass function (PMF)** of a discrete random variable $X$ assigns a probability to each value in its support. It is the discrete analogue of the PDF: where the PDF gives a density that must be integrated, the PMF gives an exact probability at every point.

$$p_X(k) = P(X = k), \qquad k \in \text{supp}(X)$$

## Key Formula

**PMF properties:**

$$p_X(k) \geq 0 \quad \text{for all } k, \qquad \sum_{k \in \text{supp}(X)} p_X(k) = 1$$

**CDF from PMF** (summing up to a threshold):

$$F_X(x) = P(X \leq x) = \sum_{k \leq x} p_X(k)$$

**Expectation and variance from PMF:**

$$E[X] = \sum_k k\, p_X(k), \qquad \text{Var}(X) = \sum_k (k - E[X])^2\, p_X(k)$$

**PMF vs PDF contrast:**

| | PMF $p_X(k)$ | PDF $f_X(x)$ |
|---|---|---|
| RV type | Discrete | Continuous |
| Point probability | $P(X = k) = p_X(k)$ | $P(X = x) = 0$ |
| Probability of interval | $P(a \leq X \leq b) = \sum_{k=a}^{b} p_X(k)$ | $P(a \leq X \leq b) = \int_a^b f_X(x)\,dx$ |
| Values | In $[0, 1]$ | Non-negative, can exceed 1 |
| Normalisation | Sums to 1 | Integrates to 1 |

## Example

**Binomial$(n=4,\, p=0.25)$:** number of up-moves in a 4-step binomial tree.

$$p_X(k) = \binom{4}{k}(0.25)^k(0.75)^{4-k}, \quad k \in \{0,1,2,3,4\}$$

| $k$ | $p_X(k)$ | $F_X(k)$ |
|---|---|---|
| 0 | 0.3164 | 0.3164 |
| 1 | 0.4219 | 0.7383 |
| 2 | 0.2109 | 0.9492 |
| 3 | 0.0469 | 0.9961 |
| 4 | 0.0039 | 1.0000 |

With $n=4$ steps and $p=0.25$ (risk-neutral up probability), the stock reaches the top node with probability only 0.39%.

## Remember

The PMF is the complete specification of a discrete distribution — knowing $p_X(k)$ for all $k$ tells you everything about $X$. In the binomial option pricing model, the PMF of the number of up-moves directly determines the probability of each terminal price node, and the option price is $E[e^{-rT}\max(S_T - K, 0)]$ computed as a weighted sum over those probabilities. This makes the PMF the bridge between the tree geometry and the pricing formula.
