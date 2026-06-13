# Chinchilla Scaling Law

**Topic:** Machine Learning
**Tags:** scaling laws, llm, training, compute, chinchilla
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The **Chinchilla scaling law** (Hoffmann et al., 2022) states that for a fixed compute budget $C$, the compute-optimal strategy is to scale model parameters $N$ and training tokens $D$ in equal proportion — overturning the prior practice of training very large models on too few tokens. The key finding is that the compute-optimal token count is approximately twenty times the parameter count.

## Key Formula

The compute budget approximately satisfies $C \approx 6ND$. Minimising loss subject to this constraint gives:

$$N^* \propto C^{0.5}, \quad D^* \propto C^{0.5}, \quad D^* \approx 20N^*$$

Both model size and training data should grow equally as compute scales. The optimal loss at parameter count $N$ and token count $D$ follows:

$$L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + L_\infty$$

where $\alpha \approx 0.34$, $\beta \approx 0.28$, and $L_\infty$ is the irreducible entropy of the data.

## Example

GPT-3 has $N = 175$ billion parameters. The Chinchilla law predicts compute-optimal training requires $D^* = 20 \times 175 \times 10^9 \approx 3.5$ trillion tokens. In practice, GPT-3 was trained on only 300 billion tokens — roughly ten times under the compute-optimal target. The Chinchilla model itself (70B parameters, 1.4T tokens) matched or exceeded GPT-3 performance at less than half the parameter count.

## Remember

In quantitative finance, the Chinchilla law informs the build-vs-fine-tune decision for domain LLMs. BloombergGPT (50B parameters, 569B tokens) was designed close to the compute-optimal frontier for its budget. Firms deciding whether to pre-train a proprietary financial LLM from scratch must weigh the Chinchilla-predicted compute cost against the alternative of prompt engineering or fine-tuning an existing general model on domain data.
