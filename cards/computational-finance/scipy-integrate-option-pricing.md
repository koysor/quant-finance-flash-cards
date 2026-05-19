# scipy.integrate for Option Pricing

**Topic:** Computational Finance
**Tags:** python, scipy, numerical integration, characteristic function, heston, option pricing
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

`scipy.integrate` provides numerical quadrature routines that evaluate definite integrals to high precision. In quantitative finance, these are used to price options under models — such as Heston stochastic volatility or the Variance Gamma model — where the option price is expressed as an integral of the characteristic function but has no closed-form antiderivative.

## Key Formula

Under any model with a known characteristic function $\phi(\omega)$, the European call price follows the **Gil-Pelaez inversion formula**:

$$C = S_0 \Pi_1 - K e^{-rT} \Pi_2$$

$$\Pi_j = \frac{1}{2} + \frac{1}{\pi} \int_0^\infty \text{Re}\!\left[\frac{e^{-i\omega \ln K}\, \phi_j(\omega)}{i\omega}\right] d\omega$$

**Python implementation using `quad`:**

```python
from scipy.integrate import quad
import numpy as np

def heston_price(S, K, r, T, kappa, theta, sigma, rho, v0):
    def integrand(omega, j):
        phi = heston_cf(omega, S, r, T, kappa, theta, sigma, rho, v0, j)
        return np.real(np.exp(-1j * omega * np.log(K)) * phi / (1j * omega))

    pi1, _ = quad(integrand, 0, 200, args=(1,))
    pi2, _ = quad(integrand, 0, 200, args=(2,))
    Pi1 = 0.5 + pi1 / np.pi
    Pi2 = 0.5 + pi2 / np.pi
    return S * Pi1 - K * np.exp(-r * T) * Pi2
```

## Example

Price a 1-year at-the-money call under the Heston model with $S=100$, $K=100$, $r=5\%$, $\kappa=2$, $\theta=0.04$, $\sigma=0.3$, $\rho=-0.7$, $v_0=0.04$:

```python
price = heston_price(100, 100, 0.05, 1.0, 2, 0.04, 0.3, -0.7, 0.04)
# price ≈ 9.53
```

`scipy.integrate.quad` evaluates the oscillatory integral to machine precision in milliseconds, whereas a Monte Carlo approach would need $10^5$ paths for similar accuracy.

## Remember

Characteristic-function pricing is the standard technique for stochastic volatility and Lévy models in production derivatives systems. `quad` handles the numerical integration reliably for smooth integrands, but **highly oscillatory integrands** (deep in- or out-of-the-money options) require the `limit` parameter or dedicated oscillatory integrators. Faster production systems replace `quad` with FFT-based methods (Carr-Madan), but `scipy.integrate` is invaluable for prototyping and validating new model implementations.
