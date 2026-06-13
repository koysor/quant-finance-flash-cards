# JAX

**Topic:** Machine Learning
**Tags:** jax, automatic differentiation, jit compilation, vectorisation, deep learning, numpy
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**JAX** is a Python numerical computing library by Google DeepMind that combines a NumPy-compatible array API with four transformations: **`jit`** (just-in-time compilation to XLA for GPU/TPU acceleration), **`grad`** (automatic differentiation), **`vmap`** (vectorisation over batches), and **`pmap`** (parallel execution across devices). Its defining constraint is that all functions must be **pure** — no side effects, no in-place mutation — which enables the compiler to optimise and differentiate them correctly.

## Key Formula

JAX's transformation system is **composable**: each transformation returns a new function with the same signature, so they can be nested freely.

$$\underbrace{\texttt{jit}(\texttt{grad}(f))(x)}_{\text{compile the gradient function}} \qquad \underbrace{\texttt{vmap}(\texttt{grad}(f))(X)}_{\text{batch gradient over all rows of }X}$$

The **`grad`** transform computes $\partial f / \partial x$ via reverse-mode automatic differentiation (backpropagation). The combined transform `jit(vmap(grad(f)))` computes a full Jacobian over a batch of inputs in a single compiled GPU kernel — the pattern used in deep hedging to compute per-path Greeks simultaneously.

```python
import jax
import jax.numpy as jnp

def loss(params, x):
    return jnp.mean((params @ x - 1.0) ** 2)

grad_fn = jax.jit(jax.grad(loss))   # compiled gradient function
g = grad_fn(params, x)              # executes on GPU, returns gradient
```

## Example

Pricing 10,000 European call paths simultaneously with JAX `vmap`:

```python
def bs_call(S, K, r, sigma, T):
    d1 = (jnp.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * jnp.sqrt(T))
    d2 = d1 - sigma * jnp.sqrt(T)
    from jax.scipy.stats import norm
    return S * norm.cdf(d1) - K * jnp.exp(-r * T) * norm.cdf(d2)

batch_price = jax.jit(jax.vmap(bs_call, in_axes=(0, None, None, None, None)))
prices = batch_price(S_array, 100.0, 0.05, 0.2, 1.0)   # shape (10_000,)
```

A vectorised NumPy loop over 10,000 paths takes ~8 ms on CPU. The `jit(vmap(...))` version takes ~0.3 ms on GPU — a 25× speedup with no algorithmic change.

## Remember

JAX is the natural substrate for finance models that require both fast Monte Carlo simulation and exact gradient computation: deep hedging needs $\nabla_\theta \mathcal{L}$ through thousands of simulated paths; neural SDE calibration needs $\partial V / \partial \sigma$ across the vol surface. PyTorch can do both, but JAX's `vmap` eliminates the Python for-loop overhead entirely by compiling the batched operation into a single SIMD kernel. The purity requirement — no mutation — is also a practical benefit: JAX functions are automatically safe to differentiate through, eliminating the class of bugs where PyTorch autograd fails because an in-place tensor operation corrupted the computation graph. For a TDBP pricer running 30 backward-induction steps on 100,000 paths per step, JAX typically reduces wall-clock training time from hours to minutes compared to a pure NumPy implementation.
