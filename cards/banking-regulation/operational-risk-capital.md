# Operational Risk Capital

**Topic:** Banking Regulation
**Tags:** operational risk, sma, ama, loss data, business indicator
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Operational risk capital is the regulatory capital banks must hold against losses from inadequate or failed internal processes, people, systems, or external events — covering rogue trading, IT failures, fraud, mis-selling, and legal losses. Basel IV replaced the previous suite of approaches (Basic Indicator, Standardised, Advanced Measurement Approach) with a single Standardised Measurement Approach (SMA) for all banks, removing the ability to use internal loss models.

## Key Formula

The Basel IV SMA capital requirement is:

$$\text{ORC} = BIC \times ILM$$

**Business Indicator Component (BIC):** A formula applied to the Business Indicator (BI), which is the sum of Interest, Lease and Dividend income; Services income; and Financial income:

$$BIC = \begin{cases} 0.12 \times BI & BI \leq €1\text{bn} \\ €0.12\text{bn} + 0.15(BI - 1) & €1\text{bn} < BI \leq €30\text{bn} \\ €4.47\text{bn} + 0.18(BI - 30) & BI > €30\text{bn} \end{cases}$$

**Internal Loss Multiplier (ILM):** For banks with $BI > €1$ bn, ILM scales capital by the bank's own 10-year average annual loss (Loss Component, LC):

$$ILM = \ln\!\left(\exp(1) - 1 + \left(\frac{LC}{BIC}\right)^{0.8}\right)$$

## Example

A mid-sized bank has $BI = £5\text{bn}$, giving $BIC = £0.12\text{bn} + 0.15 \times (5-1) = £0.72\text{bn}$. Its average annual operational losses over 10 years are $LC = £0.5\text{bn}$. Since $LC/BIC = 0.69 < 1$, $ILM < 1$, so the bank's good loss history reduces its capital below the pure BIC figure — incentivising robust loss data collection.

## Remember

The SMA's ILM creates a direct financial incentive for banks to collect and report operational loss data accurately: a bank with £500 m in documented annual operational losses faces higher capital than one with £50 m in losses, even if they have the same BI. This is controversial — banks that recognise and report losses transparently are penalised relative to those with poor data — but it aligns with the regulatory intent of making capital sensitive to actual risk experience rather than just income size. For quants, the elimination of AMA means the sophisticated loss-distribution models (frequency-severity convolution, copulas for dependency between loss types) that were central to AMA are no longer required for regulatory capital but remain useful for internal risk management and economic capital.
