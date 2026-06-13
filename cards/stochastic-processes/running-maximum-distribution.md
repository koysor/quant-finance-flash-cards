# Running Maximum Distribution

**Topic:** Stochastic Processes
**Tags:** running maximum, reflection principle, barrier options, lookback options, brownian motion, GBM
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **running maximum** of an asset price process is $M_T = \max_{0 \leq t \leq T} S_t$, the highest level the price reaches over the interval $[0, T]$. Its distribution under GBM is derived via the **reflection principle**: any Brownian path that reaches level $b$ by time $T$ can be reflected about $b$ after the first hitting time to produce a bijection with paths that end above $b$, yielding the exact probability that the maximum exceeds any barrier.

## Key Formula

Let $S_t = S_0 \exp(\nu t + \sigma W_t)$ with $\nu = \mu - \tfrac{1}{2}\sigma^2$ (the log-drift). The **distribution of the running maximum** is:

$$\Pr(M_T \geq b) = N\!\left(\frac{\nu T - \ln(b/S_0)}{\sigma\sqrt{T}}\right) + \left(\frac{b}{S_0}\right)^{2\nu/\sigma^2} N\!\left(\frac{-\nu T - \ln(b/S_0)}{\sigma\sqrt{T}}\right)$$

For zero drift ($\nu = 0$), this simplifies to the **reflection principle**:

$$\Pr\!\left(\max_{0 \leq t \leq T} W_t \geq a\right) = 2\,\Pr(W_T \geq a) = 2\,N\!\left(\frac{-a}{\sqrt{T}}\right)$$

The running **minimum** $m_T = \min_{0 \leq t \leq T} S_t$ follows by symmetry: replace $b/S_0$ with $S_0/b$ and flip signs.

**Joint density** of $(S_T, M_T)$ used in closed-form barrier and lookback pricing:

$$f(s, m) = \frac{2(2\ln m - \ln s - \ln S_0)}{m\,\sigma^2 T^{3/2}\sqrt{2\pi}} \exp\!\left(-\frac{(2\ln m - \ln s - \ln S_0 - 2\nu T)^2}{2\sigma^2 T}\right), \quad m \geq \max(s, S_0)$$

## Example

$S_0 = 100$, $\sigma = 25\%$, $r = 5\%$, $T = 1$ year, barrier $b = 120$.

Log-drift: $\nu = 0.05 - \tfrac{1}{2}(0.0625) = 0.01875$.

$$\frac{\ln(b/S_0)}{\sigma\sqrt{T}} = \frac{\ln 1.2}{0.25} = \frac{0.1823}{0.25} = 0.729$$

$$\Pr(M_1 \geq 120) = N(0.01875 - 0.729) + (1.2)^{2 \times 0.01875/0.0625} \cdot N(-0.01875 - 0.729)$$

$$= N(-0.710) + (1.2)^{0.6} \cdot N(-0.748) \approx 0.239 + 1.116 \times 0.227 \approx 0.493$$

So under the physical measure there is a 49.3% chance the stock touches £120 within the year, even though $\Pr(S_1 \geq 120) \approx 20\%$. The running maximum is considerably more likely to exceed the barrier than the terminal price.

## Remember

The gap between $\Pr(M_T \geq b) \approx 49\%$ and $\Pr(S_T \geq b) \approx 20\%$ in the example above is the central pricing insight for **barrier options**: a down-and-out call that knocks out at 80 is much less likely to survive the full year than a trader who only looks at the terminal distribution would expect, because the path makes excursions below 80 with high probability even if it ends above 80. The reflection principle quantifies this gap exactly. It also explains why lookback options are expensive: the floating-strike lookback call pays $S_T - m_T$, and $m_T$ is typically well below $S_0$ because the running minimum almost certainly dips below the starting price at some point during the option's life.
