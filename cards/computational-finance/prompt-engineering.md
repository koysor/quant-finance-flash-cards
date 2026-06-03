# Prompt Engineering

**Topic:** Computational Finance
**Tags:** prompt engineering, llm, nlp, few-shot learning, in-context learning, chain-of-thought
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Prompt engineering** is the practice of carefully designing the text input (prompt) to a frozen large language model in order to elicit accurate, structured, or task-specific outputs — without updating any model weights. It exploits the LLM's in-context learning ability, where examples or instructions prepended to the query shift the model's behaviour for that single forward pass.

## Key Formula

**Few-shot prompting** conditions the model on $k$ labelled examples before the query:

$$P(y \mid x) \approx P\!\left(y \;\middle|\; (x_1, y_1), (x_2, y_2), \ldots, (x_k, y_k), x\right)$$

**Chain-of-thought (CoT)** prompting appends a reasoning scaffold, improving accuracy on multi-step tasks:

$$P(y \mid x, \text{``Let's think step by step''}) \gg P(y \mid x)$$

## Example

To extract EPS guidance from an earnings call transcript, a prompt engineering approach might include two labelled examples of transcript snippets paired with structured JSON outputs (few-shot), then append the new transcript. The LLM produces `{"eps_guidance": "1.25–1.30", "direction": "raised"}` without any fine-tuning — purely by pattern completion from the examples in the context window.

## Remember

In quantitative finance, prompt engineering enables rapid prototyping of alpha-generating text-processing pipelines at near-zero marginal cost. A well-crafted prompt extracting management tone from earnings calls or classifying central bank language can be deployed in hours, while fine-tuning the same model would require weeks of data labelling and compute. The trade-off is that prompt-engineered solutions are fragile to phrasing changes and hit context-length limits on long documents — where retrieval-augmented generation takes over.
