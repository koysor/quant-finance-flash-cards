# Optax

**Topic:** Computational Finance
**Tags:** optax, jax, gradient optimisation, composable transforms, adam, deep learning
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Optax** is a JAX-based gradient optimisation library by Google DeepMind that provides composable gradient transformations and standard optimisers (Adam, SGD, RMSprop, and others). Its defining feature is a **functional API**: optimiser state is an explicit, immutable structure returned from `init()`, and gradient updates are computed by pure functions — compatible with JAX's just-in-time compilation and automatic vectorisation.

## Key Formula

The Optax pattern separates three operations: initialise, update, apply.

$$\theta_{t+1} = \theta_t + \Delta\theta_t, \qquad \Delta\theta_t,\, \text{state}_{t+1} = \texttt{tx.update}(\nabla_\theta \mathcal{L},\, \text{state}_t)$$

Transformations are **chained** via `optax.chain(t_1, t_2, \ldots)`, applying each in sequence. Gradient clipping followed by Adam:

```python
tx = optax.chain(
    optax.clip_by_global_norm(1.0),   # clip gradient ℓ₂-norm to 1
    optax.adam(learning_rate=1e-3)    # then Adam update
)
state          = tx.init(params)
updates, state = tx.update(grads, state, params)
params         = optax.apply_updates(params, updates)
```

## Example

Training a TDBP option pricer with 30 daily time steps, each a 2-layer MLP with parameters $\theta_t$. At each backward-induction step:

1. Compute Bellman residual: $\mathcal{L}(\theta_t) = \mathbb{E}[(\hat{P}_t - e^{-r\Delta t}\hat{P}_{t+1})^2]$
2. Compute $g = \nabla_{\theta_t}\mathcal{L}$ via `jax.grad`
3. Apply the chained transformation: clip norm to 1.0, then Adam
4. Update: `params = optax.apply_updates(params, updates)`

Without gradient clipping at step 1, the network parameters are far from the pricing surface and produce large gradients — Adam's momentum term diverges. The `chain` ensures clipping occurs before the Adam moment accumulators are updated, keeping all 30 networks stable from the first training iteration.

## Remember

Optax is the standard optimiser library when implementing finance models in JAX because JAX's `jit` and `vmap` require pure functions — `torch.optim` optimisers hold mutable state inside Python objects and cannot be JIT-compiled. The composable `chain` API is particularly valuable for deep hedging and neural SDE training: a production pipeline might chain learning-rate warm-up, gradient norm clipping, weight decay, and Adam in a single JIT-compiled step, with each component independently swappable for ablation studies. This modularity is harder to achieve with monolithic optimiser objects in PyTorch or TensorFlow.
