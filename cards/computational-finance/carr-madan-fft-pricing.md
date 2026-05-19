# Carr-Madan FFT Pricing

**Topic:** Computational Finance
**Tags:** python, fft, option pricing, characteristic function, heston, vectorised pricing
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Carr-Madan method uses the Fast Fourier Transform (FFT) to price a full strip of European options across all log-strikes simultaneously from a model's characteristic function. It replaces repeated numerical integration (one call per strike) with a single FFT pass, reducing computation from $O(N^2)$ to $O(N \log N)$ and making real-time calibration to the volatility surface tractable.

## Key Formula

For dampened call price $c_T(k) = e^{-\alpha k} C(k)$ at log-strike $k = \ln K$:

$$\psi_T(v) = \frac{e^{-rT} \phi_T(v - (\alpha+1)i)}{\alpha^2 + \alpha - v^2 + i(2\alpha+1)v}$$

$\phi_T$ is the characteristic function, $\alpha > 0$ the damping constant. Call prices at $N$ log-strikes follow from the inverse FFT:

$$C(k_u) = \frac{e^{-\alpha k_u}}{\pi} \text{Re}\!\left[\sum_{j=0}^{N-1} e^{-i \cdot 2\pi jk_u / N} \psi_T(v_j) \Delta v\right]$$

**Python sketch:**

```python
def carr_madan(phi, S, r, T, alpha=1.5, N=4096, eta=0.25):
    v = np.arange(N) * eta
    k = -np.pi / eta + (2 * np.pi / (N * eta)) * np.arange(N)
    psi = np.exp(-r * T) * phi(v - (alpha + 1) * 1j) / (
        alpha**2 + alpha - v**2 + 1j * (2 * alpha + 1) * v
    )
    prices = np.real(np.fft.fft(psi * np.exp(1j * v * k[0]) * eta)) * np.exp(-alpha * k) / np.pi
    return S * np.exp(k), prices
```

## Example

Calibrating the Heston model to 50 market strikes requires 50 `scipy.integrate.quad` calls (~500 ms). With Carr-Madan FFT on $N = 4096$ points, all 4096 strike prices are produced in a single FFT (~2 ms) — a **250× speedup**. The calibration loop can then evaluate the objective function hundreds of times per second, enabling real-time fitting to a live options surface.

## Remember

Carr-Madan is the standard approach in production options systems because calibration requires thousands of objective-function evaluations per second. The key trade-off is **accuracy vs. grid resolution**: a coarser FFT grid ($N = 512$) is faster but misses deep out-of-the-money strikes; a finer grid ($N = 8192$) is slower but prices the full surface. In practice, the FFT output is then re-interpolated using `scipy.interpolate` to query at exact market strikes that fall between grid points.
