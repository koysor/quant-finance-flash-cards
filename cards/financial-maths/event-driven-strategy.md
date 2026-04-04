# Event Driven Strategy

**Topic:** Financial Mathematics
**Tags:** event driven, merger arbitrage, corporate events, catalyst, special situations
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

An event driven strategy seeks to profit from price dislocations caused by identifiable corporate events — mergers and acquisitions, spin-offs, restructurings, bankruptcies, earnings surprises, or regulatory actions. The strategy involves taking positions before or after the event announcement and holding until the uncertainty resolves. Unlike momentum or value strategies that rely on statistical patterns, event driven strategies are anchored to specific catalysts with defined timelines and binary or near-binary outcomes.

## Key Formula

For **merger arbitrage** (the most common event driven sub-strategy), the annualised return from buying the target at the current market price $P$ when the offer price is $Q$:

$$R_{\text{ann}} = \frac{Q - P}{P} \times \frac{365}{T_{\text{days}}}$$

The **expected return** incorporating the probability of deal completion $p$ and the price if the deal fails $P_{\text{fail}}$:

$$E[R] = p \times \frac{Q - P}{P} + (1 - p) \times \frac{P_{\text{fail}} - P}{P}$$

Setting $E[R] = 0$ and solving gives the **implied deal probability**:

$$p_{\text{impl}} = \frac{P - P_{\text{fail}}}{Q - P_{\text{fail}}}$$

## Example

Company A announces a cash bid for Company B at £12.00 per share. Company B currently trades at £11.40, and analysts estimate it would fall to £8.50 if the deal breaks. The expected closing date is 90 days away.

Implied deal probability:

$$p_{\text{impl}} = \frac{11.40 - 8.50}{12.00 - 8.50} = \frac{2.90}{3.50} = 82.9\%$$

Annualised return if the deal completes:

$$R_{\text{ann}} = \frac{12.00 - 11.40}{11.40} \times \frac{365}{90} = 5.26\% \times 4.06 = 21.4\%$$

If the trader believes the true completion probability is 95% (higher than the market-implied 83%), the expected return is:

$$E[R] = 0.95 \times \frac{0.60}{11.40} + 0.05 \times \frac{-2.90}{11.40} = 5.0\% - 1.3\% = 3.7\%$$

over 90 days — an attractive annualised return of approximately 15%.

## Remember

Event driven strategies are a core hedge fund style, typically accounting for 10–15% of industry assets. The return profile is distinctive: frequent small gains when events resolve as expected, punctuated by occasional large losses when deals fail or events surprise. For quant analysts, the mathematical challenge is estimating the true probability of event outcomes — using historical base rates, regulatory precedent, and market-implied probabilities — and comparing this against the probability embedded in the current spread. The strategy is fundamentally different from factor investing because the edge comes from analysing specific situations rather than exploiting broad statistical regularities, though quantitative tools (logistic regression on deal characteristics, NLP on regulatory filings) are increasingly used to systematise it.
