# One-vs-Rest Classification

**Topic:** Computational Finance
**Tags:** one-vs-rest, multiclass classification, binary classifier, svm, logistic regression, credit ratings
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**One-vs-Rest (OvR)**, also called One-vs-All (OvA), is a strategy for extending binary classifiers to multiclass problems by training one classifier per class, where each classifier distinguishes that class from all others combined. At prediction time, the class whose classifier outputs the highest confidence score is selected.

## Key Formula

For $K$ classes, train $K$ binary classifiers $f_1, \ldots, f_K$, where $f_k$ is fitted on:

$$y_k^{(i)} = \begin{cases} +1 & \text{if } y^{(i)} = k \\ -1 & \text{otherwise} \end{cases}$$

Prediction: $\hat{y} = \arg\max_{k}\, f_k(\mathbf{x})$

**Alternative — One-vs-One (OvO)**: train $\binom{K}{2}$ classifiers, one for each pair; predict by majority vote. OvO trains on smaller subsets (faster per model) but requires more models; OvR is more common in practice.

## Example

Credit rating classification into three grades: Investment (IG), High-Yield (HY), Distressed (D). OvR trains three SVMs: SVM-IG separates IG from {HY, D}; SVM-HY separates HY from {IG, D}; SVM-D separates D from {IG, HY}. A new bond scores: SVM-IG = 0.8, SVM-HY = 0.3, SVM-D = -0.2. Prediction: Investment Grade.

## Remember

OvR is the standard multiclass strategy in quantitative finance because it preserves all the properties of the underlying binary classifier — a calibrated logistic regression classifier under OvR produces interpretable per-class probabilities that sum approximately to one (after Platt scaling). For credit rating migration models, regime classifiers (bull/bear/crisis), and sector classification, OvR allows practitioners to reuse well-understood binary models directly, with each OvR score interpretable as "how strongly does this observation resemble class $k$ versus the rest of the universe?"
