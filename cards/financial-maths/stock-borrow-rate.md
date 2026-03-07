# Stock Borrow Rate

**Topic:** Financial Mathematics
**Tags:** stock borrow rate, securities lending, short selling, specialness, cost of carry
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The stock borrow rate (also called the lending fee or "special" rate) is the annualised cost a short seller pays to borrow shares from a lender. It is determined by supply and demand in the securities lending market — stocks that are easy to borrow trade at the "general collateral" rate (typically under 1%), while hard-to-borrow or "special" stocks can command rates of 20% or more.

## Key Formula

The **annualised borrow cost** for a short position held for $t$ days:

$$C_{\text{borrow}} = \text{Market Value} \times r_b \times \frac{t}{360}$$

The **breakeven price decline** required to profit after borrowing costs:

$$\Delta P_{\text{min}} = P_0 \times r_b \times \frac{t}{360}$$

The **effective short return** net of borrow costs:

$$R_{\text{short, net}} = \frac{P_0 - P_t}{P_0} - r_b \times \frac{t}{360}$$

## Example

A trader shorts a "special" stock at £25 with a borrow rate of 15% per annum, planning to hold for 60 days.

$$C_{\text{borrow}} = £25 \times 0.15 \times \frac{60}{360} = £0.625 \text{ per share}$$

The stock must fall by at least £0.625 (2.5%) just to break even. If the stock falls to £22:

$$R_{\text{short, net}} = \frac{25 - 22}{25} - 0.15 \times \frac{60}{360} = 12\% - 2.5\% = 9.5\%$$

The high borrow rate consumes over 20% of the gross profit. For a stock at the general collateral rate of 0.5%, the same trade would cost only £0.02 per share.

## Remember

The stock borrow rate is a crucial friction in quantitative short-selling strategies. Academic research (notably D'Avolio, 2002) shows that stocks with high borrow rates — "specials" — tend to be overvalued and deliver negative subsequent returns, confirming that short-sale constraints allow mispricing to persist. The borrow rate also acts as a natural signal: a rising rate indicates growing demand to short, which often precedes price declines. Quantitative funds must incorporate borrow costs into their alpha models because a stock with strong short-signal alpha may be unprofitable to trade once the lending fee is accounted for.
