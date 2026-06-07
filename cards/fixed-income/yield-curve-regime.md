# Yield Curve Regime

**Topic:** Fixed Income
**Tags:** yield curve, recession indicator, 2s10s spread, inverted curve, macro regime, credit cycle
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

A yield curve regime is the prevailing shape of the government bond yield curve — normal (upward-sloping), flat, or inverted (downward-sloping) — which encodes the market's expectation of future short-term interest rates and economic growth. Each regime predicts different average returns for equities, credit, and long-duration bonds, making the yield curve one of the oldest and most reliable macro regime indicators.

## Key Formula

The most widely used regime indicator is the **2s10s spread** (10-year minus 2-year Treasury yield):

$$\text{2s10s} = y_{10} - y_{2}$$

Regime classification:

| 2s10s | Regime | Historical equity return (next 12 months) |
|-------|--------|------------------------------------------|
| $> +50$ bps | Normal (steep) | Strong: avg $+14\%$ p.a. |
| $0$ to $+50$ bps | Flat | Moderate: avg $+7\%$ p.a. |
| $< 0$ bps | Inverted | Weak: avg $+2\%$ p.a.; recession in 12–18 months in 7 of the last 8 inversions |

The **term premium** embedded in long yields is:

$$y_T = \mathbb{E}\!\left[\frac{1}{T}\sum_{t=0}^{T-1} r_{t}^{\text{short}}\right] + \text{TP}_T$$

where $\text{TP}_T$ is the extra yield demanded for holding duration risk over short rolling investments.

## Example

In March 2022, the US 2s10s spread was +30 bps (mildly flat). By July 2022 it had inverted to −22 bps — the first sustained inversion since 2006. Over the next 12 months, S&P 500 returned −7%, while 2-year Treasuries returned +3.5% and long bonds returned −8% (rising rates). A yield-curve regime model rotating from equities to short-duration bonds on inversion would have avoided most of the equity drawdown.

## Remember

The inverted yield curve is the most reliable recession predictor in macroeconomic data, with a typical lead time of 12–18 months. In quantitative multi-asset management, the 2s10s spread is used as a meta-signal: when inverted, reduce equity exposure and increase duration-neutral short-term bond exposure. The mechanism is straightforward — banks borrow short and lend long, so an inverted curve compresses bank net interest margins, reduces credit availability, and slows economic growth. However, the signal requires patience: the 2022 inversion persisted for over 18 months before the recession materialised, requiring a risk management framework that can tolerate prolonged positioning before the regime signal resolves.

