# Knowledge Distillation

**Topic:** Computational Finance
**Tags:** knowledge distillation, model compression, student teacher, inference, nlp
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Knowledge distillation** trains a compact **student** model to mimic the output distribution of a large pre-trained **teacher** model, rather than training directly on hard labels. The student learns from the teacher's soft probability outputs — called **soft targets** — which carry more information than one-hot labels because they encode the teacher's uncertainty and inter-class similarity structure.

## Key Formula

The student is trained on a combined loss, where temperature $T > 1$ softens the teacher's output distribution:

$$\hat{p}_k^{(T)} = \frac{\exp(z_k / T)}{\sum_j \exp(z_j / T)}$$

$$\mathcal{L}_\text{KD} = (1 - \alpha)\,\mathcal{L}_\text{CE}(\mathbf{y},\, \hat{\mathbf{p}}_S) \;+\; \alpha\, T^2\, \mathcal{L}_\text{CE}\!\left(\hat{\mathbf{p}}_T^{(T)},\, \hat{\mathbf{p}}_S^{(T)}\right)$$

The first term trains the student on true labels; the second trains it to match the teacher's soft output at temperature $T$. The $T^2$ factor corrects for the reduction in gradient magnitude caused by softening. Typical values: $\alpha = 0.5$, $T = 4$.

## Example

FinBERT (110M parameters) classifies earnings call sentences with 91% accuracy but takes 180 ms per sentence — too slow for a real-time news sentiment signal. A 4-layer DistilBERT student (40M parameters) trained with $\alpha = 0.5$, $T = 4$ on FinBERT's soft outputs achieves 88% accuracy at 35 ms per sentence. The 3% accuracy cost is acceptable; the $5\times$ inference speedup enables processing of 2,000 sentences per second, sufficient for live news flow.

## Remember

Knowledge distillation solves a core tension in production financial NLP: large models (BERT, FinBERT) achieve the best accuracy but are too slow and memory-intensive for low-latency applications such as real-time sentiment signals, order-flow analysis, or on-device risk monitoring. Distillation transfers the teacher's generalisation ability — encoded in its soft output probabilities — to a much smaller model at a fraction of the compute cost. The soft targets are crucial: they reveal, for example, that a sentence is "mostly positive, slightly ambiguous" rather than simply "positive", which helps the student learn decision boundaries more accurately than hard labels alone. In practice, domain-specific distillation (teacher and student both fine-tuned on financial text) outperforms generic distillation by 2–4 percentage points on financial classification tasks.
