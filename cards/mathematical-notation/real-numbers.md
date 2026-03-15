# Real Numbers

**Topic:** Mathematical Notation
**Tags:** notation, number sets, real line, domains, functions
**Author:** Claude Sonnet 4.6

---

## Definition

The **real numbers**, denoted $\mathbb{R}$, are the complete ordered field containing all rational numbers (fractions and integers) and all irrational numbers (such as $\sqrt{2}$ and $\pi$). Together they form the continuous real number line, which extends from $-\infty$ to $+\infty$.

The key number sets form a hierarchy:

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

where $\mathbb{N}$ are the natural numbers, $\mathbb{Z}$ the integers, and $\mathbb{Q}$ the rationals.

## Key Formula

**Interval notation** (subsets of $\mathbb{R}$):

$$[a, b] = \{x \in \mathbb{R} : a \leq x \leq b\} \qquad \text{(closed)}$$

$$(a, b) = \{x \in \mathbb{R} : a < x < b\} \qquad \text{(open)}$$

$$[a, \infty) = \{x \in \mathbb{R} : x \geq a\} \qquad \text{(half-open, unbounded)}$$

**Absolute value** (distance from zero):

$$|x| = \begin{cases} x & x \geq 0 \\ -x & x < 0 \end{cases}$$

## Example

A stock price $S_t$ must be non-negative, so its domain is $[0, \infty) \subset \mathbb{R}$. A log-return $r = \ln(S_t / S_0)$, however, can be any real number, so $r \in \mathbb{R} = (-\infty, \infty)$.

If $S_0 = 100$ and $S_t = 90$, then:

$$r = \ln\!\left(\frac{90}{100}\right) = \ln(0.9) \approx -0.105$$

This negative value lies in $\mathbb{R}$ but not in $[0, \infty)$, confirming why log-returns and prices have different domains.

## Remember

Specifying the correct domain from $\mathbb{R}$ is essential in quantitative finance. A **probability density function** is defined on $\mathbb{R}$ (or a subset), integrates to 1, and must be non-negative — so $f: \mathbb{R} \to [0, \infty)$. Confusing the domain of prices ($[0, \infty)$) with the domain of returns ($\mathbb{R}$) is a common modelling error, particularly when applying transformations such as taking logarithms or exponentials.
