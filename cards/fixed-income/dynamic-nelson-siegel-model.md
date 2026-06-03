# Dynamic Nelson-Siegel Model

**Topic:** Fixed Income
**Tags:** dynamic nelson-siegel, dns, yield curve forecasting, var, term premium, state space
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Dynamic Nelson-Siegel (DNS) model extends the static Nelson-Siegel framework by treating the level, slope, and curvature factors as time-varying state variables following a VAR(1) process, enabling yield curve forecasting and the formal decomposition of yields into expected future short rates and a term premium.

## Key Formula

The yield loading is unchanged from static Nelson-Siegel:

$$y_t(\tau) = \beta_{1t} + \beta_{2t}\frac{1-e^{-\lambda\tau}}{\lambda\tau} + \beta_{3t}\!\left(\frac{1-e^{-\lambda\tau}}{\lambda\tau} - e^{-\lambda\tau}\right)$$

The factor dynamics evolve as a VAR(1):

$$\mathbf{f}_t = \boldsymbol{\mu} + A(\mathbf{f}_{t-1} - \boldsymbol{\mu}) + \boldsymbol{\varepsilon}_t, \qquad \boldsymbol{\varepsilon}_t \sim \mathcal{N}(0, Q)$$

where $\mathbf{f}_t = (\beta_{1t}, \beta_{2t}, \beta_{3t})^\top$. The $h$-step yield curve forecast is:

$$\mathbb{E}_t[\mathbf{f}_{t+h}] = \boldsymbol{\mu} + A^h(\mathbf{f}_t - \boldsymbol{\mu})$$

## Example

US Treasury DNS: $\boldsymbol{\mu} = (4.0\%, -0.5\%, 0.8\%)^\top$, $A = \text{diag}(0.97, 0.94, 0.88)$. Current factors: $(3.8\%, -1.2\%, 0.9\%)^\top$. Six-month forecast for the level factor: $4.0\% + 0.97^6(3.8\% - 4.0\%) = 3.83\%$. The slope factor mean-reverts faster: $-0.5\% + 0.94^6(-1.2\% - (-0.5\%)) = -0.97\%$. Combining the three factor forecasts yields the full predicted yield curve, enabling a 10-year yield forecast of 4.1%.

## Remember

The DNS model is the primary tool used by central banks and academic economists to decompose bond yields into two economically distinct components: the expected path of future short rates (reflecting monetary policy expectations) and the term premium (compensation for bearing duration risk). When the Federal Reserve raises rates, DNS lets economists determine how much of the resulting long-yield rise was priced-in rate expectations versus a shift in risk appetite — a distinction that is invisible in raw yield data but crucial for monetary policy communication.
