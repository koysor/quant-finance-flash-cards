# Limits

**Topic:** Calculus
**Tags:** limits, convergence, continuity, derivative definition, option pricing, boundary conditions
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **limit** of a function $f(x)$ as $x$ approaches $a$ is the value $L$ that $f(x)$ gets arbitrarily close to as $x$ gets arbitrarily close to $a$ (without necessarily reaching it). Written $\lim_{x \to a} f(x) = L$. The limit exists if and only if the left-hand limit and right-hand limit both exist and are equal.

## Key Formula

**Formal definition ($\varepsilon$-$\delta$):** $\lim_{x \to a} f(x) = L$ if for every $\varepsilon > 0$ there exists $\delta > 0$ such that:

$$0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$

**One-sided limits:**

$$\lim_{x \to a^-} f(x) = L^- \qquad \text{(from the left)}, \qquad \lim_{x \to a^+} f(x) = L^+ \qquad \text{(from the right)}$$

The two-sided limit exists iff $L^- = L^+$.

**Limit at infinity:**

$$\lim_{x \to \infty} f(x) = L \implies f(x) \to L \text{ as } x \text{ grows without bound}$$

**Derivative as a limit:**

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

## Example

The price of a European call as the underlying $S \to \infty$:

$$\lim_{S \to \infty} C(S, K, T) = S - K e^{-rT}$$

The option behaves like a forward contract — deep in-the-money, the optionality has negligible value and the call price converges to the forward price minus the discounted strike. This limit provides a boundary condition for the Black-Scholes PDE.

Similarly, as time to expiry $T \to 0$:

$$\lim_{T \to 0} C(S, K, T) = \max(S - K,\, 0)$$

The option price collapses to its intrinsic value — a limit that defines the terminal boundary condition.

## Remember

Limits underpin every key concept in calculus: derivatives are limits of difference quotients, integrals are limits of Riemann sums, and continuity is defined in terms of limits. In quantitative finance, limits appear as **boundary conditions** for option pricing PDEs — the behaviour of the option price as $S \to 0$, $S \to \infty$, or $T \to 0$ specifies the edges of the finite-difference grid. Getting the boundary conditions wrong is one of the most common sources of numerical error in PDE-based option pricers.
