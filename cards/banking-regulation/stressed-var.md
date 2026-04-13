# Stressed VaR

**Topic:** Banking Regulation
**Tags:** stressed var, svar, market risk capital, stress testing, basel 2.5
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Stressed VaR (SVaR) is a market risk capital measure introduced under Basel 2.5 (2011) that requires banks to recalculate their VaR model using a continuous 12-month historical window calibrated to a period of significant financial stress — specifically one that would have caused large losses for the bank's current portfolio. SVaR was designed to make market risk capital counter-cyclical: by anchoring to a stress period, capital does not collapse in calm markets only to be woefully insufficient when crises hit.

## Key Formula

The total market risk capital requirement under Basel 2.5 is:

$$\text{MRC} = \max(VaR_{t-1},\; m_c \cdot \overline{VaR}_{60}) + \max(SVaR_{t-1},\; m_s \cdot \overline{SVaR}_{60})$$

where $m_c, m_s \geq 3$ are multipliers set by the regulator (increased for VaR backtesting exceptions), and the averages are over the previous 60 trading days.

The stress period is identified by finding the 12-month rolling window that maximises SVaR for the current portfolio:

$$\text{Stress period} = \underset{[t_0, t_0+1\text{yr}]}{\arg\max}\; VaR_{\text{current portfolio}}([t_0, t_0+1\text{yr}])$$

## Example

A bank uses 2008–2009 as its SVaR stress window (peak GFC). Its current-period 10-day 99% VaR is £50 m. Recalculating over the 2008–09 window, SVaR = £180 m. With multipliers $m_c = m_s = 3$ and 60-day averages equal to the current values:

$$\text{MRC} = 3 \times £50\text{m} + 3 \times £180\text{m} = £150\text{m} + £540\text{m} = £690\text{m}$$

Without SVaR, the requirement would be only £150 m — SVaR increases market risk capital by 4.6 times.

## Remember

SVaR was a direct response to the 2008 observation that banks' VaR models, calibrated to the calm pre-crisis period, produced capital requirements of £50–100 m that bore no resemblance to the billions in actual trading losses incurred. By requiring capital to reflect a stress scenario rather than recent history, SVaR forces banks to maintain higher capital buffers even in tranquil markets. Under FRTB (Basel IV market risk), SVaR is replaced by a single Expected Shortfall measure calibrated directly to stressed conditions, addressing the discontinuity between calm-period ES and a separately computed SVaR.
