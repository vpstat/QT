import streamlit as st
import numpy as np

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔀 Conditional Probability</h1>
        <p>Updating probabilities when new information restricts the sample space.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**Conditional probability** answers: *"Given that B has already occurred, what is the probability of A?"*

When we learn that B occurred, the **sample space shrinks** from S to B. We then ask what fraction of B also belongs to A.

This is arguably the most practically important concept in applied probability — it underlies Bayes' theorem, hypothesis testing, recommendation systems, and medical diagnosis.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Definition of Conditional Probability")
        st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0")
        st.caption("Read: 'Probability of A given B'")

        st.markdown("#### Equivalent Forms")
        st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}")
        st.latex(r"P(B|A) = \frac{P(A \cap B)}{P(A)}")

        st.markdown("#### Multiplication Rule (from definition)")
        st.latex(r"P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)")

        st.markdown("#### Chain Rule (General)")
        st.latex(r"P(A \cap B \cap C) = P(A|B \cap C) \cdot P(B|C) \cdot P(C)")

    with col2:
        st.markdown("#### Independence — Special Case")
        st.latex(r"A \perp B \iff P(A|B) = P(A) \iff P(B|A) = P(B)")
        st.caption("Independence means the condition does not update the probability")

        st.markdown("#### Law of Total Probability")
        st.latex(r"P(B) = \sum_{i=1}^{k} P(B | A_i) \cdot P(A_i)")
        st.caption("Where A₁, A₂, ..., Aₖ form a partition of S")

        st.markdown("#### Complementary Conditioning")
        st.latex(r"P(A|B) + P(A^c|B) = 1")
        st.caption("Conditional probabilities sum to 1 over the conditioned space")

        st.markdown("#### General Addition Rule for Conditionals")
        st.latex(r"P(A \cup B | C) = P(A|C) + P(B|C) - P(A \cap B|C)")

    st.markdown("---")

    # Interactive conditional probability calculator
    st.markdown("#### 🧮 Interactive Calculator")
    col1, col2 = st.columns(2)
    with col1:
        pA = st.number_input("P(A):", value=0.40, min_value=0.01, max_value=1.0, step=0.01)
        pB = st.number_input("P(B):", value=0.50, min_value=0.01, max_value=1.0, step=0.01)
        pAandB = st.number_input("P(A ∩ B):", value=0.20, min_value=0.0, max_value=1.0, step=0.01)
    with col2:
        if pB > 0 and pAandB <= pB and pAandB <= pA:
            pa_given_b = pAandB / pB
            pb_given_a = pAandB / pA
            st.metric("P(A | B)", f"{pa_given_b:.4f}")
            st.metric("P(B | A)", f"{pb_given_a:.4f}")
            is_indep = abs(pAandB - pA*pB) < 1e-6
            st.success("✅ A and B are **Independent**" if is_indep else "⚠️ A and B are **Dependent**")
        else:
            st.error("Check inputs: P(A∩B) must be ≤ min(P(A), P(B))")

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A card is drawn from a standard deck. Given it is a face card (J, Q, K), find the probability it is a King.

**Solution:**

Sample space restricted to face cards: 12 face cards (3 per suit × 4 suits)

Kings among face cards: 4 (one per suit)
    """)
    st.latex(r"P(\text{King} | \text{Face card}) = \frac{P(\text{King} \cap \text{Face card})}{P(\text{Face card})} = \frac{4/52}{12/52} = \frac{4}{12} = \frac{1}{3}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** In a manufacturing plant, Machine A produces 60% of output with 3% defect rate; Machine B produces 40% with 5% defect rate. 
(a) Find P(defective). (b) Given an item is defective, P(from Machine A)?

**Solution:**

(a) **Law of Total Probability:**
    """)
    st.latex(r"P(D) = P(D|A)P(A) + P(D|B)P(B) = (0.03)(0.60) + (0.05)(0.40) = 0.018 + 0.020 = 0.038")
    st.markdown("(b) This is a Bayes' theorem question (covered in the next topic), but using conditional probability:")
    st.latex(r"P(A|D) = \frac{P(D|A) \cdot P(A)}{P(D)} = \frac{0.018}{0.038} \approx 0.474")
    st.markdown("Despite A producing 60% of output, only 47.4% of *defectives* come from A — because B has a higher defect rate.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Three balls numbered 1,2,3 in bag. Two drawn without replacement. Given first ball ≥ 2, find P(sum ≥ 4).

**Solution:**

Sample space (ordered pairs without replacement): (1,2),(1,3),(2,1),(2,3),(3,1),(3,2) — 6 outcomes equally likely.

Event B (first ball ≥ 2): (2,1),(2,3),(3,1),(3,2) — 4 outcomes

Event A (sum ≥ 4): (1,3)→4, (2,3)→5, (3,1)→4, (3,2)→5 — outcomes: (2,3),(3,1),(3,2) with sum ≥ 4 AND first ball ≥ 2 → {(2,3),(3,1),(3,2)} = 3 outcomes
    """)
    st.latex(r"P(\text{sum}\geq 4 | \text{first}\geq 2) = \frac{|A \cap B|}{|B|} = \frac{3}{4} = 0.75")
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Is P(A|B) always equal to P(B|A)?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — this is the most common probability error (confusion of the inverse).**
""")
        st.latex(r"P(A|B) = \frac{P(A\cap B)}{P(B)} \neq \frac{P(A\cap B)}{P(A)} = P(B|A) \quad \text{(unless } P(A)=P(B)\text{)}")
        st.markdown("""
**Classic example:**
- P(test positive | cancer) = 0.95 (sensitivity)
- P(cancer | test positive) ≈ 0.087 (8.7% if prevalence = 0.5%)

These are dramatically different! The confusion between them is called the **prosecutor's fallacy** — claiming the probability of innocence given evidence equals the probability of such evidence given innocence.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** P(A) = 0.5, P(B) = 0.3, P(A|B) = 0.6. Find P(A∩B), P(B|A), and check if independent.")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**P(A∩B)** = P(A|B)·P(B) = 0.6 × 0.3 = **0.18**

**P(B|A)** = P(A∩B)/P(A) = 0.18/0.5 = **0.36**

**Independence check:** P(A)·P(B) = 0.5 × 0.3 = 0.15 ≠ 0.18 = P(A∩B)

→ **A and B are dependent.** Knowing B increased the probability of A from 0.5 to 0.6 — a positive association.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
