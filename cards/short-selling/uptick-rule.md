# Uptick Rule

**Topic:** Short Selling
**Tags:** short selling, regulation, market stability, price, securities law
**Created:** 2026-03-16
**Author:** Claude Sonnet 4.6

---

## Definition

The uptick rule is a financial regulation that restricts short sales to being executed only at a price higher than (or equal to, under the alternative rule) the most recent transaction price, preventing short sellers from continuously driving a falling stock lower by selling into every downtick.

## Key Formula

Under the original **SEC Rule 10a-1** (in force 1938–2007), a short sale was permitted only if the last price change was positive (an uptick):

$$P_{\text{short}} > P_{\text{last trade}}$$

Under the current **Alternative Uptick Rule (SEC Rule 201)**, triggered when a stock falls 10% in a day, short sales are restricted to prices above the current national best bid:

$$P_{\text{short}} > \text{NBB} \quad \text{(on a circuit-breaker day)}$$

$$\% \text{ decline trigger} = \frac{P_{\text{close}} - P_{\text{prev close}}}{P_{\text{prev close}}} \leq -10\%$$

## Example

Stock XYZ closes at £10.00. The next day it falls to £9.00 by mid-morning — a 10% decline — triggering Rule 201. For the rest of that day and the following day, short sellers may only sell at prices strictly above the national best bid. If the bid is £9.00, any short order must be placed at £9.01 or higher, preventing aggressive downtick shorting.

## Remember

The uptick rule is a practical constraint that quants must incorporate into execution models: a strategy that assumes unlimited short selling at any price will over-estimate profits during a sharp downturn. The circuit-breaker structure of Rule 201 means that volatility itself triggers the restriction, linking execution feasibility directly to the volatility regime.
