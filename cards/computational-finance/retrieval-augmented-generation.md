# Retrieval-Augmented Generation

**Topic:** Computational Finance
**Tags:** rag, retrieval augmented generation, llm, vector database, semantic search, nlp
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Retrieval-Augmented Generation (RAG)** is an architecture that grounds a large language model's responses in retrieved external documents, rather than relying solely on the knowledge encoded in model weights during pre-training. At inference time, the query is embedded and matched against a vector database of document chunks; the top-$k$ most similar chunks are injected into the prompt as context before the LLM generates its answer.

## Key Formula

The retrieval step selects the top-$k$ document chunks $d_1, \ldots, d_k$ by cosine similarity between query and document embeddings:

$$d^* = \arg\max_{d \in \mathcal{D}} \frac{\mathbf{e}_q \cdot \mathbf{e}_d}{\lVert \mathbf{e}_q \rVert \, \lVert \mathbf{e}_d \rVert}$$

The LLM then conditions on the retrieved context:

$$P(\text{answer} \mid \text{query}) \approx P(\text{answer} \mid \text{query},\, d_1, \ldots, d_k)$$

## Example

A compliance analyst queries: "What is our firm's current FRTB IMA approval status for equity desks?" A RAG system embeds the question, retrieves the three most relevant paragraphs from internal regulatory filings and approval letters, and passes them to the LLM. The model answers with citations to the exact document passages — grounded in current internal data rather than its pre-training knowledge cutoff.

## Remember

In quantitative finance, RAG solves the two critical weaknesses of raw LLMs: hallucination and stale knowledge. An LLM answering from memory alone may fabricate regulatory thresholds or report outdated capital ratios. RAG grounds every response in the firm's actual, current documents — regulatory filings, risk reports, research — making it suitable for compliance, due diligence, and client-facing financial Q&A where factual accuracy is non-negotiable.
