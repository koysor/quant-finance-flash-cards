# Areas and Parametric Curves

**Topic:** Calculus
**Tags:** integration, area, parametric, parameter, definite integral, curve
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **area under a parametric curve** $x = f(t)$, $y = g(t)$ is found by converting the integral over $x$ into an integral over the parameter $t$. The substitution $dx = f'(t)\, dt$ transforms the area formula into a $t$-integral, using the parameter limits corresponding to the $x$-range of interest.

## Key Formula

Area under a parametric curve (with $x$ increasing as $t$ increases, so $f'(t) > 0$):

$$A = \int_{t_1}^{t_2} y\, \frac{dx}{dt}\, dt = \int_{t_1}^{t_2} g(t)\, f'(t)\, dt$$

where $t_1$ and $t_2$ correspond to the left and right endpoints of the region.

If $x$ decreases as $t$ increases (i.e. $f'(t) < 0$), the sign of the integral reverses; take the absolute value for the unsigned area.

## Example

Find the area under the parametric curve $x = t^2$, $y = t^3 - t$ for $x$ from $0$ to $4$ (i.e. $t$ from $0$ to $2$).

$dx/dt = 2t$, so:

$$A = \int_0^2 (t^3 - t)(2t)\, dt = \int_0^2 (2t^4 - 2t^2)\, dt = \left[\frac{2t^5}{5} - \frac{2t^3}{3}\right]_0^2 = \frac{64}{5} - \frac{16}{3} = \frac{192 - 80}{15} = \frac{112}{15}$$

## Remember

Areas under parametric curves are computed whenever a financial quantity is expressed through a time-parametrised path rather than a direct formula. In **Monte Carlo pricing**, the expected payoff of a path-dependent option is an average over simulated paths — each path is a parametric curve and the option's value involves integrating the payoff along the path. More directly, the **arc length and area** of the implied volatility smile (plotted as a parametric curve in strike-vol space) are descriptive statistics used in volatility model calibration.
