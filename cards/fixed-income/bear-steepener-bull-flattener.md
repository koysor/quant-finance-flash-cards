# Bear Steepener and Bull Flattener

**Topic:** Fixed Income
**Tags:** bear steepener, bull flattener, yield curve, 2s10s spread, curve trading, monetary policy
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A **bear steepener** occurs when long-term yields rise faster than short-term yields, widening the 2s10s spread; a **bull flattener** occurs when long-term yields fall faster than short-term yields, narrowing the spread. Both are yield curve trading strategies as well as descriptions of macro regimes.

## Key Formula

The 2s10s spread change decomposes as:

$$\Delta(y_{10} - y_{2}) = \underbrace{(\Delta y_{10} - \Delta y_{2})}_{\text{slope change}}$$

Four canonical curve moves:
| Move | Short rates | Long rates | Spread | Macro regime |
|---|---|---|---|---|
| Bear steepener | Rise slowly | Rise fast | Widens | QT, term premium repricing |
| Bear flattener | Rise fast | Rise slowly | Narrows | Tightening cycle start |
| Bull steepener | Fall fast | Fall slowly | Widens | Rate cuts priced in |
| Bull flattener | Fall slowly | Fall fast | Narrows | Recession / flight to safety |

A curve-steepening trade is long the 2-year and short the 10-year (duration-neutral); a flattening trade is the reverse.

## Example

US 2022 tightening cycle: bear flattener from January to July (2-year yield rose from 0.7% to 3.1%, 10-year from 1.5% to 3.0%, spread compressed from +80bp to -10bp). Then bear steepener in Q3 2023 (2-year stuck at 5%, 10-year rose from 3.8% to 5.0% as QT term premium repriced), widening the inversion from -90bp to -20bp. A trader long 10-year, short 2-year (steepener) would have profited +70bp per unit of duration in Q3 2023.

## Remember

The distinction between bull/bear and flattener/steepener tells you which end of the curve is driving the move — the macro signal. A **bear flattener** means the central bank is hiking aggressively (short rates lead); a **bull flattener** means a growth scare (long rates fall, short rates sticky). For yield curve traders, the key is identifying the driving force: Taylor Rule tightening pushes bear flatteners, while recession risk produces bull flatteners and eventually bull steepeners as the market prices rate cuts. Getting the direction right but the driver wrong means the wrong DV01 hedge.
