# RLHF (Reinforcement Learning from Human Feedback)

**Topic:** Machine Learning
**Tags:** rlhf, reinforcement learning, llm, alignment, fine-tuning, ppo
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Reinforcement Learning from Human Feedback (RLHF)** is a three-stage technique for aligning a pre-trained language model with human preferences. A reward model $r_\phi$ is first trained on human pairwise comparisons of model outputs, then the policy (the LLM) is optimised to maximise expected reward whilst staying close to the original supervised fine-tuned model — typically using Proximal Policy Optimisation (PPO).

## Key Formula

The RLHF training objective maximises expected reward subject to a KL-divergence penalty that prevents the policy from drifting too far from the reference model $\pi_\text{ref}$:

$$\max_{\pi_\theta} \; \mathbb{E}_{x \sim \mathcal{D},\, y \sim \pi_\theta(\cdot \mid x)} \!\left[ r_\phi(x, y) \right] - \beta \cdot D_{\mathrm{KL}}\!\left[\pi_\theta(\cdot \mid x) \;\|\; \pi_\text{ref}(\cdot \mid x)\right]$$

The coefficient $\beta > 0$ trades off reward maximisation against staying close to the pre-trained distribution. Without the KL term, the model collapses to repeating high-reward but degenerate outputs.

## Example

Suppose two responses to "Summarise this earnings call" are shown to a human annotator: response A is accurate but verbose; response B is concise and structured. The annotator marks B as preferred. After collecting thousands of such comparisons, a reward model is trained to predict preferences. The LLM is then fine-tuned via PPO to maximise $r_\phi$ while keeping $\beta \cdot D_\text{KL} < 0.1$ nats, producing a model that reliably generates concise, structured summaries.

## Remember

In quantitative finance, RLHF is the mechanism that transforms a powerful but unreliable LLM into a production-grade financial assistant. Without alignment, an LLM answering client queries about portfolio risk may hallucinate regulatory thresholds or fabricate fund performance figures. RLHF fine-tuning with domain expert annotators teaches the model to flag uncertainty and cite sources — critical for compliance in regulated environments.
