# Momentum Investor

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** momentum investor, trend following, behavioural finance, herding, relative strength
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

A momentum investor is a market participant who systematically buys assets whose prices have been rising and sells assets whose prices have been falling, on the belief that recent trends will persist. Unlike value investors who seek cheap assets, momentum investors pay no attention to fundamental valuation — they follow price trends, expecting that behavioural biases (underreaction to news, herding, and confirmation bias) will cause winning assets to continue outperforming and losers to continue underperforming over horizons of roughly 3 to 12 months.

## Key Formula

The **relative strength** signal used by momentum investors to rank assets:

$$\text{RS}_i = \frac{P_{i,t}}{P_{i,t-J}} - 1$$

where $J$ is the look-back period (commonly 12 months minus the most recent month). Assets are sorted into quintiles or deciles by RS, and the investor goes long the top group and short the bottom group.

The **expected return** from the momentum tilt, under the Carhart four-factor model:

$$E[R_i] - R_f = \beta_i \lambda_{\text{MKT}} + s_i \lambda_{\text{SMB}} + h_i \lambda_{\text{HML}} + w_i \lambda_{\text{WML}}$$

where $\lambda_{\text{WML}}$ is the momentum factor premium, historically around 6–8% per annum for global equities.

## Example

A momentum investor reviews a universe of 100 FTSE stocks at the end of March. Stock A returned +35% over the prior 11 months (months $t{-}12$ to $t{-}1$); Stock B returned $-$20% over the same period. The investor buys £10,000 of Stock A and shorts £10,000 of Stock B.

Over the next 3 months, Stock A rises a further 8% and Stock B falls another 5%:

$$\text{Long P\&L} = £10{,}000 \times 0.08 = £800$$
$$\text{Short P\&L} = £10{,}000 \times 0.05 = £500$$
$$\text{Total} = £1{,}300 \text{ on zero net capital}$$

The momentum effect persisted — recent winners continued to win and losers continued to lose.

## Remember

Momentum investing is one of the most empirically robust strategies in finance, documented by Jegadeesh and Titman (1993) across decades, geographies, and asset classes. The behavioural explanation is that investors underreact to new information initially, causing prices to drift, and then overreact as herding amplifies the trend. The critical risk for momentum investors is the **momentum crash** — during market recoveries after crises, beaten-down losers snap back violently while winners stall, generating catastrophic losses for the long-short portfolio. Understanding when and why momentum fails (high-volatility regimes, market turning points) is as important as understanding why it works.
