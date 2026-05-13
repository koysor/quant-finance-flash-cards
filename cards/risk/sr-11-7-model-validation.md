# SR 11-7 Model Validation Framework

**Topic:** Risk
**Tags:** model validation, SR 11-7, model governance, backtesting, model inventory, regulatory
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**SR 11-7** is the Federal Reserve's 2011 supervisory guidance on model risk management, defining a model as "a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories to transform input data into quantitative estimates." It mandates independent validation of all models used in decision-making and has become the global industry standard for model governance.

## Key Formula

SR 11-7 does not prescribe a single formula but requires **P&L attribution** as a core validation test. A model passes if its predicted P&L $\hat{P}$ tracks actual P&L $P$ within tolerance:

$$\text{Unexplained P\&L} = P - \hat{P}, \qquad \text{must satisfy}\; \frac{\text{Var}(\text{Unexplained})}{\text{Var}(P)} < \delta$$

where $\delta$ is an institution-specific threshold (typically 10–20% of total P&L variance under FRTB).

## Example

A bank's VaR model predicts daily losses of up to $\$2.5\text{m}$ at 99% confidence. Backtesting over 250 trading days reveals 6 breaches (days where actual loss exceeded the VaR). Under SR 11-7 validation, 6 breaches at 99% confidence in 250 days is in the "red zone" (expected ≤2.5 breaches) — the model must be re-examined. The validation team reviews assumptions (normal returns, constant correlations) and either recalibrates the model or applies a model risk add-on to capital.

## Remember

SR 11-7 introduced four pillars that are now standard across all major financial regulators globally: (1) **model development** — documented assumptions and limitations; (2) **independent validation** — a team separate from the model developers must challenge every model; (3) **model inventory** — all models must be registered with ratings (low/medium/high risk); (4) **ongoing monitoring** — performance metrics tracked continuously with periodic revalidation. In practice, SR 11-7 compliance is why large banks have dedicated model risk management teams of dozens of quants whose sole job is reviewing and challenging models built by other quants.
