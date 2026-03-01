# SDE Standard Form

**Topic:** Stochastic Processes
**Tags:** SDE, standard form, drift, diffusion, stochastic calculus
**Author:** Claude Opus 4.6

---

## Definition

Any stochastic differential equation can be rearranged into **standard form**, which cleanly separates the deterministic and random components:

$$dG = A(G, t)\,dt + B(G, t)\,dW_t$$

where $A(G, t)$ is the **drift** coefficient and $B(G, t)$ is the **diffusion** coefficient. Identifying these two functions is essential for analysing behaviour, classifying models, and applying Itô's lemma or Fokker–Planck equations.

## Key Formula

**Standard form:**

$$dG = \underbrace{A(G, t)}_{\text{drift}}\,dt + \underbrace{B(G, t)}_{\text{diffusion}}\,dW_t$$

**Common models in standard form:**

| Model | Drift $A(S, t)$ | Diffusion $B(S, t)$ |
|---|---|---|
| GBM | $\mu S$ | $\sigma S$ |
| Vasicek | $\nu - \mu S$ | $\sigma$ |
| CIR | $\nu - \mu S$ | $\sigma \sqrt{S}$ |
| BM with drift | $\mu$ | $\sigma$ |

## Example

**Given:** $df + dW_t - dt + 2\mu tf\,dt + 2\sqrt{f}\,dW_t = 0$

**Step 1:** Move everything except $df$ to the right:

$$df = dt - dW_t - 2\mu tf\,dt - 2\sqrt{f}\,dW_t$$

**Step 2:** Collect $dt$ and $dW_t$ terms:

$$df = (1 - 2\mu tf)\,dt + (-1 - 2\sqrt{f})\,dW_t$$

**Result:** drift $A = 1 - 2\mu tf$, diffusion $B = -1 - 2\sqrt{f}$.

Watch for $dS$ appearing on **both sides** — collect and factor first. For example, $dS = (\nu - \mu S)\,dt + \sigma\,dW_t + 4\,dS$ becomes $-3\,dS = (\nu - \mu S)\,dt + \sigma\,dW_t$, so $dS = -\frac{1}{3}(\nu - \mu S)\,dt - \frac{1}{3}\sigma\,dW_t$.

## Remember

- Standard form is the **gateway to analysis**: once you have $A$ and $B$, you can write down the Fokker–Planck equation $\partial_t p = -\partial_x(Ap) + \frac{1}{2}\partial_{xx}(B^2 p)$ for the transition density, or apply Itô's lemma to transform the SDE.
- The diffusion coefficient $B$ determines whether the process can reach zero or go negative — GBM has $B = \sigma S$ (vanishes at zero, so prices stay positive), while Vasicek has $B = \sigma$ (constant, so the rate can go negative).
- Always check for the dependent variable on both sides of the equation before identifying drift and diffusion — a common source of errors in exam problems.
