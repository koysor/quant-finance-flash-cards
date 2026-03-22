# Deposit Beta

**Topic:** Financial Mathematics
**Tags:** deposit beta, pass-through rate, NMD, IRRBB, repricing, regression
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Deposit beta** is the regression coefficient measuring how much a bank's deposit rate changes in response to a unit change in the benchmark policy rate. A deposit beta of 0.40 means that for every 100 basis points the central bank raises rates, the bank increases its deposit rate by 40 basis points. Deposit beta is the econometric formalisation of the pass-through rate concept and is the key input for modelling the repricing behaviour of non-maturity deposits in IRRBB frameworks.

## Key Formula

The deposit beta is estimated by regressing deposit rate changes on policy rate changes:

$$\Delta r_{\text{dep},t} = \alpha + \beta \times \Delta r_{\text{policy},t} + \varepsilon_t$$

where $\beta$ is the deposit beta, $\alpha$ captures any autonomous drift, and $\varepsilon_t$ is the error term.

The **effective duration** of an NMD portfolio depends on beta:

$$D_{\text{NMD}} \approx \frac{1 - \beta}{\lambda_c} \times w_{\text{core}}$$

where $\lambda_c$ is the core balance decay rate and $w_{\text{core}}$ is the core deposit fraction. Lower beta implies longer effective duration.

## Example

A bank estimates deposit beta from 5 years of monthly data. The central bank raised rates by a cumulative 400 bps over 18 months, and the bank's savings rate increased by 160 bps.

- Crude beta estimate: 160 / 400 = **0.40**
- Regression estimate (accounting for lags): $\beta = 0.45$ with a 3-month lag

With $\beta = 0.45$, a further 100 bps rate rise would increase deposit costs by approximately 45 bps, leaving 55 bps of additional NII for the bank. On a £25bn deposit book, this is worth £25bn × 0.55% = **£137.5m** per year.

## Remember

Deposit beta is asymmetric and non-linear — it tends to be lower in rising-rate environments (banks are slow to raise deposit rates) and higher in falling-rate environments (banks cut deposit rates quickly to protect margins). This asymmetry is a source of franchise value for banks but creates model risk in IRRBB measurement. During the 2022–2023 hiking cycle, UK and US banks initially enjoyed deposit betas as low as 0.20–0.30, but competitive pressure and regulatory scrutiny pushed betas toward 0.50–0.60 over time. Regulators increasingly require banks to justify their beta assumptions with historical evidence segmented by product type, customer segment, and rate cycle — a single aggregate beta is insufficient for robust IRRBB modelling.
