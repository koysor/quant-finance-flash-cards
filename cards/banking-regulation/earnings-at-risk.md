# Earnings at Risk

**Topic:** Banking Regulation
**Tags:** EaR, NII, IRRBB, earnings sensitivity, interest rate risk, ALM
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Earnings at Risk (EaR)** is the maximum decline in a bank's net interest income (NII) over a specified horizon (typically 12 months) at a given confidence level, under adverse interest rate movements. It is the income-based counterpart of Value at Risk: while VaR measures potential mark-to-market losses, EaR measures the potential shortfall in accounting earnings due to rate changes.

## Key Formula

Under a simple repricing-gap approach:

$$\text{EaR} = \sum_{i} \text{Gap}_i \times \Delta r_{\text{adverse}}$$

where $\text{Gap}_i$ is the repricing gap in bucket $i$ and $\Delta r_{\text{adverse}}$ is the assumed adverse rate shock.

Under a more sophisticated simulation approach:

$$\text{EaR}_{\alpha} = \text{NII}_{\text{base}} - \text{NII}_{\alpha\text{-percentile}}$$

where $\text{NII}_{\alpha\text{-percentile}}$ is the NII outcome at the $\alpha$-th percentile from a distribution of rate scenarios (e.g. historical simulation or Monte Carlo).

## Example

A bank's base-case NII for the next 12 months is £500m. Under 1,000 simulated rate paths, the 1st-percentile NII outcome is £430m.

$$\text{EaR}_{99\%} = 500 - 430 = \textbf{£70m}$$

There is a 1% probability that NII will fall by more than £70m over the next year due to interest rate movements.

Alternatively, using a simple 200 bps parallel shock and a cumulative repricing gap of +£3bn:

$$\text{EaR} = 3\text{bn} \times 0.02 = \textbf{£60m}$$

## Remember

EaR translates interest rate risk into the language that bank boards and analysts understand — impact on the income statement. While EVE captures the present-value impact on the balance sheet, EaR shows what shareholders will see in reported earnings. The two can diverge: a rising-rate environment might reduce EVE (long-duration assets lose value) but boost near-term NII (more assets reprice higher than liabilities). Banks report EaR under multiple scenarios — parallel shifts, curve steepening, and flattening — as part of their IRRBB disclosure. Regulators view EaR as essential because a sustained earnings decline can erode capital buffers even when EVE appears adequate.
