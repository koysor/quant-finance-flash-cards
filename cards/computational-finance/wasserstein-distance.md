# Wasserstein Distance

**Topic:** Computational Finance
**Tags:** wasserstein distance, optimal transport, earth mover distance, generative model, distribution comparison, scenario generation
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Wasserstein distance** (also called the Earth Mover's Distance, EMD) measures the minimum cost of transforming one probability distribution into another, where cost is the amount of probability mass moved multiplied by the distance moved. Unlike KL divergence, it is a true metric between distributions: it is symmetric, satisfies the triangle inequality, and remains finite even when the distributions have non-overlapping support.

## Key Formula

**$W_p$ distance** between distributions $P$ and $Q$ on $\mathbb{R}^d$:

$$W_p(P, Q) = \left(\inf_{\gamma \in \Gamma(P,Q)} \int_{\mathbb{R}^d \times \mathbb{R}^d} \|x - y\|^p \, d\gamma(x,y)\right)^{1/p}$$

where $\Gamma(P, Q)$ is the set of all joint distributions $\gamma$ with marginals $P$ and $Q$ (transport plans).

**$W_1$ in 1-D** — closed-form via the CDF difference:

$$W_1(P, Q) = \int_{-\infty}^{\infty} |F_P(x) - F_Q(x)| \, dx$$

**Sliced Wasserstein distance** — computationally tractable approximation for high-D:

$$\widetilde{W}_2^2(P, Q) = \int_{\mathcal{S}^{d-1}} W_2^2\!\left(\pi_\theta \# P,\; \pi_\theta \# Q\right) d\theta$$

average $W_2$ between 1-D projections onto random unit vectors $\theta$.

## Example

Two return distributions: $P$ = pre-crisis equity returns (mean $+0.05\%$, vol $1.2\%$), $Q$ = crisis returns (mean $-0.30\%$, vol $3.8\%$). KL divergence $D_{\text{KL}}(P \| Q) = \infty$ if the tails have non-overlapping support. $W_1(P, Q) = 0.35\%$ — the minimum average shift (in return units) to morph one distribution into the other. This finite, interpretable value makes $W_1$ the preferred metric for measuring the distance between historical market regimes in stress testing.

## Remember

KL divergence is the standard loss in VAE training, but Wasserstein distance is the theoretically superior metric for comparing financial return distributions for three reasons: (1) it remains finite when distributions have non-overlapping tails — a common situation during regime transitions; (2) it provides geometrically meaningful distances in return space (units are the same as returns); (3) it is symmetric — $W_1(P, Q) = W_1(Q, P)$ — unlike KL divergence, so scenario distances are commutative. In practice, the Wasserstein GAN (WGAN) replaces the standard GAN discriminator loss with a Wasserstein-1 estimate, improving training stability for generating synthetic financial return paths. For portfolio stress testing, the $W_1$ distance between today's return distribution and historical crisis distributions ranks which past episode is the closest analogue — a more principled approach than selecting by correlation or PCA distance alone.
