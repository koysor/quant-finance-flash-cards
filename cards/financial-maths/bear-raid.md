# Bear Raid

**Topic:** Financial Mathematics
**Tags:** bear raid, short selling, market manipulation, price decline, regulation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A bear raid is a deliberate strategy in which one or more traders aggressively short sell a stock to drive its price down, often while spreading negative sentiment. The aim is to profit from the resulting decline or to trigger stop-loss orders and margin calls among existing holders, creating a cascade of selling that pushes the price even lower. Bear raids are a form of market manipulation and are prohibited under securities law in most jurisdictions.

## Key Formula

The **gross profit** from a coordinated short attack that moves the price from $P_0$ to $P_1 < P_0$:

$$\text{Profit} = Q \times (P_0 - P_1) - C_{\text{borrow}} - C_{\text{impact}}$$

where $Q$ is shares shorted, $C_{\text{borrow}}$ is borrowing cost, and $C_{\text{impact}}$ is market impact cost (the price deterioration caused by the trader's own selling).

The **amplification factor** from triggered stop losses can be modelled as:

$$P_1 = P_0 - \Delta P_{\text{initial}} - \sum_{i=1}^{n} \Delta P_{\text{stop}_i}$$

where $\Delta P_{\text{initial}}$ is the price drop from the raid's selling pressure and $\Delta P_{\text{stop}_i}$ represents the incremental price impact of each triggered stop-loss order.

## Example

A trader shorts 200,000 shares of a thinly traded stock at £8.00. The aggressive selling drops the price to £7.20, which triggers stop-loss orders from other holders, pushing the price to £6.50. The borrow cost is £500 and market impact cost is £1,200:

$$\text{Profit} = 200{,}000 \times (£8.00 - £6.50) - £500 - £1{,}200 = £300{,}000 - £1{,}700 = £298{,}300$$

The £0.70 drop from stop-loss cascades amplified the raider's profit by $200{,}000 \times £0.70 = £140{,}000$ beyond what the initial selling pressure alone would have achieved.

## Remember

Bear raids illustrate why regulators impose rules like the uptick rule and short-sale circuit breakers — these constraints exist to prevent manipulative feedback loops where aggressive selling begets more selling. In quantitative finance, understanding bear raid mechanics is important for market microstructure modelling: the interaction between order flow, stop losses, and margin calls can produce price dislocations far larger than fundamentals justify. Systematic strategies that rely on stop-loss orders or momentum signals are particularly vulnerable to bear raids, as the artificial price decline can trigger real liquidations.
