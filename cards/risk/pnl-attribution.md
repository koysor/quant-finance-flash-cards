# P&L Attribution

**Topic:** Risk
**Level:** A Level Mathematics
**Tags:** P&L attribution, risk explain, Greeks, trading desk, daily P&L
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

P&L attribution (also called P&L explain or risk attribution) decomposes the daily profit and loss of a trading book into contributions from each risk factor — equity moves, interest rate changes, volatility shifts, time decay, and so on. Using the portfolio's Greek sensitivities, each component of P&L is attributed to a specific market move, making it possible to verify that the P&L is consistent with the known risk exposures and to identify any unexplained residual.

## Key Formula

The **daily P&L explain** for a derivatives portfolio:

$$\Delta V \approx \underbrace{\delta \cdot \Delta S}_{\text{delta P\&L}} + \underbrace{\frac{1}{2} \Gamma \cdot (\Delta S)^2}_{\text{gamma P\&L}} + \underbrace{\nu \cdot \Delta \sigma}_{\text{vega P\&L}} + \underbrace{\Theta \cdot \Delta t}_{\text{theta P\&L}} + \underbrace{\rho \cdot \Delta r}_{\text{rho P\&L}} + \underbrace{\epsilon}_{\text{unexplained}}$$

The **unexplained P&L** is:

$$\epsilon = \Delta V_{\text{actual}} - \Delta V_{\text{explained}}$$

A well-attributed book has $|\epsilon| / |\Delta V_{\text{actual}}| < 5\%$.

## Example

A derivatives desk holds options on a stock. Overnight:

| Greek | Value | Market move | P&L contribution |
|-------|-------|------------|-----------------|
| Delta ($\delta$) | £50,000 | $\Delta S = +£2$ | £100,000 |
| Gamma ($\Gamma$) | £3,000 | $(\Delta S)^2 = 4$ | £6,000 |
| Vega ($\nu$) | £20,000 | $\Delta \sigma = -0.5\%$ | $-£10,000$ |
| Theta ($\Theta$) | $-£8,000$ | $\Delta t = 1/252$ | $-£8,000$ |

$$\Delta V_{\text{explained}} = £100{,}000 + £6{,}000 - £10{,}000 - £8{,}000 = £88{,}000$$

Actual P&L from the risk system: £90,500. Unexplained: £2,500 (2.8% of actual), which is acceptable and likely due to higher-order Greeks or cross-gamma effects.

## Remember

P&L attribution is a daily ritual on every trading desk and one of the first production systems a quant developer builds or maintains. The unexplained P&L is the most watched number — a large unexplained signals either a model error, a booking mistake, or a missing risk factor. Regulators (under FRTB) require banks to perform P&L attribution tests to validate that internal models capture the risk factors driving actual P&L. For hedge funds, P&L attribution enables the PM to understand exactly why the book made or lost money, decomposing performance into deliberate bets (alpha) and unintended exposures (basis risk, residual Greeks). A clean P&L explain is the hallmark of a well-managed trading book.
