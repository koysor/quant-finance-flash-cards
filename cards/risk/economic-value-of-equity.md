# Economic Value of Equity

**Topic:** Risk
**Tags:** EVE, IRRBB, economic value, present value, banking book, ALM
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Economic Value of Equity (EVE)** is the present value of all banking book assets minus the present value of all banking book liabilities. It represents the net worth of the bank from an economic (mark-to-market) perspective rather than an accounting one. Changes in interest rates alter the discount factors applied to future cash flows, causing EVE to rise or fall — measuring this sensitivity is one of the two core IRRBB metrics required by Basel.

## Key Formula

$$\text{EVE} = \sum_{t} CF_t^{\text{assets}} \cdot d(t) - \sum_{t} CF_t^{\text{liabilities}} \cdot d(t)$$

where $d(t) = e^{-r(t)\,t}$ is the discount factor at tenor $t$.

The sensitivity of EVE to a parallel rate shift $\Delta r$:

$$\Delta\text{EVE} \approx -(\text{Dur}_A \times PV_A - \text{Dur}_L \times PV_L) \times \Delta r$$

where $\text{Dur}_A$ and $\text{Dur}_L$ are the modified durations of assets and liabilities.

This simplifies to:

$$\Delta\text{EVE} \approx -\text{Duration Gap} \times PV_A \times \Delta r$$

## Example

A bank has assets with $PV_A = £20\text{bn}$ and duration 4.5 years, and liabilities with $PV_L = £18\text{bn}$ and duration 1.2 years.

**Current EVE** = £20bn − £18bn = **£2bn**

**Duration gap** = $4.5 - (18/20) \times 1.2 = 4.5 - 1.08 = 3.42$ years

If rates rise by 100 bps:

$$\Delta\text{EVE} \approx -3.42 \times 20\text{bn} \times 0.01 = -£684\text{m}$$

EVE falls from £2bn to approximately £1.32bn — a 34% decline from a 1% rate move.

## Remember

EVE captures the long-run solvency impact of rate changes on the entire banking book, including instruments that never appear at market value on the balance sheet (like fixed-rate loans held to maturity). Basel's outlier test flags a bank if its worst-case EVE decline under prescribed rate shocks exceeds 15% of Tier 1 capital. The key driver of EVE sensitivity is the **duration gap** — the mismatch between asset and liability durations. Banks with positive duration gaps (asset duration exceeds liability duration) lose EVE when rates rise, which is the typical exposure for a traditional lending bank funding long-term mortgages with short-term deposits.
