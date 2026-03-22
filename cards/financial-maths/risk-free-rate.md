# Risk-Free Rate

**Topic:** Financial Mathematics
**Tags:** risk-free rate, discounting, time value of money, treasury, benchmark rate
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The risk-free rate $r_f$ is the theoretical rate of return on an investment with zero default risk and zero reinvestment risk. In practice it is proxied by the yield on short-term government securities (e.g. UK gilts, US Treasury bills) or overnight secured rates such as SOFR. The risk-free rate is the foundational building block of asset pricing: it represents the minimum return an investor demands for parting with money today.

## Key Formula

The **present value** of a future cash flow discounted at the risk-free rate:

$$PV = \frac{CF}{(1 + r_f)^t}$$

In continuous time (used throughout derivatives pricing):

$$PV = CF \cdot e^{-r_f \, t}$$

The **risk premium** of any asset is defined relative to the risk-free rate:

$$\text{Risk Premium} = E[r] - r_f$$

## Example

A 3-month UK Treasury bill with face value £10,000 trades at £9,870. The annualised risk-free rate implied is:

$$r_f = \left(\frac{£10{,}000}{£9{,}870} - 1\right) \times \frac{12}{3} = 0.01318 \times 4 = 5.27\%$$

Using this rate, the present value of £50,000 to be received in 2 years:

$$PV = £50{,}000 \times e^{-0.0527 \times 2} = £50{,}000 \times 0.9002 = £45{,}009$$

## Remember

The risk-free rate appears in virtually every pricing model in quantitative finance. It is the discount rate in the Black-Scholes formula, the drift rate under the risk-neutral measure, the denominator in the Sharpe ratio, and the baseline for the Capital Asset Pricing Model. A seemingly small change in $r_f$ propagates through option prices (via rho), bond valuations (via DV01), and portfolio allocation decisions. Understanding that the risk-free rate is a modelling convenience — no asset is truly riskless — is essential for interpreting model outputs and recognising their limitations.
