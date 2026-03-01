# Summation Notation

**Topic:** Mathematical Notation
**Tags:** notation, summation, sigma, series
**Author:** Claude Opus 4.6

---

## Definition

**Summation notation** (sigma notation) provides a compact way to write the sum of a sequence of terms. The Greek letter $\Sigma$ (capital sigma) denotes the operation, with an index variable, lower bound, and upper bound specifying which terms to add.

The general form is:

$$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + \cdots + a_n$$

where $i$ is the **index variable**, $m$ is the **lower bound**, $n$ is the **upper bound**, and $a_i$ is the **general term**.

## Key Formula

**Linearity of summation:**

$$\sum_{i=1}^{n} (c \, a_i + d \, b_i) = c \sum_{i=1}^{n} a_i + d \sum_{i=1}^{n} b_i$$

**Arithmetic series** (sum of first $n$ positive integers):

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

**Geometric series** (finite, with common ratio $r \neq 1$):

$$\sum_{i=0}^{n-1} r^i = \frac{1 - r^n}{1 - r}$$

**Double summation** (order of summation can be swapped when all terms are finite):

$$\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} = \sum_{j=1}^{n} \sum_{i=1}^{m} a_{ij}$$

## Example

A portfolio holds $n$ assets with weights $w_i$ and expected returns $\mu_i$. The portfolio expected return is:

$$E[R_p] = \sum_{i=1}^{n} w_i \, \mu_i$$

For three assets with weights $(0.5, 0.3, 0.2)$ and expected returns $(8\%, 6\%, 4\%)$:

$$E[R_p] = 0.5 \times 8\% + 0.3 \times 6\% + 0.2 \times 4\% = 4\% + 1.8\% + 0.8\% = \textbf{6.6\%}$$

## Remember

- Summation notation underpins discrete expected value $E[X] = \sum x_i P(X = x_i)$, variance $\text{Var}(X) = \sum (x_i - \mu)^2 P(X = x_i)$, and portfolio return calculations.
- Linearity of summation is the discrete foundation for **linearity of expectation** — constants factor out and sums split, regardless of dependence between variables.
- In the continuous limit, $\sum$ becomes $\int$ — Riemann integration is the limit of finite sums as the partition width shrinks to zero.
