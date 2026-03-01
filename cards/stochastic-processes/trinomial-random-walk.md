# Trinomial Random Walk

**Topic:** Stochastic Processes
**Tags:** random walk, trinomial, discrete, diffusion, Fokker-Planck, option pricing

---

## Definition

The **trinomial random walk** is a discrete-time stochastic process in which a particle (or price) can take one of three actions at each time step: move up by $+\delta y$, stay at the same level, or move down by $-\delta y$. The probabilities are symmetric: $\alpha$ for an upward step, $\alpha$ for a downward step, and $1 - 2\alpha$ for remaining stationary, subject to the constraint $\alpha < \tfrac{1}{2}$ to ensure all probabilities are non-negative.

Because the up and down probabilities are equal, the expected displacement at each step is zero, satisfying the **no-drift condition**. This symmetry makes the trinomial walk a natural discrete approximation to a driftless diffusion process and a stepping stone from the simpler binomial random walk to continuous-time models governed by partial differential equations.

## Key Formula

The position after $n$ steps starting from $y_0$ is:

$$Y_n = y_0 + \delta y \sum_{i=1}^{n} X_i$$

where each increment $X_i$ takes values $\{+1,\, 0,\, -1\}$ with probabilities $\{\alpha,\, 1-2\alpha,\, \alpha\}$.

The mean and variance of a single step are:

$$\mathbb{E}[X_i] = \alpha(+1) + (1-2\alpha)(0) + \alpha(-1) = 0$$

$$\operatorname{Var}(X_i) = 2\alpha$$

After $n$ independent steps (with time step $\delta t$ and total time $t = n\,\delta t$):

$$\operatorname{Var}(Y_n) = 2\alpha\,(\delta y)^2\,n = \frac{2\alpha\,(\delta y)^2}{\delta t}\,t$$

Choosing $\alpha$, $\delta y$, and $\delta t$ so that $\tfrac{2\alpha\,(\delta y)^2}{\delta t} = D$ gives a variance that grows linearly at rate $D$, matching the diffusion coefficient of the continuous limit.

## Example

Set $\alpha = 0.25$, $\delta y = 1$, $\delta t = 1$, and $y_0 = 0$. After $n = 100$ steps:

$$\operatorname{Var}(Y_{100}) = 2 \times 0.25 \times 1^2 \times 100 = 50$$

$$\sigma_{Y_{100}} = \sqrt{50} \approx 7.07$$

The diffusion coefficient is $D = 2 \times 0.25 \times 1^2 / 1 = 0.5$. Comparing with a continuous diffusion over $t = 100$: the variance would be $Dt = 0.5 \times 100 = 50$, confirming the discrete model matches.

If we instead set $\alpha = 0.10$ (more likely to stay put), the variance drops to $2 \times 0.10 \times 100 = 20$, illustrating how $\alpha$ controls the "activity" of the walk without introducing drift.

## Remember

The trinomial random walk is the discrete scaffold behind the **Fokker-Planck equation**. By expanding the transition probabilities in a Taylor series and taking the limit $\delta y, \delta t \to 0$ with $2\alpha\,(\delta y)^2 / \delta t = D$ held constant, the Chapman-Kolmogorov equation for the walk converges to $\partial p / \partial t = \tfrac{D}{2}\,\partial^2 p / \partial y^2$. In quantitative finance this same limiting procedure, applied to asset prices under the risk-neutral measure, produces the **Black-Scholes PDE** and its generalisations. The trinomial tree is also the basis of practical **option pricing lattices** (such as the Kamrad-Ritchken and Boyle models), which add a middle "no-move" node to improve convergence over the standard binomial tree.
