# Early Stopping

**Topic:** Computational Finance
**Tags:** early stopping, regularisation, overfitting, validation loss, deep learning, hyperparameter
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Early stopping** is an implicit regularisation technique that halts training when the model's performance on a held-out validation set stops improving, preventing the model from memorising the training data at the cost of generalisation; the number of training epochs at which to stop is itself a hyperparameter, determined by monitoring the validation loss trajectory.

## Key Formula

Training proceeds for epoch $e = 1, 2, \ldots$ and the validation loss $\mathcal{L}_{\text{val}}(e)$ is recorded after each epoch. Training is stopped at epoch $e^*$ defined by the **patience** rule with patience $p$:

$$e^* = \min\!\left\{e \;\middle|\; \mathcal{L}_{\text{val}}(e') \geq \mathcal{L}_{\text{val}}(e^* - p) \;\;\forall\, e' \in [e^*-p,\, e^*]\right\}$$

That is, stop when the validation loss has not improved for $p$ consecutive epochs. The final model weights used are those at epoch $\hat{e} = \arg\min_e \mathcal{L}_{\text{val}}(e)$, not the weights at $e^*$ (which may have degraded).

The optimal stopping epoch implicitly controls effective model capacity: a model stopped after 5 epochs has explored less of the loss landscape and has lower effective complexity than the same architecture trained for 100 epochs.

## Example

Fine-tuning FinBERT on 4,000 labelled analyst sentences. Training loss decreases monotonically. Validation F1:

| Epoch | Train loss | Val F1 |
|---|---|---|
| 3 | 0.41 | 0.83 |
| 5 | 0.28 | 0.87 |
| 7 | 0.19 | 0.88 |
| 9 | 0.12 | 0.87 |
| 11 | 0.07 | 0.85 |

With patience $p = 2$: stop at epoch 9 (val F1 not improved for 2 epochs), restore weights from epoch 7. Without early stopping: training to epoch 20 gives train loss ≈ 0.01 but val F1 drops to 0.79 — clear over-fitting.

## Remember

Early stopping is particularly important when fine-tuning large pre-trained models like BERT or GPT on small financial datasets. The pre-trained weights encode general language knowledge that took billions of tokens to acquire; continued fine-tuning past the validation optimum destroys this knowledge through **catastrophic forgetting** — the model overwrites the general-domain representations with patterns from a few thousand financial sentences that are specific to the training period. In a quant context, this manifests as excellent performance on the labelled training sentences but degraded performance on new earnings releases from a different macro regime. Patience of 2–3 epochs is the standard choice; the validation set must come from a later time window than the training set to avoid look-ahead bias.
