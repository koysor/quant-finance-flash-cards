# Navier-Stokes Equation

**Topic:** Calculus
**Tags:** PDE, fluid dynamics, diffusion, viscosity, physics-to-finance
**Author:** Claude Sonnet 4.6

---

## Definition

The Navier-Stokes equations are a system of partial differential equations governing the motion of a viscous, incompressible fluid, expressing conservation of mass and momentum for each infinitesimal fluid element.

## Key Formula

For an incompressible Newtonian fluid with velocity field $\mathbf{u}$, pressure $p$, density $\rho$, and dynamic viscosity $\mu$:

**Continuity (mass conservation):**
$$\nabla \cdot \mathbf{u} = 0$$

**Momentum:**
$$\rho\!\left(\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u}\right) = -\nabla p + \mu\,\nabla^2 \mathbf{u} + \mathbf{f}$$

Left side: mass × acceleration. Right side: pressure gradient, viscous diffusion, and external body forces.

## Example

Steady viscous flow between two parallel plates, driven by a pressure gradient $dp/dx = -100\,\text{Pa m}^{-1}$, plate separation $h = 0.01\,\text{m}$, viscosity $\mu = 0.001\,\text{Pa s}$. The equations reduce to $\mu\,d^2u/dy^2 = dp/dx$, giving the parabolic (Poiseuille) velocity profile:

$$u(y) = \frac{1}{2\mu}\!\left(-\frac{dp}{dx}\right)\!(hy - y^2)$$

Maximum velocity at the centreline ($y = h/2$):

$$u_{\max} = \frac{100 \times (0.01)^2}{8 \times 0.001} = 1.25\,\text{m s}^{-1}$$

## Remember

The viscous diffusion term $\mu\,\nabla^2\mathbf{u}$ is mathematically analogous to the diffusion term $\tfrac{1}{2}\sigma^2 S^2\,\partial^2 V/\partial S^2$ in the Black–Scholes PDE — both are second-order parabolic operators that spread information smoothly across their domain. Via a standard change of variables, Black–Scholes reduces exactly to the classical heat equation, a result fluid-dynamics physicists recognised immediately when they moved to quantitative finance in the 1980s and 1990s. This analogy is why finite-difference methods developed for solving the Navier-Stokes equations transfer directly to numerical option pricing.
