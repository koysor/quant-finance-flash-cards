# Reynolds Number

**Topic:** Calculus
**Tags:** reynolds number, dimensionless, turbulence, laminar flow, fluid dynamics
**Author:** Claude Sonnet 4.6

---

## Definition

The Reynolds number is a dimensionless ratio comparing inertial forces to viscous forces in a fluid flow, used to predict whether the flow will be smooth and orderly (laminar) or chaotic and unpredictable (turbulent).

## Key Formula

$$Re = \frac{\rho u L}{\mu} = \frac{uL}{\nu}$$

where $\rho$ is fluid density, $u$ is flow speed, $L$ is a characteristic length scale, $\mu$ is dynamic viscosity, and $\nu = \mu/\rho$ is kinematic viscosity. For pipe flow, $Re < 2{,}300$ is laminar; $Re > 4{,}000$ is fully turbulent.

## Example

Water ($\nu = 10^{-6}\,\text{m}^2\text{s}^{-1}$) flowing at $u = 0.5\,\text{m s}^{-1}$ through a pipe of diameter $L = 0.02\,\text{m}$:

$$Re = \frac{0.5 \times 0.02}{10^{-6}} = 10{,}000$$

Since $Re = 10{,}000 > 4{,}000$, the flow is turbulent. Doubling the pipe diameter at the same speed gives $Re = 20{,}000$ — even more turbulent, because a larger length scale amplifies inertial effects relative to viscous damping.

## Remember

The Reynolds number captures a regime transition in a single dimensionless ratio — the same structural idea underpins quantitative finance. Market regimes switch between "laminar" states (low volatility, orderly trending, e.g. 2003–2007) and "turbulent" states (high volatility, erratic reversals, e.g. 2008–2009) much as fluid flow transitions at a critical Reynolds number. Regime-switching models such as Hamilton's hidden Markov model are the finance equivalent: they use a latent state variable to distinguish periods where asset dynamics are fundamentally different, mirroring the laminar-to-turbulent bifurcation.
