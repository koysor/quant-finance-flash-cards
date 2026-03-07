# Integral Notation

**Topic:** Mathematical Notation
**Tags:** notation, integration, calculus, bounds, differential
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Integral notation** uses the elongated "S" symbol $\int$ (from Latin *summa*) to denote the accumulation of a quantity over an interval. The notation specifies the integrand (what is being summed), the variable of integration, and optionally the limits.

| Symbol | Read as | Meaning |
|---|---|---|
| $\displaystyle\int_a^b f(x)\,dx$ | "integral from $a$ to $b$ of $f$ of $x$, $dx$" | Definite integral with bounds |
| $\displaystyle\int f(x)\,dx$ | "integral of $f$ of $x$, $dx$" | Indefinite integral (antiderivative) |
| $dx$ | "$dx$" | Infinitesimal width; specifies variable of integration |
| $\displaystyle\int_0^T \!\!\int_0^S f\,dx\,dt$ | "double integral" | Iterated integral over two variables |
| $\displaystyle\oint$ | "contour integral" | Integral around a closed curve |

## Key Formula

**Present value of continuous cash flows** at rate $r$:

$$PV = \int_0^T c(t)\,e^{-rt}\,dt$$

**Expectation of a continuous random variable:**

$$E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx$$

**Itô integral** (stochastic, $dW$ replaces $dx$):

$$I(T) = \int_0^T g(t, X_t)\,dW_t$$

## Example

The present value of a continuous coupon paying £5 per year for 3 years at $r = 4\%$:

$$PV = \int_0^3 5\,e^{-0.04t}\,dt = 5\left[\frac{-e^{-0.04t}}{0.04}\right]_0^3 = 125\left(1 - e^{-0.12}\right) = 125 \times 0.1131 = \text{£}14.13$$

## Remember

The transition from $\int f(x)\,dx$ (ordinary integral) to $\int g(t)\,dW_t$ (Itô integral) is one of the most important notational shifts in quantitative finance. The $dW_t$ signals that the integrator is Brownian motion rather than a smooth variable — and this single change means the integral is a martingale with zero expectation, the Itô correction term appears, and standard calculus rules must be replaced with Itô's lemma. Recognising whether you are looking at $dt$, $dx$, or $dW$ in an integral tells you immediately which set of rules applies.
