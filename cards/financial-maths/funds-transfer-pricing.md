# Funds Transfer Pricing

**Topic:** Financial Mathematics
**Tags:** FTP, transfer pricing, ALM, treasury, NII, cost of funds
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Funds transfer pricing (FTP)** is an internal pricing mechanism used by banks to charge each business unit for the interest rate risk and liquidity cost of the funds it uses or generates. Treasury acts as an internal "bank within the bank": it notionally borrows from deposit-gathering units at the FTP rate and lends to loan-originating units at the FTP rate, ensuring that each unit's profitability reflects the true economic cost of its funding profile rather than the bank's blended average cost.

## Key Formula

The FTP rate for a product with maturity $T$:

$$\text{FTP}(T) = r_{\text{swap}}(T) + \text{LP}(T) + \text{basis spread}$$

where $r_{\text{swap}}(T)$ is the matched-maturity swap rate, $\text{LP}(T)$ is the term liquidity premium, and the basis spread captures any reference rate mismatch.

The **true margin** earned by a lending unit:

$$\text{True margin} = r_{\text{loan}} - \text{FTP}(T)$$

and the **true spread** earned by a deposit unit:

$$\text{True spread} = \text{FTP}(T) - r_{\text{deposit}}$$

## Example

A bank originates a 5-year fixed-rate mortgage at 5.2%. Treasury sets the FTP rate:
- 5-year swap rate: 3.80%
- 5-year liquidity premium: 0.35%
- FTP rate = 3.80% + 0.35% = 4.15%

The lending unit's true margin = 5.20% − 4.15% = **1.05%**. Meanwhile, a savings unit gathers deposits paying 2.50% against the same 5-year FTP of 4.15%, earning a true spread of 4.15% − 2.50% = **1.65%**. Treasury absorbs the residual interest rate risk between the two sides.

## Remember

FTP is the mechanism that makes ALM work at an organisational level — without it, business units have no incentive to consider the duration or liquidity profile of the products they sell. A lending unit that originates 30-year fixed mortgages funded by overnight deposits would appear highly profitable on a simple NII basis, but FTP reveals the true cost by charging the matched-maturity rate. After the 2008 crisis, regulators and industry best practice increasingly required banks to include a liquidity premium component in FTP, ensuring that units relying on short-term wholesale funding bear the cost of that fragile funding model.
