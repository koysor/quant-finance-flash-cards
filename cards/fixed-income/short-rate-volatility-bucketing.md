# Short-Rate Volatility Bucketing Method

**Topic:** Fixed Income
**Tags:** volatility estimation, bucketing, power law, quadratic variation, short rate, empirical
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **bucketing method** estimates the power-law volatility function $w(r) = \nu r^\beta$ by grouping historical rate changes into buckets by rate level, computing the average squared change within each bucket, then reading off $\beta$ and $\nu$ from a log-log plot. It exploits the fact that quadratic variation $\mathbb{E}[(\delta r)^2]$ converges faster and with less noise than the mean $\mathbb{E}[\delta r]$.

## Key Formula

For $dr = u(r)\,dt + \nu r^\beta\,dW_t$, Itô's lemma gives:

$$\mathbb{E}\!\left[(\delta r)^2\right] \approx \nu^2\,r^{2\beta}\,\delta t$$

Taking logs:

$$\log \mathbb{E}\!\left[(\delta r)^2\right] = \underbrace{\log(\nu^2\delta t)}_{\text{intercept}} + \underbrace{2\beta}_{\text{slope}} \cdot \log r$$

**Procedure:** sort observations by rate level → compute mean squared change per bucket → plot $\log \mathbb{E}[(\delta r)^2]$ vs $\log r$ → read slope $= 2\hat\beta$ and intercept $= \log(\hat\nu^2 \delta t)$.

## Example

From US 1-month LIBOR daily data (1985–1997): the log-log plot is strikingly straight, giving slope $= 2 \times 1.13 = 2.26$ and intercept $\approx \log((0.126)^2 \times 1/252)$. This implies $\hat\beta = 1.13$ and $\hat\nu = 0.126$. The $R^2$ of the fit is very high, confirming the power-law form. The results rule out $\beta = 0$ (Vasicek) and $\beta = 0.5$ (CIR).

## Remember

The bucketing method works because **variance is $O(\delta t)$ while drift is $O(\delta t^2)$** for short time steps: at daily frequency the signal-to-noise ratio for variance estimation is far better than for drift. The slope $2\beta \approx 2.26$ tells us that interest rate volatility scales approximately linearly with the rate level — higher rates are proportionally more volatile. This is closer to a **log-normal** model ($\beta = 1$) than to the CIR square-root model, which has important implications for option pricing and tail risk.
