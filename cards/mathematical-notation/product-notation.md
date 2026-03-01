# Product Notation

**Topic:** Mathematical Notation
**Tags:** notation, product, pi, factorial
**Author:** Claude Opus 4.6

---

## Definition

**Product notation** (pi notation) provides a compact way to write the product of a sequence of terms. The Greek letter $\Pi$ (capital pi) denotes the operation, with an index variable, lower bound, and upper bound specifying which terms to multiply.

The general form is:

$$\prod_{i=m}^{n} a_i = a_m \times a_{m+1} \times \cdots \times a_n$$

where $i$ is the **index variable**, $m$ is the **lower bound**, $n$ is the **upper bound**, and $a_i$ is the **general term**.

## Key Formula

**Factorial** as a product:

$$n! = \prod_{i=1}^{n} i = 1 \times 2 \times \cdots \times n$$

**Binomial coefficient** (using factorials):

$$\binom{n}{k} = \frac{n!}{k!(n-k)!} = \frac{\prod_{i=1}^{n} i}{\left(\prod_{i=1}^{k} i\right)\left(\prod_{i=1}^{n-k} i\right)}$$

**Logarithm converts products to sums:**

$$\log \prod_{i=1}^{n} a_i = \sum_{i=1}^{n} \log a_i$$

**Compound return** over $n$ periods:

$$R_{\text{total}} = \prod_{i=1}^{n} (1 + r_i) - 1$$

## Example

An investment earns returns of $+10\%$, $-5\%$, and $+8\%$ over three consecutive periods. The total compound return is:

$$1 + R_{\text{total}} = \prod_{i=1}^{3} (1 + r_i) = 1.10 \times 0.95 \times 1.08 = \textbf{1.1286}$$

So $R_{\text{total}} = 12.86\%$, which is less than the arithmetic sum $10\% - 5\% + 8\% = 13\%$ due to compounding effects.

## Remember

- Product notation appears in **likelihood functions** $L(\theta) = \prod_{i=1}^{n} f(x_i \mid \theta)$, where independence turns a joint density into a product — taking logs converts this to a sum for easier maximisation.
- The **binomial coefficient** $\binom{n}{k}$ counts paths through a binomial tree with exactly $k$ up-moves, which is central to binomial option pricing.
- The **moment generating function** of independent random variables factorises as $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$, a direct application of product notation.
