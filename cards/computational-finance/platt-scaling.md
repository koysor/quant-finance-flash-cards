# Platt Scaling

**Topic:** Computational Finance
**Tags:** platt scaling, probability calibration, logistic regression, svm, classifier output, credit scoring
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Platt scaling** is a post-processing method that converts the raw output scores of a trained classifier into calibrated probabilities by fitting a logistic regression on those scores. Unlike retraining the classifier, Platt scaling learns just two scalar parameters — $A$ and $B$ — on a held-out calibration set, making it computationally cheap and applicable to any classifier that produces a continuous score. It was originally proposed by John Platt (1999) to calibrate the signed-distance outputs of Support Vector Machines, which have no natural probabilistic interpretation, but is now routinely applied to gradient-boosted trees, random forests, and neural networks.

## Key Formula

Given a classifier's raw score $f(\mathbf{x}) \in \mathbb{R}$, Platt scaling produces a calibrated probability estimate via:

$$\hat{p} = \sigma(A \cdot f(\mathbf{x}) + B) = \frac{1}{1 + e^{-(A f(\mathbf{x}) + B)}}$$

where $\sigma(\cdot)$ is the logistic sigmoid function. Parameters $A$ and $B$ are estimated by minimising the negative log-likelihood (cross-entropy) on a calibration set $\{(f(\mathbf{x}_i), y_i)\}_{i=1}^{n}$:

$$\hat{A}, \hat{B} = \arg\min_{A, B} -\sum_{i=1}^{n} \left[ y_i \log \hat{p}_i + (1 - y_i) \log(1 - \hat{p}_i) \right]$$

The sigmoid's sign convention means $A < 0$ is typical for SVM outputs (higher score → lower probability of the positive class under the default SVM convention). For most other classifiers, $A > 0$ and $B \approx 0$ when scores are already roughly ordered.

## Example

A bank uses an SVM trained on 50,000 historical loan records to assign each applicant a signed-distance score $f(\mathbf{x})$. The SVM achieves AUC $= 0.80$ but the raw scores are not calibrated probabilities.

On a separate 5,000-loan calibration set, Platt scaling estimates $A = -0.85$, $B = 0.12$. An applicant with raw score $f(\mathbf{x}) = 2.0$ receives:

$$\hat{p} = \frac{1}{1 + e^{-(-0.85 \times 2.0 + 0.12)}} = \frac{1}{1 + e^{1.58}} \approx 0.17$$

The model now assigns a 17% probability of default — a value that can feed directly into $\text{ECL} = PD \times LGD \times EAD$ provisioning under IFRS 9, without requiring the model to be retrained.

## Remember

Platt scaling sits at the intersection of model calibration and regulatory compliance. Under the Basel Internal Ratings-Based (IRB) approach and IFRS 9, risk-weighted assets and expected credit loss provisions are computed using **calibrated** PD estimates, not raw classifier scores. A gradient-boosted or SVM model may rank borrowers excellently (high AUC) yet produce systematically overconfident or underconfident scores. Platt scaling is the practitioner's quick fix: two parameters estimated on a small calibration set transform uncalibrated scores into regulatory-grade PD estimates. The key limitation is its parametric assumption — the logistic function — which may not fit well when the score distribution is multimodal or highly skewed; in those cases, isotonic regression calibration is preferred.
