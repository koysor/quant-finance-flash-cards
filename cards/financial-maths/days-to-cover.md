# Days to Cover

**Topic:** Financial Mathematics
**Tags:** short selling, short interest, liquidity, market sentiment, short squeeze
**Created:** 2026-03-16
**Author:** Claude Sonnet 4.6

---

## Definition

Days to cover (also called the short interest ratio) measures how many days of average trading volume it would take for all short sellers to buy back (cover) their positions. It is a liquidity-adjusted measure of short-selling pressure and a key indicator of short squeeze risk.

## Key Formula

$$\text{Days to Cover} = \frac{\text{Total Short Interest}}{\text{Average Daily Volume (ADV)}}$$

where **Total Short Interest** is the total number of shares currently sold short, and **ADV** is typically the 30-day average daily trading volume.

The **short interest as a percentage of float** is a related metric:

$$\text{Short Interest \%} = \frac{\text{Total Short Interest}}{\text{Float}} \times 100$$

## Example

A stock has 50 million shares sold short and an ADV of 5 million shares:

$$\text{Days to Cover} = \frac{50{,}000{,}000}{5{,}000{,}000} = 10 \text{ days}$$

If positive news causes the stock to rise sharply, all short sellers must buy 50 million shares — but there are only 5 million shares traded on an average day. The rush to cover over 10 days of volume creates a self-reinforcing price spike: a short squeeze.

## Remember

Days to cover is a key input to short squeeze risk models. A value above 5–10 is typically considered elevated. Quantitative traders monitor this metric alongside stock borrow rates to assess the cost and risk of maintaining a short position — a high days-to-cover combined with a rising price is a classic warning sign to cut a short.
