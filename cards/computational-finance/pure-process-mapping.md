# Pure Process Mapping (Y-Process)

**Topic:** Computational Finance
**Tags:** pure process, discrete dividends, corporate events, ivs decomposition, jump removal, calibration
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Pure process mapping** transforms a "jumpy" stock price $S$ — one with known discrete dividends or corporate event drops — into a **pure continuous process** $Y$ that satisfies standard no-arbitrage conditions. Pricing and calibration are performed on $Y$; results are then mapped back to $S$, isolating genuine market dynamics from anticipated mechanical jumps.

## Key Formula

If stock $S$ has known dividends $d_i$ at times $t_i > t$, the pure process at time $t$ is:

$$Y_t = S_t + \sum_{t_i > t} e^{-r(t_i - t)}\,d_i$$

i.e. $Y_t$ equals the stock price plus the **present value of all future dividends**. This removes the anticipated drop from $Y$ so that $Y$ follows a continuous no-arbitrage dynamics. The implied volatility surfaces decompose as:

$$\Sigma_S(K,T) = \Sigma_Y(K,T) + \mathcal{E}(K,T)$$

where $\mathcal{E}$ is a correction term that re-introduces the dividend impact.

## Example

A stock at £100 pays £3 dividends in 30 and 90 days, $r = 5\%$. Today's pure process value is $Y_0 = 100 + 3e^{-0.05 \times 30/365} + 3e^{-0.05 \times 90/365} \approx 105.97$. Calibrating a vol model to $Y$ avoids spurious volatility spikes at ex-dividend dates that would appear if calibrating to raw $S$ prices.

## Remember

Pure process mapping "launders" the price series before RL training: the neural network learns the smooth underlying dynamics of $Y$ without confusing anticipated dividend drops for genuine volatility shocks. The correction term $\mathcal{E}$ re-introduces the dividend impact when mapping prices back to options on $S$, ensuring the calibrated IVS matches market quotes around ex-dividend dates without requiring any modification to the RL training algorithm.
