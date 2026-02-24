import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔵 Sets & Venn Diagrams</h1>
        <p>The language of events — using set theory to reason about probability.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**Set theory** provides the mathematical backbone of probability. An **event** is simply a *set* of outcomes from a sample space. Understanding sets, unions, intersections, and complements is essential before studying probability rules.

A **Venn diagram** is a visual tool for representing relationships between sets/events — widely used to solve probability problems intuitively.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Core Set Notation")
        st.markdown(r"""
| Symbol | Meaning |
|--------|---------|
| S | Sample space (universal set of all outcomes) |
| A, B | Events (subsets of S) |
| ∅ | Empty set (impossible event) |
| x ∈ A | x is an element of A |
| A ⊆ B | A is a subset of B |
| \|A\| or n(A) | Cardinality (number of elements in A) |
        """)

        st.markdown("#### Union (OR)")
        st.latex(r"A \cup B = \{x : x \in A \text{ or } x \in B\}")

        st.markdown("#### Intersection (AND)")
        st.latex(r"A \cap B = \{x : x \in A \text{ and } x \in B\}")

        st.markdown("#### Complement (NOT)")
        st.latex(r"A^c = \bar{A} = \{x \in S : x \notin A\}")

        st.markdown("#### Difference")
        st.latex(r"A \setminus B = A \cap B^c = \{x \in A : x \notin B\}")

    with col2:
        st.markdown("#### Counting / Cardinality Rules")
        st.latex(r"|A \cup B| = |A| + |B| - |A \cap B|")
        st.latex(r"|A \cup B \cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|")

        st.markdown("#### De Morgan's Laws")
        st.latex(r"(A \cup B)^c = A^c \cap B^c")
        st.latex(r"(A \cap B)^c = A^c \cup B^c")

        st.markdown("#### Distributive Laws")
        st.latex(r"A \cap (B \cup C) = (A\cap B) \cup (A\cap C)")
        st.latex(r"A \cup (B \cap C) = (A\cup B) \cap (A\cup C)")

        st.markdown("#### Probability via Sets")
        st.latex(r"P(A \cup B) = P(A)+P(B)-P(A\cap B)")
        st.latex(r"P(A^c) = 1-P(A)")
        st.latex(r"P(A \setminus B) = P(A) - P(A \cap B)")

    st.markdown("---")
    st.markdown("#### 🔵 Venn Diagram Regions (Two Sets A and B)")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info("**Only A**\nA ∩ Bᶜ\n= A − (A∩B)")
    with col2:
        st.success("**A ∩ B**\nBoth A and B\n= Intersection")
    with col3:
        st.info("**Only B**\nAᶜ ∩ B\n= B − (A∩B)")
    with col4:
        st.warning("**Neither**\nAᶜ ∩ Bᶜ\n= (A∪B)ᶜ")

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** In a class of 50 students: 30 play Cricket (C), 25 play Football (F), and 10 play both. Find:
(a) n(C ∪ F), (b) n(only Cricket), (c) n(neither sport)

**Solution:**

(a) n(C ∪ F) = 30 + 25 − 10 = **45 students** play at least one sport

(b) n(only Cricket) = n(C) − n(C ∩ F) = 30 − 10 = **20 students**

(c) n(neither) = 50 − 45 = **5 students**

Venn diagram regions: [Only C = 20] [Both = 10] [Only F = 15] [Neither = 5]
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** S = {1,2,3,4,5,6,7,8,9,10}, A = {2,4,6,8,10} (evens), B = {1,2,3,4,5} (first five).
Find: A∪B, A∩B, Aᶜ, A∖B, and verify De Morgan's law.

**Solution:**
- A ∪ B = {1,2,3,4,5,6,8,10} → 8 elements
- A ∩ B = {2,4} → elements both even AND ≤ 5
- Aᶜ = {1,3,5,7,9} → odd numbers
- A ∖ B = A ∩ Bᶜ = {6,8,10} → evens greater than 5

**De Morgan's verification:** (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ  
(A ∪ B)ᶜ = {7,9} (elements not in A∪B)  
Aᶜ = {1,3,5,7,9}, Bᶜ = {6,7,8,9,10}, Aᶜ ∩ Bᶜ = {7,9} ✅
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** In a survey of 100 people: 60 read newspaper A, 50 read B, 40 read C, 30 read A∩B, 20 read A∩C, 15 read B∩C, 10 read all three. Find:
(a) n(A∪B∪C) and (b) n(none of the three).
    """)
    st.latex(r"|A\cup B\cup C| = |A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|")
    st.markdown("""
= 60 + 50 + 40 − 30 − 20 − 15 + 10 = **95 people**

(b) n(none) = 100 − 95 = **5 people** read none of the three newspapers.

This is the **Inclusion-Exclusion Principle** extended to 3 sets — a powerful combinatorial counting tool.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** If A ⊆ B, what can you conclude about P(A), P(B), and P(A∩B)?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
If A ⊆ B (A is a subset of B), then every outcome in A is also in B. Therefore:
- **P(A) ≤ P(B)** — since A is a smaller set, it can't have higher probability
- **A ∩ B = A** — every element of A is in B, so the intersection *is* A
- **P(A ∩ B) = P(A)** — directly follows

This also means: P(A ∪ B) = P(A) + P(B) − P(A∩B) = P(A) + P(B) − P(A) = **P(B)**

Intuitively: if A is a subset of B, then "A or B happening" is just B happening.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Prove that for any two events A and B: P(A∖B) = P(A) − P(A∩B)")
    with st.expander("🔍 Reveal Solution"):
        st.latex(r"A = (A \cap B) \cup (A \cap B^c) = (A \cap B) \cup (A \setminus B)")
        st.markdown("Since (A∩B) and (A∖B) are **mutually exclusive** (disjoint):")
        st.latex(r"P(A) = P(A\cap B) + P(A\setminus B)")
        st.latex(r"\therefore P(A\setminus B) = P(A) - P(A\cap B) \quad \blacksquare")
        st.markdown("This result is useful when you know P(A), P(B), and P(A∩B) but need the probability of A without B.")
    st.markdown("</div>", unsafe_allow_html=True)
