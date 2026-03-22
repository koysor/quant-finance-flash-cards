# Prime Broker

**Topic:** Financial Mathematics
**Tags:** prime broker, hedge funds, securities lending, margin, leverage, custody
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A prime broker is a financial institution (typically a division of a large investment bank) that provides a bundled suite of services to hedge funds and other institutional clients. Core services include securities lending for short selling, trade execution and clearing, custody of assets, leverage through margin financing, and consolidated reporting across multiple trading venues.

## Key Formula

The **net margin balance** a fund must maintain with its prime broker is:

$$M_{\text{net}} = V_{\text{long}} \times m_L + |V_{\text{short}}| \times m_S - C_{\text{posted}}$$

where $V_{\text{long}}$ is the long portfolio value, $|V_{\text{short}}|$ is the absolute short portfolio value, $m_L$ and $m_S$ are the long and short margin requirements (typically 50% initial under Regulation T), and $C_{\text{posted}}$ is collateral already held.

The **financing cost** on a leveraged position is:

$$C_{\text{finance}} = V_{\text{borrowed}} \times (r_{\text{benchmark}} + s) \times \frac{t}{360}$$

where $s$ is the prime broker's spread over the benchmark rate.

## Example

A hedge fund has £10m in long positions and £6m in short positions. The prime broker requires 30% initial margin on longs and 35% on shorts:

$$M_{\text{required}} = £10{,}000{,}000 \times 0.30 + £6{,}000{,}000 \times 0.35 = £3{,}000{,}000 + £2{,}100{,}000 = £5{,}100{,}000$$

If the fund has posted £5,500,000 in collateral, its excess margin is £400,000. The prime broker charges SOFR + 50 bps on the £10m borrowed; if SOFR is 4.8%, the annualised financing cost is:

$$C_{\text{finance}} = £10{,}000{,}000 \times 0.053 \times \frac{1}{1} = £530{,}000 \text{ per year}$$

## Remember

The prime broker is the critical intermediary that makes leveraged and short-selling strategies possible for hedge funds. In quantitative finance, the prime brokerage relationship directly affects a fund's cost of leverage, availability of borrows for short selling, and counterparty risk. During market stress — as seen in the 2008 financial crisis — prime brokers can raise margin requirements or recall securities, forcing funds to deleverage at the worst possible time. Understanding prime brokerage economics is essential for modelling the true cost of any strategy that uses leverage or short positions.
