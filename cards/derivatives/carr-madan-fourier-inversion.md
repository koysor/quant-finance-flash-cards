# Carr–Madan Fourier Inversion

**Topic:** Derivatives
**Tags:** Carr-Madan, Fourier inversion, characteristic function, Gil-Pelaez, option pricing, dampening factor
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Carr–Madan (1999) shows that any European option price can be expressed as a Fourier transform of the model's characteristic function; a damping factor $e^{\alpha k}$ makes the call payoff square-integrable in log-strike, enabling fast numerical pricing via FFT.

## Key Formula

Let $k = \ln K$ (log-strike), $x_T = \ln S_T$ (log-price), and $\phi(u) = \mathbb{E}[e^{iux_T}]$ the risk-neutral characteristic function. The damped call price is:

$$z_T(k) = e^{\alpha k}\,C_T(k) = \frac{e^{-rT}}{\pi}\int_0^\infty e^{iuk}\,\Psi(u)\,du$$

where the modified integrand is:

$$\Psi(u) = \frac{\phi\bigl(u - (\alpha+1)i\bigr)}{\alpha^2 + \alpha - u^2 + i(2\alpha+1)u}$$

**Why damping?** $C_T(k) \to S_0$ as $k \to -\infty$ (deep ITM call $\approx S_0$), so $C_T$ is not in $L^2(\mathbb{R})$ and has no Fourier transform. Multiplying by $e^{\alpha k}$ ($\alpha > 0$) forces $z_T \to 0$ as $k \to -\infty$, making the transform valid.

**Admissible $\alpha$:** need $\phi(-i(\alpha+1))$ finite, i.e. $\mathbb{E}[S_T^{\alpha+1}] < \infty$. For Black–Scholes this holds for all $\alpha > 0$; for Heston, $\alpha < \bar\alpha$ where $\bar\alpha$ depends on parameters.

## Example

Pricing a 1-year ATM call on $S_0 = 100$, $r = 5\%$, under Black–Scholes with $\sigma = 20\%$: set $\alpha = 1.5$ (safe for BS), discretise $u \in [0, 2048\Delta u]$ with $\Delta u = 0.25$, apply FFT to $e^{iuk}\Psi(u)$ weights, recover $z_T(k)$, then divide by $e^{\alpha k}$ to get $C_T(k)$ for all $k$ simultaneously. One FFT call of $N = 4096$ points prices the full strike grid in $O(N\log N)$ operations — vs $N$ separate integrations without FFT.

## Remember

The Carr–Madan result transformed derivative pricing: any model with an analytic characteristic function — Heston, Bates, VG, NIG, Lévy processes — immediately inherits a fast calibration routine at no extra mathematical cost. The insight is that the *characteristic function* is the universal pricing object: it encodes the full distribution of $\ln S_T$, and the Fourier pairing between log-strike and log-price space turns a cross-sectional calibration to 50+ strikes from an $O(N^2)$ problem into an $O(N\log N)$ one. This is why model builders now routinely derive $\phi(u)$ first and treat the option pricing formula as a corollary.
