# Reciprocal Trigonometric Functions

**Topic:** Calculus
**Tags:** secant, cosecant, cotangent, reciprocal, trigonometry, asymptote, derivatives
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The three **reciprocal trigonometric functions** are defined as the multiplicative inverses of sin, cos, and tan:

$$\sec(\theta) = \frac{1}{\cos(\theta)}, \qquad \csc(\theta) = \frac{1}{\sin(\theta)}, \qquad \cot(\theta) = \frac{1}{\tan(\theta)} = \frac{\cos(\theta)}{\sin(\theta)}$$

Each is undefined where its denominator is zero, creating vertical asymptotes at those points.

## Key Formula

**Derivatives:**

$$\frac{d}{d\theta}\sec(\theta) = \sec(\theta)\tan(\theta)$$

$$\frac{d}{d\theta}\csc(\theta) = -\csc(\theta)\cot(\theta)$$

$$\frac{d}{d\theta}\cot(\theta) = -\csc^2(\theta)$$

**Pythagorean identities** (derived from $\sin^2\theta + \cos^2\theta = 1$):

$$1 + \tan^2(\theta) = \sec^2(\theta)$$

$$1 + \cot^2(\theta) = \csc^2(\theta)$$

**Periods:** $\sec$ and $\csc$ have period $2\pi$; $\cot$ has period $\pi$.

## Example

The identity $\sec^2(\theta) = 1 + \tan^2(\theta)$ is used when differentiating $\arctan$:

$$\frac{d}{dx}\arctan(x) = \frac{1}{1 + x^2} = \frac{1}{\sec^2(\arctan(x))}$$

This arises in the derivation of the normal CDF's relationship to the arctangent, and in evaluating integrals of the form $\int \frac{dx}{1+x^2}$ that appear when computing moments of the Cauchy distribution (a fat-tailed distribution used in heavy-tail modelling).

## Remember

The reciprocal functions appear primarily as intermediate steps in differentiation and integration rather than as end results. The identity $1 + \tan^2\theta = \sec^2\theta$ is the key tool for simplifying derivatives of inverse trig functions — particularly $\arctan$, which appears in the CDF of the Cauchy distribution. In quantitative finance, the Cauchy distribution is the $t$-distribution with one degree of freedom, notable for having no finite mean or variance, and its CDF involves $\arctan$. The $\sec^2$ identity is what makes that CDF differentiable.
