# Taylor Series

**Topic:** Calculus
**Level:** A Level Mathematics
**Tags:** calculus, Taylor series, approximation

---

## Definition

A **Taylor series** approximates a smooth function f(x) as an infinite sum of polynomial terms evaluated at a point a. It allows complex functions to be approximated locally using only derivatives.

## Key Formula

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

The **Maclaurin series** is the special case where a = 0:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

$$\ln(1 + x) \approx x - \frac{x^2}{2} + \cdots \quad \text{for small } x$$

## Example

Approximate f(x) = eˣ near x = 0 to second order:

$$e^x \approx 1 + x + \frac{x^2}{2}$$

For x = 0.1: e^0.1 ≈ 1 + 0.1 + 0.005 = **1.105** (exact: 1.10517...)

## Remember

Taylor series are the foundation of:
- **Option Greeks**: Delta is the first-order term, Gamma the second-order term — a Taylor expansion of the option price in ΔS.
- **Duration and Convexity** of bonds: first and second-order sensitivities to yield changes.
- The **two-term approximation** for small changes is used everywhere in quantitative finance:

$$\Delta V \approx \Delta \cdot \Delta S + \tfrac{1}{2} \cdot \Gamma \cdot (\Delta S)^2$$
