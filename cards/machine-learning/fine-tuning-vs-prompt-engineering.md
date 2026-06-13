# Fine-Tuning vs Prompt Engineering

**Topic:** Machine Learning
**Tags:** fine-tuning, prompt engineering, llm, transfer learning, nlp, alternative data
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Fine-tuning** updates a pre-trained model's weights on a labelled task-specific dataset, shifting the model's parameters towards the target domain; **prompt engineering** leaves weights frozen and instead crafts the input text to steer the model's output using in-context examples or instructions — the choice between them is a trade-off between labelled-data cost and inference cost.

## Key Formula

Fine-tuning minimises the task loss $\mathcal{L}$ over the labelled set $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$ by updating model parameters $\theta$ from their pre-trained values $\theta_0$:

$$\hat{\theta} = \arg\min_{\theta} \frac{1}{N}\sum_{i=1}^{N} \mathcal{L}(f_\theta(x_i),\, y_i)$$

Prompt engineering leaves $\theta = \theta_0$ fixed and instead constructs an augmented input $\tilde{x}_i = [\text{context}; x_i]$ to shift the conditional distribution $P_{\theta_0}(y \mid \tilde{x}_i)$ without any gradient updates. The effective number of trainable parameters is 0 vs $\lvert\theta\rvert$ (millions to billions).

## Example

Task: classify central bank statement sentences as hawkish, dovish, or neutral.

| Approach | Labelled examples needed | Cost to adapt | Inference cost per doc | Accuracy (FinancialPhraseBank) |
|---|---|---|---|---|
| Fine-tuned FinBERT | 2,000 | \$15 GPU-hour | \$0.0001 | 87% |
| GPT-4 few-shot prompt | 5 (in prompt) | \$0 | \$0.05 | 84% |
| GPT-4 zero-shot prompt | 0 | \$0 | \$0.05 | 76% |

At 10,000 documents per day, inference cost is \$1 (fine-tuned) vs \$500 (GPT-4 few-shot) — a 500× difference that compounds over a year to \$180,000.

## Remember

The practical rule in financial NLP: use **prompt engineering** when labelled data is scarce (fewer than ~500 examples) or the task is exploratory and changes frequently; use **fine-tuning** when the task is stable, you have at least 1,000 labelled examples, and inference volume is high. Earnings sentiment scoring for an index of 500 stocks, done daily, almost always justifies fine-tuning — the one-time annotation cost is recovered within weeks of inference savings. Conversely, answering ad-hoc analyst questions about a specific filing is prompt engineering territory, since the queries are unique and volume is low.
