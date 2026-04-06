# Cover-up Rule

**Topic:** Calculus
**Tags:** calculus, partial fractions, integration, decomposition, rational functions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.5

---

## Definition

The cover-up rule (Heaviside cover-up method) is a shortcut for finding the numerator constants in a partial fraction decomposition of a proper rational function whose denominator has distinct linear factors. For each factor $(x - a)$, the corresponding constant $A$ is found by covering up that factor in the denominator and evaluating the remaining expression at $x = a$.

## Key Formula

Given a proper rational function with distinct linear factors:

$$\frac{N(x)}{(x - a_1)(x - a_2) \cdots (x - a_n)} = \frac{A_1}{x - a_1} + \frac{A_2}{x - a_2} + \cdots + \frac{A_n}{x - a_n}$$

Each constant is found by:

$$A_k = \left.\frac{N(x)}{\prod_{j \neq k}(x - a_j)}\right|_{x = a_k}$$

That is, substitute $x = a_k$ into the original fraction with the factor $(x - a_k)$ removed from the denominator.

## Example

Decompose $\dfrac{1}{(x-1)(x-3)}$ and hence integrate it.

**Finding $A$:** cover up $(x - 1)$ and set $x = 1$:

$$A = \frac{1}{(1 - 3)} = \frac{1}{-2} = -\frac{1}{2}$$

**Finding $B$:** cover up $(x - 3)$ and set $x = 3$:

$$B = \frac{1}{(3 - 1)} = \frac{1}{2}$$

So:

$$\frac{1}{(x-1)(x-3)} = \frac{-1/2}{x-1} + \frac{1/2}{x-3}$$

Integrating:

$$\int \frac{dx}{(x-1)(x-3)} = -\frac{1}{2}\ln|x-1| + \frac{1}{2}\ln|x-3| + C = \frac{1}{2}\ln\!\left|\frac{x-3}{x-1}\right| + C$$

## Remember

Partial fractions decompose rational functions that arise naturally in continuous-time finance. The Laplace transform of a discount factor or bond price is often a rational function of the complex variable $s$; partial fractions resolve it into terms whose inverse transforms are simple exponentials, recovering the time-domain cash-flow structure. The cover-up rule is the fastest way to read off the coefficients by inspection, making it essential when deriving closed-form solutions to interest-rate ODEs or bond pricing equations analytically rather than numerically.
