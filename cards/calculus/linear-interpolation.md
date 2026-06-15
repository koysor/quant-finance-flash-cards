# Linear Interpolation

**Topic:** Calculus
**Tags:** linear interpolation, interpolation, yield curve, curve construction, approximation
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Linear interpolation** estimates the value of an unknown function at a point between two known data points by assuming the function changes at a constant rate — a straight line — between them.

## Key Formula

Given known values $(x_0, y_0)$ and $(x_1, y_1)$, the interpolated value at $x \in [x_0, x_1]$ is:

$$y = y_0 + \frac{y_1 - y_0}{x_1 - x_0}\,(x - x_0)$$

Equivalently, with weight $w = (x - x_0)/(x_1 - x_0) \in [0, 1]$:

$$y = (1 - w)\,y_0 + w\,y_1$$

Applied across a set of pillar points, linear interpolation produces a **piecewise linear** function — continuous but with kinks at each pillar.

## Example

A yield curve has a 1-year zero rate of 3.50% and a 2-year zero rate of 4.00%. The 18-month (1.5-year) rate is:

$$r_{1.5} = 3.50\% + \frac{4.00\% - 3.50\%}{2 - 1} \times (1.5 - 1) = 3.50\% + 0.25\% = 3.75\%$$

The rate moves linearly from 3.50% to 4.00% over the one-year interval; the 18-month point sits exactly halfway.

## Remember

Linear interpolation is the default curve-building method when no smoother model is specified. Risk systems routinely interpolate spot rates, zero rates, or discount factors between quoted maturities to price instruments at non-standard tenors. The resulting piecewise linear curve has a kink in slope at every pillar date: gamma hedges calculated at off-pillar dates depend sensitively on which adjacent pillars are used, which can generate spurious bucketed DV01s if the pillar grid does not align with the instruments being priced.
