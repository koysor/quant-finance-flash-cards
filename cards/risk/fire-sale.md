# Fire Sale

**Topic:** Risk
**Tags:** fire sale, forced liquidation, liquidity spiral, systemic risk, contagion
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A fire sale is the forced liquidation of assets at prices significantly below fundamental value, typically driven by margin calls, fund redemptions, or regulatory constraints. Fire sales create negative externalities because the resulting price declines impair other holders of the same or similar assets, triggering further forced selling.

## Key Formula

The **fire sale discount** reflects the deviation from fundamental value:

$$\text{Discount} = \frac{P_{\text{fundamental}} - P_{\text{fire sale}}}{P_{\text{fundamental}}}$$

The **Shleifer–Vishny (1992) price impact** of forced selling:

$$P_{\text{fire sale}} = P_{\text{fundamental}} - \lambda \times Q_{\text{forced}}$$

where $\lambda$ is the illiquidity parameter and $Q_{\text{forced}}$ is the volume of forced sales.

The **contagion multiplier** — selling £1 of assets can destroy more than £1 of total market value:

$$\text{Total Loss} = Q_{\text{forced}} \times \lambda \times N_{\text{holders}}$$

where $N_{\text{holders}}$ is the number of investors holding the same asset who suffer mark-to-market losses.

## Example

A fund receives £50 million in redemptions and must liquidate corporate bond holdings. The bonds have a fundamental value of £50 million but the market is thin.

With an illiquidity parameter of $\lambda = 0.10$ per £10 million sold:

$$P_{\text{fire sale}} = £50\text{m} - 0.10 \times £50\text{m} = £45\text{m}$$

The fund realises only £45 million — a 10% fire sale discount. But 20 other funds hold the same bonds, each marking down their portfolios by £2.5 million:

$$\text{Total contagion loss} = 20 \times £2{,}500{,}000 = £50\text{m}$$

The £50 million forced sale creates £50 million in collateral damage across the system — a 2x contagion multiplier.

## Remember

Fire sales are the primary mechanism through which idiosyncratic shocks become systemic crises. The 2008 financial crisis was, at its core, a cascade of fire sales: subprime losses triggered margin calls, which forced asset sales, which depressed prices, which triggered more margin calls. The Brunnermeier–Pedersen (2009) liquidity spiral model shows that funding liquidity (the ability to borrow) and market liquidity (the ability to sell) are mutually reinforcing — a decline in one causes a decline in the other. For quantitative risk managers, the key insight is that standard risk models assume assets can be sold at current market prices, but during fire sales, the act of selling **is** what moves the price. Stress testing must therefore model the endogenous feedback between forced selling, price impact, and margin erosion.
