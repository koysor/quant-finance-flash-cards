# Static versus Dynamic Balance Sheet Assumptions

**Topic:** Financial Mathematics
**Tags:** net interest income, balance sheet, constant balance sheet, simulation, IRRBB, management actions
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

When a bank simulates net interest income, it must decide what happens to its balance sheet as positions mature. A **static** (constant) balance sheet assumes each maturing position is replaced by a like-for-like position at the new market rate, so size and mix stay fixed. A **dynamic** balance sheet assumes growth, changes in mix and management actions in response to rates.

## Key Formula

Under a static balance sheet the entire change in NII comes from repricing:

$$\Delta\text{NII}_{\text{static}}(T) \approx \sum_{\text{positions}} \text{Notional} \times \Delta r \times \text{fraction of the year repriced by } T$$

A dynamic projection adds volume and mix effects, so $\Delta\text{NII}_{\text{dyn}} = \Delta\text{NII}_{\text{static}} + \text{(volume, mix, pricing actions)}$.

## Example

A bank has £12bn of fixed-rate loans maturing evenly over six years (£2bn a year), funded by £12bn of floating-rate deposits. Rates rise by 100 bp and the balance sheet is held static.

- **Year 1:** funding costs rise by $12\text{bn} \times 1\% = £120\text{m}$; reinvesting £2bn of maturing loans on average mid-year adds $2\text{bn} \times 1\% \times 0.5 = £10\text{m}$. $\Delta\text{NII} = -£110\text{m}$.
- **Year 2:** funding costs still rise £120m, but loans reinvested in year 1 now earn a full year ($+£20\text{m}$) and another £10m arrives from year 2's maturities. $\Delta\text{NII} = -£90\text{m}$.

## Remember

The static view isolates pure interest rate exposure and is the basis of regulatory comparisons, but it is unrealistic: a real bank would raise loan prices or shift funding. The dynamic view is better for budgeting but easier to bias, because the management actions assumed can always make the answer look benign. Always ask which assumption a quoted NII sensitivity uses before comparing it with another bank's.
