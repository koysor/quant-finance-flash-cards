# Liquidity Risk

**Topic:** Risk
**Tags:** liquidity risk, bid-ask spread, market impact, funding, fire sale
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Liquidity risk is the danger that a firm cannot convert assets into cash quickly enough, or at an acceptable price, to meet its obligations. It has two forms: **market liquidity risk** (the cost of selling assets due to wide bid-ask spreads or thin order books) and **funding liquidity risk** (the inability to roll over short-term borrowing such as repos or commercial paper).

## Key Formula

The **liquidity-adjusted VaR** adds a bid-ask spread cost to standard VaR:

$$\text{LVaR} = \text{VaR} + \frac{1}{2} \times \text{Position} \times \overline{S}$$

where $\overline{S}$ is the average proportional bid-ask spread.

The **market impact cost** for a large trade (Almgren-Chriss model):

$$\text{Impact} = \eta \times \sigma \times \sqrt{\frac{Q}{V}}$$

where $\eta$ is the impact coefficient, $\sigma$ is daily volatility, $Q$ is the trade size, and $V$ is average daily volume.

## Example

A fund holds a £20 million position in a mid-cap stock with a 1-day VaR of £800,000. The average bid-ask spread is 0.3%.

$$\text{LVaR} = £800{,}000 + \frac{1}{2} \times £20{,}000{,}000 \times 0.003 = £800{,}000 + £30{,}000 = £830{,}000$$

But if the fund needs to liquidate quickly and the spread widens to 2% in a stressed market:

$$\text{LVaR}_{\text{stress}} = £800{,}000 + £200{,}000 = £1{,}000{,}000$$

The liquidity cost now accounts for 20% of the total risk — and this ignores market impact from actually trading the volume.

## Remember

Liquidity risk is often called the "silent killer" because standard risk models (VaR, expected shortfall) assume positions can be unwound instantly at mid-market prices — an assumption that fails precisely when it matters most. The 2008 crisis showed the lethal interaction between funding and market liquidity: as repo haircuts rose, firms had to deleverage; deleveraging meant selling into illiquid markets; fire sales pushed prices down, eroding collateral values and triggering further margin calls. This **liquidity spiral** (Brunnermeier & Pedersen, 2009) demonstrates that the two forms of liquidity risk are mutually reinforcing. Quantitative risk managers must therefore stress-test both dimensions simultaneously and maintain liquidity buffers that account for regime switches.
