# SHAP Values

**Topic:** Computational Finance
**Tags:** shap values, explainability, shapley, feature importance, credit scoring, regulatory compliance
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**SHAP (SHapley Additive exPlanations)** values decompose any model's output into a sum of signed feature contributions, based on the Shapley value from cooperative game theory. Each feature receives a contribution $\phi_j$ that equals its average marginal impact on the prediction across all possible orderings of features.

## Key Formula

The SHAP decomposition satisfies: $f(\mathbf{x}) = \phi_0 + \sum_{j=1}^{p} \phi_j$

where $\phi_0 = \mathbb{E}[f(\mathbf{X})]$ is the baseline (mean prediction) and each SHAP value is:

$$\phi_j = \sum_{S \subseteq P \setminus \{j\}} \frac{|S|!\,(p-|S|-1)!}{p!}\left[f_{S\cup\{j\}}(\mathbf{x}) - f_S(\mathbf{x})\right]$$

Key properties: **Efficiency** (values sum to prediction minus baseline), **Symmetry** (equally contributing features get equal values), **Dummy** (features with no effect get $\phi_j = 0$), **Additivity** (ensemble SHAP = sum of component SHAPs).

## Example

A credit model assigns default probability 0.72 (baseline 0.35). SHAP breakdown: debt-to-income ratio $+0.27$, recent missed payments $+0.18$, income $-0.08$. The explanation: this applicant's high leverage and payment history push default risk up; above-average income partially offsets it — making a £-quantified, auditable explanation of the rejection decision.

## Remember

SHAP values are essential in financial machine learning because regulators and clients require explainability for model-driven decisions. The EU's GDPR and the UK's Consumer Duty regulation both require firms to explain algorithmic outcomes to affected individuals. SHAP provides the rigorous "why" for each individual prediction — each feature's signed contribution — making complex models (XGBoost, neural networks) legally deployable for credit scoring, insurance underwriting, and investment recommendations.
