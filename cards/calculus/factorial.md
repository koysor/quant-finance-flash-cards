# Factorial

**Topic:** Calculus
**Tags:** factorial, combinatorics, taylor series, binomial theorem, sequences
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The factorial of a non-negative integer $n$, written $n!$, is the product of all positive integers from 1 up to $n$. By convention, $0! = 1$.

## Key Formula

$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1 = \prod_{i=1}^{n} i$$

**Binomial coefficient** (combinations):

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

**Taylor series** uses factorials as denominators to ensure convergence and correct scaling:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$

Special cases:

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}, \qquad \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$

## Example

How many ways can 4 assets be selected (without order) from a portfolio of 10?

$$\binom{10}{4} = \frac{10!}{4!\,6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$$

There are 210 distinct 4-asset subsets.

## Remember

Factorials are the hidden scaffolding of quantitative finance. In the **binomial option pricing model** the coefficient $\binom{n}{k}$ counts exactly how many paths through an $n$-step tree end with $k$ up-moves — it is factorial arithmetic that converts the tree into a probability. In **Taylor series** the $n!$ denominator keeps each successive correction term appropriately small, which is why delta–gamma approximations work for small moves in option pricing and why duration–convexity captures most of a bond's yield sensitivity.
