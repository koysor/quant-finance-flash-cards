# Forward Guidance

**Topic:** Fixed Income
**Tags:** forward guidance, monetary policy, expectations, yield curve, central bank, rate path
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Forward guidance is a central bank tool that explicitly communicates the intended future path of short-term interest rates, shifting market expectations and thereby moving medium and long-term bond yields without any immediate policy rate change.

## Key Formula

Under rational expectations, the $n$-year yield decomposes as:

$$y_t(n) = \underbrace{\frac{1}{n}\sum_{k=0}^{n-1}\mathbb{E}_t[r_{t+k}]}_{\text{expected short rates}} + \underbrace{tp_t(n)}_{\text{term premium}}$$

Explicit forward guidance that rates will remain at $r_0$ for $m$ additional periods shifts $\mathbb{E}_t[r_{t+k}]$ down for $k \leq m$, reducing $y_t(n)$ for all maturities influenced by that horizon. State-contingent guidance ("until unemployment falls below 6.5%") also reduces the term premium $tp$ by lowering uncertainty about the future rate path.

## Example

ECB March 2016 guidance: rates will remain at or below current levels "well past the horizon of net asset purchases." The 2-year German Bund yield fell 15bp on announcement day. Dynamic Nelson-Siegel decomposition: 12bp from revised rate expectations (markets extended the expected zero-rate period by ~18 months) and 3bp from a reduced term premium (lower rate-path uncertainty). An equivalent 15bp move from an actual rate cut would have required using up scarce policy space.

## Remember

Forward guidance is the central bank's most cost-efficient easing tool because it moves yields through expectations alone, without purchasing assets or cutting rates that may need reversing. For bond traders, this creates a systematic mis-pricing opportunity: when the central bank is more credible than the market believes, the 1–5 year segment of the curve will be priced too cheaply (yields too high) relative to the commitment. Positions that buy this segment profit as the market eventually re-prices the guidance fully — but only if the bank delivers on its commitment.
