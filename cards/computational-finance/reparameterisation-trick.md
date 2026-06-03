# Reparameterisation Trick

**Topic:** Computational Finance
**Tags:** reparameterisation, gradient estimation, neural sde, variational autoencoder, stochastic node, backpropagation
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **reparameterisation trick** makes stochastic sampling differentiable by re-expressing a random variable $z \sim p(z;\theta)$ as a deterministic function of $\theta$ and a noise variable $\varepsilon$ whose distribution does not depend on $\theta$. This allows gradients to flow through the sampling operation, enabling backpropagation through stochastic nodes in Neural SDEs, VAEs, and stochastic policy networks.

## Key Formula

For $z \sim \mathcal{N}(\mu_\theta, \sigma_\theta^2)$, the reparameterisation is:

$$z = \mu_\theta + \sigma_\theta\,\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, 1)$$

This converts the gradient identity from a problematic form (gradient of an expectation) to a tractable one:

$$\frac{\partial}{\partial\theta}\,\mathbb{E}_{z \sim p(z;\theta)}\!\left[f(z)\right] = \mathbb{E}_{\varepsilon \sim \mathcal{N}(0,1)}\!\left[\frac{\partial f(\mu_\theta + \sigma_\theta\varepsilon)}{\partial\theta}\right]$$

The expectation on the right has no $\theta$-dependence inside $p(\varepsilon)$, so the gradient passes through to $f$.

## Example

A Neural SDE generates a price path $S_t = S_{t-1}\exp(\mu_\theta\,\Delta t + \sigma_\phi\,\varepsilon_t\sqrt{\Delta t})$ with $\varepsilon_t \sim \mathcal{N}(0,1)$. To train $\theta, \phi$ to match observed returns, we need $\partial \mathcal{L}/\partial\theta$ through the sample $S_t$. Without reparameterisation, $S_t$ is a random draw and the gradient is undefined. With reparameterisation, $S_t$ is a deterministic function of the fixed noise draw $\varepsilon_t$, so the chain rule applies and the gradient flows back to $\mu_\theta$ and $\sigma_\phi$ normally.

## Remember

Without the reparameterisation trick, training Neural SDEs or VAEs would require high-variance REINFORCE-style gradient estimators — the signal-to-noise ratio is too low for stable learning. Reparameterisation reduces gradient variance by orders of magnitude by converting the stochastic computation into a deterministic one with external noise. In quantitative finance, this is why Neural SDEs trained on option price data can learn realistic volatility dynamics: each simulated path is differentiable with respect to the network weights, making the training objective a standard smooth minimisation problem.
