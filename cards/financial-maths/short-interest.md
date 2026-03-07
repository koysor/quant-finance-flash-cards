# Short Interest

**Topic:** Financial Mathematics
**Tags:** short interest, short selling, sentiment, days to cover, short ratio
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Short interest is the total number of shares of a security that have been sold short and not yet covered (bought back). It serves as a measure of bearish sentiment — high short interest indicates that many investors are betting on a price decline.

## Key Formula

The **short interest ratio** (days to cover) measures how long it would take all short sellers to close their positions:

$$\text{Days to Cover} = \frac{\text{Short Interest}}{\text{Average Daily Volume}}$$

The **short interest as a percentage of float** measures the intensity of shorting:

$$\text{SI\%} = \frac{\text{Short Interest}}{\text{Free Float}} \times 100$$

The **utilisation rate** measures how much of the available lending pool is being used:

$$\text{Utilisation} = \frac{\text{Shares on Loan}}{\text{Shares Available to Lend}} \times 100$$

## Example

A stock has 3 million shares sold short, a free float of 20 million shares, and average daily volume of 500,000 shares.

$$\text{Days to Cover} = \frac{3{,}000{,}000}{500{,}000} = 6 \text{ days}$$

$$\text{SI\%} = \frac{3{,}000{,}000}{20{,}000{,}000} \times 100 = 15\%$$

A days-to-cover ratio above 5 and SI% above 10% are widely considered elevated. If positive news arrives, the 6-day covering timeline means short sellers cannot exit quickly, creating conditions for a short squeeze.

## Remember

Short interest data is a valuable input to quantitative trading models. Research shows that heavily shorted stocks underperform on average — short sellers tend to be sophisticated investors whose positions reflect genuine negative information. However, extremely high short interest also creates **squeeze risk**, where forced covering drives prices sharply higher. The relationship is therefore non-linear: moderate short interest is bearish for the stock, but very high short interest can be bullish in the short term due to squeeze dynamics. Regulatory bodies (the SEC in the US, the FCA in the UK) require periodic disclosure of short positions, and this data is published on a biweekly or monthly schedule — a lag that quantitative funds try to overcome using real-time securities lending data.
