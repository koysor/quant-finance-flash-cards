# Similarity Solutions

**Topic:** Calculus
**Tags:** calculus, PDE, ODE, similarity variable, self-similar, diffusion, Gaussian

---

## Definition

A **similarity solution** is a technique for reducing a partial differential equation (PDE) to an ordinary differential equation (ODE) by introducing a **similarity variable** that combines the independent variables into one.

The method works when the PDE has no intrinsic length or time scale, so its solutions are **self-similar** -- the spatial profile at any time is a rescaled copy of the profile at any other time.

**Procedure:**

1. **Ansatz** -- propose a solution of the form $p(y, t) = t^{a}\, f(\xi)$, where $\xi = y / t^{b}$ is the similarity variable.
2. **Dimensional consistency** -- substitute into the PDE and require that every term has the same power of $t$. This fixes the exponents $a$ and $b$.
3. **Solve the ODE** -- the PDE collapses to an ODE in $f(\xi)$ alone, which is typically simpler (often separable).

## Key Formula

Starting from the diffusion equation $\displaystyle \frac{\partial p}{\partial t} = c^{2}\,\frac{\partial^{2} p}{\partial y^{2}}$, set

$$p(y, t) = t^{a}\, f(\xi), \qquad \xi = \frac{y}{t^{b}}$$

Substituting and matching powers of $t$ gives $b = \tfrac{1}{2}$ (diffusive scaling) and the normalisation constraint gives $a = -\tfrac{1}{2}$. The resulting ODE is

$$f''(\xi) + \frac{\xi}{2c^{2}}\, f'(\xi) + \frac{1}{2c^{2}}\, f(\xi) = 0$$

which is separable with the Gaussian solution

$$f(\xi) = A \exp\!\left(-\frac{\xi^{2}}{4c^{2}}\right)$$

so that the full solution is

$$p(y, t) = \frac{A}{\sqrt{t}}\, \exp\!\left(-\frac{y^{2}}{4c^{2}\,t}\right)$$

## Example

Solve $\dfrac{\partial p}{\partial t} = c^{2}\,\dfrac{\partial^{2} p}{\partial y^{2}}$ with the ansatz $p = t^{a}\,f(\xi)$, $\xi = y/t^{b}$.

**Step 1 -- compute partials.** Using the chain rule:

$$\frac{\partial p}{\partial t} = a\,t^{a-1}\,f - b\,\xi\,t^{a-1}\,f'$$

$$\frac{\partial^{2} p}{\partial y^{2}} = t^{a-2b}\,f''$$

**Step 2 -- match powers of $t$.** The PDE requires $t^{a-1}$ on the left and $t^{a-2b}$ on the right, so $a - 1 = a - 2b$ giving $b = \tfrac{1}{2}$.

**Step 3 -- normalisation.** Requiring $\int_{-\infty}^{\infty} p\,dy = 1$ for all $t$ fixes $a = -\tfrac{1}{2}$ (the $\sqrt{t}$ from the change of variable must cancel $t^{a}$).

**Step 4 -- solve the ODE.** The ODE is first-order in $g = f'$:

$$g' = -\frac{\xi}{2c^{2}}\,g \implies g(\xi) = B\exp\!\left(-\frac{\xi^{2}}{4c^{2}}\right)$$

Integrating and applying boundary conditions yields $f(\xi) = A\exp(-\xi^{2}/(4c^{2}))$.

## Remember

The self-similar structure -- the solution at every time is just a rescaled Gaussian -- reflects the absence of any intrinsic length scale in the diffusion equation. This is precisely why the **transition density** of Brownian motion is Gaussian: the Fokker-Planck equation for a free particle is a diffusion equation, and its similarity solution is the normal distribution $\mathcal{N}(0,\,\sigma^{2}t)$.

In quantitative finance this has two critical consequences:

- The Gaussian transition density is the kernel that underpins all **Black-Scholes pricing**. Every call and put price is ultimately an integral against this self-similar density.
- The $\sqrt{t}$ scaling that falls out of $b = \tfrac{1}{2}$ is why **volatility scales with the square root of time**: $\sigma_{T} = \sigma\sqrt{T}$. This is not an assumption but a direct consequence of the diffusive (self-similar) dynamics of the underlying.
