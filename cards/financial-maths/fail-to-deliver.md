# Fail-to-Deliver

**Topic:** Financial Mathematics
**Tags:** fail-to-deliver, settlement, short selling, naked shorting, clearing
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A fail-to-deliver (FTD) occurs when a seller does not deliver securities to the buyer by the settlement date (typically T+1 in the US and UK). FTDs can arise from administrative errors, but persistent or large-scale fails are often associated with naked short selling — selling shares without first borrowing them. Regulators monitor FTD data closely because sustained fails can indicate manipulative short selling and undermine market integrity.

## Key Formula

The **FTD rate** for a security on a given day:

$$\text{FTD Rate} = \frac{\text{FTD Shares}}{\text{Total Shares Traded}}$$

The **aggregate cost of fails** to the failing party (who must pay the lending fee but receives no rebate):

$$C_{\text{fail}} = \sum_{d=1}^{D} \text{FTD Shares}_d \times r_{\text{penalty}} \times \frac{1}{365}$$

where $r_{\text{penalty}}$ is the penalty rate imposed by the clearing house and $D$ is the number of days the fail persists.

## Example

A stock trades 2 million shares on a given day, and 15,000 shares fail to deliver:

$$\text{FTD Rate} = \frac{15{,}000}{2{,}000{,}000} = 0.75\%$$

If the clearing house imposes a penalty rate of 3% per annum and the fail persists for 5 days:

$$C_{\text{fail}} = 15{,}000 \times £10 \times 0.03 \times \frac{5}{365} = £4{,}500 \times 0.000411 = £61.64$$

While the direct cost per fail is modest, the SEC's Regulation SHO requires mandatory close-out of threshold securities, forcing the failing party to purchase shares in the open market — which can be far more expensive if the stock has risen.

## Remember

Fail-to-deliver data, published by the SEC and other regulators, is a valuable signal in quantitative finance. Persistently high FTDs indicate that short sellers may be struggling to locate borrows, suggesting heavy bearish positioning. Academic research shows that stocks with high FTD levels tend to have negative abnormal returns in subsequent weeks, as the forced close-out buying creates temporary price support followed by renewed selling pressure. For risk management, monitoring FTDs helps identify securities where settlement risk is elevated and short-side strategies may face unexpected forced covering.
