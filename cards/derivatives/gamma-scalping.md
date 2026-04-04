# Gamma Scalping

**Topic:** Derivatives
**Tags:** gamma scalping, delta hedging, gamma, realised volatility, options trading
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Gamma scalping is a trading strategy in which a trader holds a long option position (long gamma) and repeatedly delta-hedges to lock in profits from large moves in the underlying. Each time the underlying moves significantly, the delta hedge generates a realised profit proportional to gamma, which accumulates over time. The strategy is profitable when the underlying's realised volatility exceeds the implied volatility at which the options were purchased — the gamma profits must outweigh the theta decay paid to maintain the position.

## Key Formula

The instantaneous P&L from a delta-hedged long option position over a small interval $dt$:

$$d\text{P\&L} = \frac{1}{2}\,\Gamma\,S^2\left(\sigma_{\text{realised}}^2 - \sigma_{\text{implied}}^2\right)dt$$

The cumulative gamma P&L from a discrete rebalance when the underlying moves by $\Delta S$:

$$\text{Gamma P\&L} = \frac{1}{2}\,\Gamma\,(\Delta S)^2$$

This is offset by the daily theta cost:

$$\Theta \approx -\frac{1}{2}\,\Gamma\,S^2\,\sigma_{\text{implied}}^2 \times \frac{1}{365}$$

## Example

A trader buys an ATM call on a £100 stock with $\Gamma = 0.03$ and daily $\Theta = -£0.25$. During the day, the stock rises £3 and the trader sells 0.09 shares ($\Gamma \times \Delta S$) to rebalance:

$$\text{Gamma P\&L} = \frac{1}{2} \times 0.03 \times 3^2 = £0.135$$

The stock then falls £2 and the trader buys back shares:

$$\text{Gamma P\&L} = \frac{1}{2} \times 0.03 \times 2^2 = £0.060$$

Total gamma profit: £0.135 + £0.060 = £0.195. After subtracting theta of £0.25, the net day's P&L is $-$£0.055. The stock needed to move slightly more for gamma scalping to break even — realised volatility was below implied.

## Remember

Gamma scalping is the practical implementation of long volatility trading. Market makers who buy options and delta-hedge are effectively betting that the underlying will realise more volatility than the market implied. The break-even condition — realised vol must exceed implied vol — is the same condition that drives the variance risk premium. In quantitative finance, understanding gamma scalping reveals why options are not free insurance: the theta paid by gamma scalpers is the income earned by option sellers, creating the fundamental tension between long and short volatility that drives the entire options market.
