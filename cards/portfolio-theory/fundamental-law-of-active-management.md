# Fundamental Law of Active Management

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** fundamental law, information ratio, information coefficient, breadth, active management
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The Fundamental Law of Active Management, formulated by Richard Grinold in 1989, states that a portfolio manager's information ratio is approximately equal to the information coefficient multiplied by the square root of breadth. It decomposes active management skill into two independent components: **forecast accuracy** (how well the manager predicts returns) and **breadth** (how many independent bets the manager makes per year). The law provides a theoretical framework for understanding why diversified quantitative strategies can outperform concentrated discretionary approaches.

## Key Formula

$$\text{IR} \approx \text{IC} \times \sqrt{BR}$$

where:
- $\text{IR}$ = information ratio (active return divided by tracking error)
- $\text{IC}$ = information coefficient (correlation between forecasted and realised returns)
- $BR$ = breadth (number of independent investment decisions per year)

The **transfer coefficient** (TC) extends the basic law to account for portfolio constraints:

$$\text{IR} \approx \text{TC} \times \text{IC} \times \sqrt{BR}$$

where $\text{TC} \in [0, 1]$ measures how efficiently forecasts are translated into portfolio positions (TC = 1 means no constraints).

## Example

**Discretionary PM:** makes 20 high-conviction bets per year with IC = 0.10 (reasonably skilled):

$$\text{IR} = 0.10 \times \sqrt{20} = 0.10 \times 4.47 = 0.45$$

**Quantitative PM:** makes 500 bets per year with IC = 0.03 (modest edge per trade):

$$\text{IR} = 0.03 \times \sqrt{500} = 0.03 \times 22.36 = 0.67$$

The quant PM achieves a higher IR despite much lower forecast accuracy per bet, because breadth compounds the small edge across many independent decisions. If the quant PM faces portfolio constraints that reduce the transfer coefficient to 0.7:

$$\text{IR} = 0.7 \times 0.03 \times \sqrt{500} = 0.47$$

Constraints erode the advantage significantly.

## Remember

The Fundamental Law explains the structural advantage of quantitative investing: a tiny, consistent edge applied across hundreds of securities can outperform brilliant but infrequent insights. It also reveals why strategy capacity matters — as a fund grows, market impact reduces the effective IC and constraints lower the transfer coefficient, both degrading the IR. The law is the theoretical justification for multi-factor, multi-asset quantitative strategies and explains why firms like AQR and Renaissance Technologies trade thousands of positions with small expected alpha per trade rather than concentrating capital in a few high-conviction bets.
