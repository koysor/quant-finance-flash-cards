# Joint Distribution Notation

**Topic:** Mathematical Notation
**Tags:** notation, joint distribution, marginal, conditional density, bivariate
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Joint distribution notation** describes the simultaneous probabilistic behaviour of two or more random variables. It extends single-variable PDF/PMF notation to multiple dimensions, and gives rise to marginal and conditional distributions.

| Symbol | Read as | Meaning |
|---|---|---|
| $f_{X,Y}(x,y)$ | "joint density of X and Y at (x,y)" | Joint PDF: $P(X \in dx, Y \in dy) = f_{X,Y}(x,y)\,dx\,dy$ |
| $p_{X,Y}(x,y)$ | "joint PMF of X and Y" | $P(X = x, Y = y)$ for discrete RVs |
| $F_{X,Y}(x,y)$ | "joint CDF" | $P(X \leq x, Y \leq y)$ |
| $f_X(x)$ | "marginal density of X" | $\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy$ — integrating out $Y$ |
| $f_{X \mid Y}(x \mid y)$ | "conditional density of X given Y=y" | $f_{X,Y}(x,y) / f_Y(y)$ |
| $f_{X_1,\ldots,X_n}$ | "joint density of $n$ variables" | Multivariate extension |

## Key Formula

**Marginalisation:**

$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy$$

**Factorisation (chain rule):**

$$f_{X,Y}(x,y) = f_{X \mid Y}(x \mid y)\,f_Y(y) = f_{Y \mid X}(y \mid x)\,f_X(x)$$

**Independence test:**

$$X \perp\!\!\!\perp Y \iff f_{X,Y}(x,y) = f_X(x)\,f_Y(y) \quad \text{for all } x, y$$

## Example

Two correlated asset returns $(R_1, R_2) \sim \mathcal{N}_2\!\left(\boldsymbol{\mu}, \boldsymbol{\Sigma}\right)$: the joint density is

$$f_{R_1, R_2}(r_1, r_2) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}} \exp\!\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(r_1-\mu_1)^2}{\sigma_1^2} - \frac{2\rho(r_1-\mu_1)(r_2-\mu_2)}{\sigma_1\sigma_2} + \frac{(r_2-\mu_2)^2}{\sigma_2^2}\right]\right)$$

The marginal $f_{R_1}(r_1)$ is obtained by integrating out $r_2$ — recovering $R_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$.

## Remember

The distinction between joint, marginal, and conditional densities is the core of multivariate probability. In copula modelling — the standard tool for capturing tail dependence in credit portfolios — the joint distribution is written as $f_{X,Y}(x,y) = c(F_X(x), F_Y(y))\,f_X(x)\,f_Y(y)$, where $c$ is the copula density encoding all dependence structure beyond the marginals.
