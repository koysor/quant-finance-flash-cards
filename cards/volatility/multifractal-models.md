# Multifractal Models of Asset Returns

**Topic:** Volatility
**Tags:** multifractal, turbulence, fat tails, volatility clustering, Mandelbrot, scaling
**Author:** Claude Sonnet 4.6

---

## Definition

Multifractal models of asset returns describe financial time series that exhibit self-similar, power-law scaling across multiple timescales — capturing fat tails and volatility clustering that log-normal models miss. The approach was developed by Mandelbrot, drawing on Kolmogorov's cascade theory of turbulence.

## Key Formula

In the Multifractal Model of Asset Returns (MMAR), log-price increments $X(\Delta t)$ satisfy a scaling relation:

$$\mathbb{E}\!\left[|X(\Delta t)|^q\right] \propto (\Delta t)^{\tau(q)+1}$$

where $\tau(q)$ is a nonlinear scaling function. For a log-normal multifractal:

$$\tau(q) = -1 + \lambda q - \frac{\lambda^2}{2}\,q^2$$

The nonlinearity of $\tau(q)$ — its deviation from the linear $(\frac{1}{2}q - 1)$ of standard Brownian motion — is the signature of multifractality.

## Example

For daily S&P 500 returns, the empirical kurtosis is approximately 8–10 (versus 3 for a normal distribution). A multifractal model calibrated to $\lambda^2 = 0.03$ generates a $\tau(q)$ curve that is noticeably concave, reproducing the observed excess kurtosis across horizons from 1 day to 1 year without requiring separate parameters for each horizon. Standard GARCH must be re-estimated at each timescale; the multifractal scaling relation handles all horizons simultaneously.

## Remember

Multifractal models borrow Kolmogorov's energy cascade from fluid turbulence: just as kinetic energy is injected at large scales and cascades down to small scales where viscosity dissipates it, market volatility is driven at macro timescales (economic cycles) and cascades to micro timescales (intraday). This gives financial returns the same self-similar, scale-invariant structure observed in turbulent flows — fat tails, volatility clustering, and long memory — and explains why single-timescale models like Black-Scholes systematically underestimate the probability of extreme moves.
