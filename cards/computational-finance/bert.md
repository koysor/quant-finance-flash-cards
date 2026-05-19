# BERT

**Topic:** Computational Finance
**Tags:** bert, transformers, nlp, pre-training, masked language modelling, transfer learning
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**BERT (Bidirectional Encoder Representations from Transformers)** is a transformer encoder pre-trained on two self-supervised tasks — Masked Language Modelling and Next Sentence Prediction — that force it to learn rich bidirectional contextual representations, making it a powerful starting point for fine-tuning on downstream tasks such as sentiment classification and named entity recognition.

## Key Formula

**Masked Language Modelling (MLM):** 15% of input tokens are replaced by [MASK]; the model is trained to predict the original tokens:

$$\mathcal{L}_{\text{MLM}} = -\sum_{i \in \mathcal{M}} \log P\!\left(w_i \;\middle|\; \tilde{\mathbf{x}};\,\theta\right)$$

where $\mathcal{M}$ is the set of masked positions and $\tilde{\mathbf{x}}$ is the masked input sequence. Unlike GPT (left-to-right), BERT attends to **both** left and right context simultaneously when predicting each masked token.

**Next Sentence Prediction (NSP):** the [CLS] token embedding classifies whether sentence B follows sentence A:

$$\mathcal{L}_{\text{NSP}} = -\log P(\text{IsNext} \mid \mathbf{h}_{[\text{CLS}]};\,\theta)$$

Total pre-training loss: $\mathcal{L} = \mathcal{L}_{\text{MLM}} + \mathcal{L}_{\text{NSP}}$.

## Example

BERT-base is pre-trained on 3.3 billion words. MLM example from a 10-K: *"The company recorded a goodwill [MASK] of \$240 million."* BERT sees all surrounding tokens and predicts: P("impairment") = 0.72, P("charge") = 0.18, P("write-off") = 0.07. BERT correctly exploits both left context ("goodwill") and right context ("of \$240 million") — a unidirectional model sees only the left side.

After pre-training, adding a linear classification head on [CLS] and fine-tuning on 5,000 labelled earnings sentences achieves 91% sentiment accuracy — versus 74% for a bag-of-words baseline trained on the same data.

## Remember

BERT's bidirectionality is its critical advantage for financial language: "not improving" requires the right context ("not") to negate the left context ("improving"), and "raised guidance" requires synthesising two separate words. A left-to-right model (GPT-style) cannot see "raised" when predicting the sentiment of "guidance" if it appears first in a sentence. FinBERT is BERT fine-tuned on financial text — it inherits BERT's bidirectional representations and adapts them to financial jargon, enabling practitioners to deploy a high-accuracy financial sentiment model with only a few thousand labelled examples rather than millions.
