# Probability Calibration

**Topic:** Computational Finance
**Tags:** calibration, probability, reliability diagram, platt scaling, isotonic regression, credit scoring
**Created:** 2026-04-26
**Author:** Claude Sonnet 4.6

---

## Definition

**Probability calibration** ensures that a classifier's output score $\hat{p}$ accurately represents a true empirical probability: if a model assigns $\hat{p} = 0.3$ to a set of loans, then approximately 30% of those loans should actually default. A model that discriminates well (high AUC) can still be poorly calibrated, producing scores that rank borrowers correctly but cannot be used directly as probability of default (PD) estimates.

## Key Formula

**Calibration error** — assessed by binning predictions into $B$ buckets and comparing mean predicted probability to observed frequency:

$$\text{ECE} = \sum_{b=1}^{B} \frac{|n_b|}{N} \left| \bar{p}_b - \bar{y}_b \right|$$

where $\bar{p}_b$ is the mean predicted probability in bin $b$ and $\bar{y}_b$ is the observed default rate.

**Platt scaling** — fit a logistic regression on top of the raw model score $f(\mathbf{x})$:

$$\hat{p}_{\text{cal}} = \sigma(A \cdot f(\mathbf{x}) + B) = \frac{1}{1 + e^{-(A f(\mathbf{x}) + B)}}$$

Parameters $A$ and $B$ are estimated by maximising the cross-entropy likelihood on a held-out calibration set.

**Isotonic regression** — fit a non-parametric, monotone step function $g$ to the (score, outcome) pairs:

$$\hat{p}_{\text{cal}} = g(f(\mathbf{x})), \quad g \text{ is non-decreasing}$$

## Example

A gradient-boosted model predicts default probabilities on 5,000 retail loans. The model achieves AUC $= 0.82$ (strong discrimination), but a reliability diagram reveals systematic overconfidence: borrowers predicted at $\hat{p} = 0.50$ actually default at a rate of 0.35.

After Platt scaling with $A = 0.72$, $B = -0.18$ (estimated on a 1,000-loan calibration set), the ECE drops from $0.12$ to $0.03$. The model now assigns $\hat{p} = 0.35$ to those borrowers — consistent with their observed default rate. Expected Credit Loss calculations downstream that use $PD \times LGD \times EAD$ now produce reliable reserve estimates.

## Remember

Probability calibration is a **Basel III and IFRS 9 requirement**, not merely a statistical nicety. Under Basel's Internal Ratings-Based (IRB) approach, PD estimates must be long-run averages of actual default rates: a miscalibrated model that assigns $\hat{p} = 0.40$ when the true rate is $0.25$ will cause a bank to hold excess capital (costly) or, worse, assign $\hat{p} = 0.20$ when the true rate is $0.35$ (undercapitalised). Under IFRS 9, Lifetime Expected Credit Loss provisions are computed directly from PD × LGD × EAD × discount factor — calibration error propagates linearly into provision errors. A well-discriminating but poorly calibrated model therefore fails its regulatory purpose even if its ranking of borrowers is excellent.
