import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🎲 Probability Concepts</h1>
        <p>The mathematical framework for quantifying uncertainty and likelihood of events.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**Probability** measures the likelihood of an event occurring, on a scale from 0 (impossible) to 1 (certain).  
It is the foundation of statistics, hypothesis testing, and machine learning.

**Three approaches:**
1. **Classical**: all outcomes equally likely (rolling dice, tossing coins)
2. **Empirical (Frequentist)**: P(A) = proportion of times A occurs in many trials
3. **Subjective**: P(A) = personal belief/expert judgment (used in Bayesian statistics)
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Classical Probability")
        st.latex(r"P(A) = \frac{n(A)}{n(S)} = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")

        st.markdown("#### Complement Rule")
        st.latex(r"P(A^c) = P(\bar{A}) = 1 - P(A)")

        st.markdown("#### Addition Rule (General)")
        st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")

        st.markdown("#### Addition Rule (Mutually Exclusive)")
        st.latex(r"P(A \cup B) = P(A) + P(B) \quad \text{if } A \cap B = \emptyset")

        st.markdown("#### Multiplication Rule (General)")
        st.latex(r"P(A \cap B) = P(A) \cdot P(B|A) = P(B) \cdot P(A|B)")

        st.markdown("#### Multiplication Rule (Independent)")
        st.latex(r"P(A \cap B) = P(A) \cdot P(B) \quad \text{if A, B independent}")

    with col2:
        st.markdown("#### Conditional Probability")
        st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) \neq 0")

        st.markdown("#### Bayes' Theorem")
        st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")
        st.markdown("**Expanded form (Law of Total Probability):**")
        st.latex(r"P(B) = \sum_{i} P(B|A_i) \cdot P(A_i)")
        st.latex(r"P(A_i|B) = \frac{P(B|A_i) \cdot P(A_i)}{\sum_j P(B|A_j) \cdot P(A_j)}")

        st.markdown("#### Independence Test")
        st.latex(r"A \perp B \iff P(A \cap B) = P(A) \cdot P(B)")

        st.markdown("#### Odds")
        st.latex(r"\text{Odds of A} = \frac{P(A)}{P(A^c)} = \frac{P(A)}{1-P(A)}")

    st.markdown("---")
    st.markdown("#### 🎯 Key Probability Axioms (Kolmogorov)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Axiom 1**\n0 ≤ P(A) ≤ 1 for any event A")
    with col2:
        st.info("**Axiom 2**\nP(S) = 1 (sample space has probability 1)")
    with col3:
        st.info("**Axiom 3**\nFor mutually exclusive events:\nP(A₁∪A₂∪...) = ΣP(Aᵢ)")

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A standard deck has 52 cards. Find P(King), P(Heart), P(King of Hearts), P(King OR Heart).

**Solution:**

P(King) = 4/52 = **1/13 ≈ 0.0769**  
P(Heart) = 13/52 = **1/4 = 0.25**  
P(King ∩ Heart) = 1/52 (**King of Hearts**)  
P(King ∪ Heart) = 4/52 + 13/52 − 1/52 = 16/52 = **4/13 ≈ 0.307**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A quality inspector samples 2 items (without replacement) from a box of 10 (7 good, 3 defective). Find P(both defective) and P(at least one defective).

**Solution:**

P(both defective) = P(D₁) × P(D₂|D₁) = (3/10) × (2/9) = 6/90 = **1/15 ≈ 0.0667**

P(at least one defective) = 1 − P(both good)  
= 1 − (7/10)(6/9) = 1 − 42/90 = 1 − 7/15 = **8/15 ≈ 0.5333**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A medical test is 95% sensitive (P(+|Disease)=0.95) and 90% specific (P(−|No Disease)=0.90). Disease prevalence = 1%. If a patient tests positive, what is P(Disease|+)?

**Solution (Bayes' Theorem):**
    """)
    st.latex(r"P(D|+) = \frac{P(+|D) \cdot P(D)}{P(+|D)\cdot P(D) + P(+|\bar{D})\cdot P(\bar{D})}")
    st.markdown("""
P(D) = 0.01, P(+|D) = 0.95, P(+|no D) = 1−0.90 = 0.10, P(no D) = 0.99

Numerator = 0.95 × 0.01 = 0.0095  
Denominator = 0.0095 + (0.10 × 0.99) = 0.0095 + 0.099 = 0.1085

P(D|+) = 0.0095 / 0.1085 ≈ **8.76%**

⚠️ Despite a 95% sensitive test, only ~8.8% of positives actually have the disease! This is the **false positive paradox** — low prevalence dominate.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 4 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Three machines A, B, C produce 50%, 30%, 20% of output respectively. Defect rates: A=2%, B=3%, C=5%. An item is defective. Find P(made by C | defective).

**Solution:**

P(D) = P(D|A)P(A) + P(D|B)P(B) + P(D|C)P(C)  
= (0.02)(0.50) + (0.03)(0.30) + (0.05)(0.20)  
= 0.010 + 0.009 + 0.010 = **0.029**

P(C|D) = P(D|C)·P(C) / P(D) = (0.05 × 0.20) / 0.029 = 0.010 / 0.029 ≈ **34.5%**

Even though Machine C only produces 20% of output, it accounts for 34.5% of defects — its disproportionate defect rate makes it the most likely source.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Are mutually exclusive events the same as independent events?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — they are almost opposites (for events with P > 0).**

- **Mutually exclusive**: A and B cannot both occur simultaneously → P(A ∩ B) = 0
- **Independent**: Knowing A occurred gives no information about B → P(A ∩ B) = P(A)·P(B)

If A and B are mutually exclusive AND both have P > 0, then:  
P(A ∩ B) = 0 ≠ P(A)·P(B) > 0

→ **Mutually exclusive events are DEPENDENT** (knowing A occurred tells you B definitely didn't happen!)

*Exception:* If P(A) = 0 or P(B) = 0, an event can technically be both mutually exclusive and independent.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** The Monty Hall Problem — You pick door 1. Host opens door 3 (showing a goat). Should you switch to door 2?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Yes, you should ALWAYS switch.**

**Initial probabilities:** P(car at Door 1) = 1/3; P(car at Door 2 or 3) = 2/3

After host opens Door 3 (which always has a goat, and host knows the layout):

P(car at Door 1 | Door 3 opened) = 1/3  
P(car at Door 2 | Door 3 opened) = 2/3

**Switching doubles your probability of winning!**

**Intuition:** When you picked Door 1, there was a 2/3 chance the car was behind Door 2 or 3. The host's action (always revealing a goat) collapses that 2/3 probability onto Door 2 alone.

This is a famous application of **conditional probability and Bayes' theorem** that confounds even professional mathematicians.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
