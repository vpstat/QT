import streamlit as st
import numpy as np
from math import factorial, comb, perm

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔢 Counting Rules</h1>
        <p>Systematic methods to count outcomes — the backbone of classical probability.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Classical probability requires counting favorable outcomes and total outcomes. For complex scenarios, direct enumeration is impractical — **counting rules** provide systematic shortcuts.

Core rules: **Multiplication Rule → Permutations → Combinations → Partition Rule**
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["✖️ Multiplication", "🔄 Permutations", "🎯 Combinations", "📦 Partition"])

    with tab1:
        st.markdown("### Fundamental Counting Principle (Multiplication Rule)")
        st.latex(r"\text{If task 1 can be done in } n_1 \text{ ways, task 2 in } n_2, \ldots \text{ then total} = n_1 \times n_2 \times \cdots \times n_k")
        st.markdown("""
**Example:** A restaurant offers 3 starters, 5 mains, 4 desserts.  
Number of 3-course meals = 3 × 5 × 4 = **60 meals**

**With/Without repetition:**
- **With repetition:** Choosing digits for a 4-digit PIN from 0–9 → 10⁴ = 10,000
- **Without repetition:** 4-digit PIN with distinct digits → 10 × 9 × 8 × 7 = 5,040
        """)

    with tab2:
        st.markdown("### Permutations — Order MATTERS")
        st.markdown("#### Arranging n distinct objects in all possible orders:")
        st.latex(r"n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1")
        st.markdown("#### Choosing r objects from n (order matters):")
        st.latex(r"^nP_r = P(n,r) = \frac{n!}{(n-r)!}")
        st.markdown("#### Permutations with repeated elements:")
        st.latex(r"\frac{n!}{n_1! \cdot n_2! \cdots n_k!} \quad \text{(n objects, } n_i \text{ of type } i\text{)}")
        st.markdown("#### Circular Permutations:")
        st.latex(r"(n-1)! \quad \text{(n objects in a circle — one position is fixed)}")
        st.markdown("""
**Order matters examples:** Race rankings, passwords, seating arrangements, scheduling tasks.
        """)
        st.markdown("#### 🧮 Calculator")
        col1, col2 = st.columns(2)
        with col1:
            n_p = st.number_input("n:", value=10, min_value=1, max_value=20, key="perm_n")
        with col2:
            r_p = st.number_input("r:", value=3, min_value=0, max_value=int(n_p), key="perm_r")
        if r_p <= n_p:
            result = perm(int(n_p), int(r_p))
            st.metric(f"P({int(n_p)},{int(r_p)}) =", f"{result:,}")

    with tab3:
        st.markdown("### Combinations — Order does NOT matter")
        st.latex(r"^nC_r = C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}")
        st.markdown("""
**Relationship:** nCr = nPr / r! (divide by r! to remove ordering)

**Properties:**
        """)
        st.latex(r"\binom{n}{r} = \binom{n}{n-r}, \quad \binom{n}{0}=\binom{n}{n}=1, \quad \binom{n}{1}=n")
        st.latex(r"\binom{n}{r} + \binom{n}{r+1} = \binom{n+1}{r+1} \quad \text{(Pascal's identity)}")
        st.markdown("""
**Order doesn't matter examples:** Lottery selection, committee formation, card hands, choosing toppings.
        """)
        st.markdown("#### 🧮 Calculator")
        col1, col2 = st.columns(2)
        with col1:
            n_c = st.number_input("n:", value=52, min_value=1, max_value=52, key="comb_n")
        with col2:
            r_c = st.number_input("r:", value=5, min_value=0, max_value=int(n_c), key="comb_r")
        if r_c <= n_c:
            result_c = comb(int(n_c), int(r_c))
            st.metric(f"C({int(n_c)},{int(r_c)}) =", f"{result_c:,}")

    with tab4:
        st.markdown("### Partition Rule (Multinomial Coefficient)")
        st.latex(r"\binom{n}{n_1, n_2, \ldots, n_k} = \frac{n!}{n_1!\cdot n_2!\cdots n_k!}, \quad \sum n_i = n")
        st.markdown("""
**Use:** Distributing n distinct objects into k groups of sizes n₁, n₂, ..., nₖ.

**Example:** 10 people → 3 committees of 3, 4, and 3: 10!/(3!·4!·3!) = 4,200 ways

**Multinomial Theorem:**
        """)
        st.latex(r"(x_1+x_2+\cdots+x_k)^n = \sum_{n_1+\cdots+n_k=n} \binom{n}{n_1,\ldots,n_k}\prod x_i^{n_i}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** How many 3-letter codes can be formed from {A,B,C,D,E}: (a) with repetition, (b) without repetition, (c) without repetition as a combination?

**Solution:**

(a) **With repetition** (order matters): 5³ = **125 codes**

(b) **Without repetition, order matters** (permutation): P(5,3) = 5!/(5-3)! = 5×4×3 = **60 arrangements**

(c) **Without repetition, order doesn't matter** (combination): C(5,3) = 5!/(3!·2!) = **10 groups**

Ratio: 60/10 = 3! = 6 — each combination corresponds to 6 different ordered arrangements.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** In a lottery, 6 numbers are drawn from 1–49 (no repetition, order doesn't matter). What is: (a) total possible outcomes, (b) P(winning with 1 ticket)?

**Solution:**
    """)
    st.latex(r"\binom{49}{6} = \frac{49!}{6!\cdot 43!} = \frac{49\times48\times47\times46\times45\times44}{6!} = 13{,}983{,}816")
    st.markdown(f"""
(a) Total outcomes = **13,983,816**

(b) P(winning) = 1/13,983,816 ≈ **0.0000000715 = 7.15 × 10⁻⁸**

You're about 45× more likely to be struck by lightning this year than to win this lottery with a single ticket.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A committee of 5 is chosen from 6 men and 4 women. Find P(at least 2 women on committee).

**Solution:**

Total committees: C(10,5) = 252

**P(≥2 women) = 1 − P(0 women) − P(1 woman)**

P(0 women) = C(4,0)·C(6,5)/C(10,5) = 1×6/252 = 6/252

P(1 woman) = C(4,1)·C(6,4)/C(10,5) = 4×15/252 = 60/252
    """)
    st.latex(r"P(\geq 2\text{ women}) = 1 - \frac{6}{252} - \frac{60}{252} = 1 - \frac{66}{252} = \frac{186}{252} = \frac{31}{42} \approx 0.738")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** How many distinct arrangements of the letters in 'STATISTICS'?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**STATISTICS** has 10 letters: S(3), T(3), A(1), I(2), C(1)

Using the **permutation with repeated elements formula:**
        """)
        st.latex(r"\frac{10!}{3!\cdot 3!\cdot 1!\cdot 2!\cdot 1!} = \frac{3{,}628{,}800}{6\times6\times1\times2\times1} = \frac{3{,}628{,}800}{72} = 50{,}400")
        st.markdown("There are **50,400 distinct arrangements** of the letters in STATISTICS.")

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** nCr = nC(n−r). Prove this and explain intuitively why selecting r objects from n is equivalent to selecting the n−r objects you DON'T take.")
    with st.expander("🔍 Reveal Solution"):
        st.latex(r"\binom{n}{n-r} = \frac{n!}{(n-r)!\cdot(n-(n-r))!} = \frac{n!}{(n-r)!\cdot r!} = \binom{n}{r} \quad \blacksquare")
        st.markdown("""
**Intuition:** Every time you choose a group of r objects, you simultaneously *unchosen* the remaining n−r objects. So choosing 3 from 10 is the same counting problem as choosing the 7 you leave behind.

**Practical use:** If C(100,97) looks hard to compute, use C(100,3) = 161,700 instead — same value, much easier!
        """)
    st.markdown("</div>", unsafe_allow_html=True)
