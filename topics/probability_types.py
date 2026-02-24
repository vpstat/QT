import streamlit as st
import numpy as np

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🎲 Types of Probability & Events</h1>
        <p>Classical, empirical, and subjective probability — plus every type of event you need to know.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Probability has **three interpretations** (schools of thought), and events can be categorized in multiple ways that affect which probability rules apply.
Understanding these distinctions is the foundation for all statistical inference.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TYPES OF PROBABILITY ─────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Types of Probability</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎯 Classical", "📊 Empirical", "🧠 Subjective"])

    with tab1:
        st.markdown("### Classical (A Priori) Probability")
        st.latex(r"P(A) = \frac{n(A)}{n(S)} = \frac{\text{Number of favorable outcomes}}{\text{Total number of equally likely outcomes}}")
        st.markdown("""
**Assumptions:** All outcomes in the sample space are **equally likely**.

**When to use:** Games of chance, symmetric situations (fair dice, coins, cards).

**Examples:**
- Rolling a fair die: P(4) = 1/6
- Drawing an Ace from a deck: P(Ace) = 4/52 = 1/13
- Tossing two coins, getting HH: P(HH) = 1/4

**Limitation:** Many real-world events are NOT equally likely. A biased coin, a weighted die, or disease outcomes cannot use classical probability.
        """)

    with tab2:
        st.markdown("### Empirical (Frequentist / A Posteriori) Probability")
        st.latex(r"P(A) = \lim_{n \to \infty} \frac{f_A}{n} \approx \frac{\text{Number of times A occurred}}{\text{Total number of trials}}")
        st.markdown("""
**Basis:** Observed frequencies from repeated experiments or historical data.

**Law of Large Numbers:** As n → ∞, the empirical frequency converges to the true probability.

**When to use:** Insurance (mortality rates), quality control (defect rates), epidemiology (disease rates).

**Examples:**
- Factory inspects 1000 bulbs; 23 are defective → P(defective) ≈ 23/1000 = 0.023
- Hospital records 5000 surgeries; 4750 succeed → P(success) ≈ 0.95
- Weather station records rain on 73 out of 365 days → P(rain) ≈ 0.20

**Limitation:** Requires many trials; the past may not represent the future.
        """)

    with tab3:
        st.markdown("### Subjective Probability")
        st.markdown("""
**Basis:** Personal belief, expert judgment, or degree of confidence — **not** based on equally likely outcomes or frequencies.

**Formal foundation:** Bayesian probability theory.

**When to use:** One-time events, forecasting, expert systems.

**Examples:**
- A doctor says: "I believe there is a 70% chance this patient will recover."
- An economist: "Probability of recession next year is 35%."
- A sports analyst: "Team India has a 60% chance of winning this match."

**Key property:** Must satisfy Kolmogorov's axioms:
        """)
        st.latex(r"0 \leq P(A) \leq 1, \quad P(S)=1, \quad P(A\cup B)=P(A)+P(B) \text{ for mutually excl.}")
        st.markdown("""
**Criticism:** Different experts may assign vastly different probabilities. Subjective probabilities must still be **internally consistent**.
        """)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── TYPES OF EVENTS ──────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Types of Events</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1. Simple vs Compound Events")
        st.markdown("""
- **Simple event**: A single outcome — cannot be decomposed.
  - *Example:* Rolling a 3 on a die.
- **Compound event**: Union/intersection of two or more simple events.
  - *Example:* Rolling an even number (2, 4, or 6).
        """)

        st.markdown("#### 2. Mutually Exclusive (Disjoint) Events")
        st.latex(r"A \cap B = \emptyset \implies P(A \cap B) = 0")
        st.markdown("""
Events that **cannot both occur** at the same time.
- *Example:* Getting Head AND Tail on one coin toss.
- *Rule:* P(A∪B) = P(A) + P(B) ← only for mutually exclusive!
        """)

        st.markdown("#### 3. Exhaustive Events")
        st.latex(r"A_1 \cup A_2 \cup \cdots \cup A_k = S")
        st.markdown("""
Events that together **cover the entire sample space** — at least one must occur.
- *Example:* {Head, Tail} on a coin toss.
        """)

        st.markdown("#### 4. Mutually Exclusive & Exhaustive")
        st.markdown("""
A **partition** of S: events that are both pairwise disjoint AND cover S.
- Forms the basis of the Law of Total Probability.
        """)

    with col2:
        st.markdown("#### 5. Independent Events")
        st.latex(r"A \perp B \iff P(A \cap B) = P(A) \cdot P(B)")
        st.latex(r"\Leftrightarrow P(A|B) = P(A) \Leftrightarrow P(B|A) = P(B)")
        st.markdown("""
The occurrence of one event **does not affect** the probability of the other.
- *Example:* Tossing a coin and rolling a die are independent.
- *Non-example:* Drawing cards without replacement — each draw changes probabilities.
        """)

        st.markdown("#### 6. Dependent Events")
        st.markdown("""
The occurrence of A **changes** the probability of B occurring.
- *Example:* Drawing 2 cards WITHOUT replacement.
- P(2nd card is Ace | 1st was Ace) = 3/51 ≠ 4/52

**Key test:** Are they independent? Check P(A∩B) = P(A)·P(B)
        """)

        st.markdown("#### 7. Equally Likely Events")
        st.markdown("""
All individual outcomes have the **same probability**.
- *Example:* Fair die — each face has P = 1/6.
- Required assumption for classical probability.
        """)

        st.markdown("#### 8. Complementary Events")
        st.latex(r"P(A) + P(A^c) = 1")
        st.markdown("""
A and Aᶜ together are always mutually exclusive AND exhaustive.
Useful strategy: **P(at least one) = 1 − P(none)**
        """)

    st.markdown("---")
    st.markdown("#### 📋 Summary Table: Event Types")
    st.markdown(r"""
| Event Type | Condition | Key Rule |
|------------|-----------|----------|
| Mutually Exclusive | A∩B = ∅ | P(A∪B) = P(A)+P(B) |
| Independent | P(A∩B) = P(A)P(B) | P(A\|B) = P(A) |
| Exhaustive | A₁∪⋯∪Aₖ = S | ΣP(Aᵢ) ≥ 1 |
| Complementary | A∪Aᶜ = S, A∩Aᶜ = ∅ | P(A)+P(Aᶜ) = 1 |
| Equally Likely | All P(ωᵢ) equal | P(A) = n(A)/n(S) |
| Dependent | P(A\|B) ≠ P(A) | Use conditional P |
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A coin is tossed 500 times. Heads appear 260 times. (a) What is the empirical probability of Heads? (b) How does this compare to classical probability?

**Solution:**

(a) **Empirical:** P(H) = 260/500 = **0.52**

(b) **Classical:** P(H) = 1/2 = **0.50** (assumes fair coin)

The coin shows a slight bias toward heads. With more trials (law of large numbers), the empirical probability would converge closer to 0.50 if the coin is truly fair.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Events A and B: P(A) = 0.4, P(B) = 0.3, P(A∩B) = 0.12. Are A and B independent? Are they mutually exclusive?

**Solution:**

**Independence test:** P(A)·P(B) = 0.4 × 0.3 = **0.12** = P(A∩B) ✅

→ **A and B are independent.**

**Mutually exclusive test:** P(A∩B) = 0.12 ≠ 0 → **NOT mutually exclusive.**

⚠️ Key insight: Independent events are generally NOT mutually exclusive (and vice versa), unless at least one event has probability 0.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A bag has 5 Red, 3 Blue, 2 Green balls. Two balls drawn WITHOUT replacement. Classify the draws as dependent/independent and find P(both Red).

**Solution:**

The draws are **dependent** — the second draw's probability changes based on the first result (sampling without replacement changes the composition).

P(1st Red) = 5/10 = 1/2

P(2nd Red | 1st was Red) = 4/9 ← only 4 red remain out of 9 total
    """)
    st.latex(r"P(\text{both Red}) = P(R_1) \times P(R_2|R_1) = \frac{5}{10} \times \frac{4}{9} = \frac{20}{90} = \frac{2}{9} \approx 0.222")
    st.markdown("""
If drawn WITH replacement (independent): P(both Red) = (5/10)² = 1/4 = 0.25 — slightly higher.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can two events be both independent AND mutually exclusive (with P(A) > 0 and P(B) > 0)?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — it is impossible** for two events with positive probability.

If A and B are **mutually exclusive**: P(A∩B) = 0

If A and B are **independent**: P(A∩B) = P(A)·P(B) > 0 (since both probabilities > 0)

These two conditions contradict each other: 0 ≠ P(A)·P(B) > 0.

**Intuition:** Mutually exclusive events are maximally *negatively associated* — knowing A happened tells you B definitely didn't. This is the opposite of independence (where knowing A gives no information about B).
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** P(A) = 0.6, P(B) = 0.5, P(A∪B) = 0.8. What type of relationship do A and B have?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Step 1:** Find P(A∩B):  
P(A∪B) = P(A)+P(B)−P(A∩B)  
0.8 = 0.6+0.5−P(A∩B) → **P(A∩B) = 0.3**

**Step 2:** Test independence:  
P(A)·P(B) = 0.6×0.5 = 0.30 = P(A∩B) ✅ → **A and B are independent**

**Step 3:** Test mutual exclusivity:  
P(A∩B) = 0.3 ≠ 0 → **NOT mutually exclusive**

This is a good example where numerical checking (not just intuition) reveals independence.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
