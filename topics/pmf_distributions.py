import streamlit as st
import numpy as np
import plotly.graph_objects as go
from math import comb as math_comb

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📊 Probability Mass Function, Expected Value & Discrete Uniform Distribution</h1>
        <p>Describing how probability is distributed across discrete outcomes.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
The **Probability Mass Function (PMF)** is the fundamental tool for discrete random variables — it assigns a probability to every possible value.

The **Expected Value** is the long-run average — weighted by probability.

The **Discrete Uniform Distribution** is the simplest case: every outcome is equally likely (die roll, lottery).
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📈 PMF", "➕ Expected Value", "🎲 Discrete Uniform"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Probability Mass Function (PMF)")
            st.latex(r"p(x_i) = P(X = x_i), \quad i = 1,2,\ldots,k")

            st.markdown("#### Validity Conditions")
            st.latex(r"(1)\quad p(x_i) \geq 0 \quad \forall\, i")
            st.latex(r"(2)\quad \sum_{i=1}^{k} p(x_i) = 1")

            st.markdown("#### CDF from PMF")
            st.latex(r"F(x) = P(X\leq x) = \sum_{x_i \leq x} p(x_i)")

            st.markdown("#### P(a < X ≤ b)")
            st.latex(r"P(a < X \leq b) = F(b) - F(a)")

        with col2:
            st.markdown("#### Example PMF Table (Die Roll)")
            import pandas as pd
            die_df = pd.DataFrame({
                'x': [1, 2, 3, 4, 5, 6],
                'p(x)': ['1/6', '1/6', '1/6', '1/6', '1/6', '1/6'],
                'F(x)': ['1/6', '2/6', '3/6', '4/6', '5/6', '6/6'],
            })
            st.table(die_df)

            st.markdown("#### Constructing a PMF")
            st.markdown("""
1. List all possible values of X
2. Assign probabilities based on the experiment
3. Verify: all probabilities ≥ 0 and sum = 1
4. Compute CDF by accumulating probabilities
            """)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Expected Value (Mean)")
            st.latex(r"E[X] = \mu = \sum_{i} x_i \cdot p(x_i)")
            st.caption("Weighted average of all possible values, weights = probabilities")

            st.markdown("#### Expected Value of a Function g(X)")
            st.latex(r"E[g(X)] = \sum_i g(x_i)\cdot p(x_i)")

            st.markdown("#### Second Moment")
            st.latex(r"E[X^2] = \sum_i x_i^2 \cdot p(x_i)")

            st.markdown("#### Variance")
            st.latex(r"\text{Var}(X) = E[(X-\mu)^2] = E[X^2] - \mu^2")

            st.markdown("#### Standard Deviation")
            st.latex(r"\sigma_X = \sqrt{\text{Var}(X)}")

        with col2:
            st.markdown("#### Key Properties of E[X]")
            st.latex(r"E[aX + b] = a\,E[X] + b")
            st.latex(r"E[X + Y] = E[X] + E[Y]")
            st.latex(r"E[c] = c \quad \text{(constant)}")

            st.markdown("#### Key Properties of Var(X)")
            st.latex(r"\text{Var}(aX+b) = a^2\text{Var}(X)")
            st.latex(r"\text{Var}(c) = 0 \quad \text{(constant has no spread)}")
            st.latex(r"\text{Var}(X+Y) = \text{Var}(X)+\text{Var}(Y) \quad \text{(if X,Y independent)}")

            st.markdown("#### Expected Profit / Decision Making")
            st.markdown("""
**E[X]** is used in actuarial science, gambling, and decision theory to choose the action with **highest expected value**.
            """)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Discrete Uniform Distribution")
            st.markdown("When X takes each of n equally-likely integer values {a, a+1, ..., b}:")
            st.latex(r"X \sim \text{DUniform}(a,\, b), \quad n = b - a + 1")

            st.markdown("#### PMF")
            st.latex(r"P(X = x) = \frac{1}{n} = \frac{1}{b-a+1} \quad \text{for } x = a, a+1,\ldots,b")

            st.markdown("#### Mean")
            st.latex(r"E[X] = \frac{a+b}{2}")

            st.markdown("#### Variance")
            st.latex(r"\text{Var}(X) = \frac{(b-a+1)^2 - 1}{12} = \frac{n^2-1}{12}")

            st.markdown("#### Standard Deviation")
            st.latex(r"\sigma = \sqrt{\frac{(b-a)(b-a+2)}{12}}")

        with col2:
            st.markdown("#### Common Examples")
            st.markdown("""
| Experiment | Distribution |
|------------|-------------|
| Fair die | DUniform(1, 6) |
| Flip one coin (0/1) | DUniform(0, 1) |
| Random day of week | DUniform(1, 7) |
| Random month | DUniform(1, 12) |
| Random card rank | DUniform(1, 13) |
            """)

            st.markdown("#### 🎲 Interactive Discrete Uniform")
            a_val = st.number_input("a (min):", value=1, min_value=-50)
            b_val = st.number_input("b (max):", value=6, min_value=int(a_val)+1)
            n_val = b_val - a_val + 1
            mean_u = (a_val + b_val) / 2
            var_u = (n_val**2 - 1) / 12
            st.metric("Mean E[X]", f"{mean_u:.3f}")
            st.metric("Variance", f"{var_u:.3f}")
            st.metric("SD", f"{var_u**0.5:.3f}")

    st.markdown("---")
    st.markdown("#### 🧮 Custom PMF Builder & Analyzer")
    st.markdown("Enter values and probabilities (comma-separated):")
    col1, col2 = st.columns(2)
    with col1:
        vals_str = st.text_input("Values x:", "0, 1, 2, 3, 4")
        probs_str = st.text_input("Probabilities p(x):", "0.05, 0.20, 0.40, 0.25, 0.10")
    try:
        vals = [float(v.strip()) for v in vals_str.split(',')]
        probs = [float(p.strip()) for p in probs_str.split(',')]
        total = sum(probs)
        if len(vals) == len(probs) and all(p >= 0 for p in probs):
            Ex = sum(v*p for v, p in zip(vals, probs))
            Ex2 = sum(v**2*p for v, p in zip(vals, probs))
            VarX = Ex2 - Ex**2
            with col2:
                st.metric("Σ p(x)", f"{total:.4f} {'✅' if abs(total-1)<0.001 else '⚠️ Must = 1'}")
                st.metric("E[X]", f"{Ex:.4f}")
                st.metric("Var(X)", f"{VarX:.4f}")
                st.metric("SD(X)", f"{VarX**0.5:.4f}")
            fig = go.Figure(go.Bar(x=vals, y=probs, marker_color='#4f46e5',
                                   text=[f"{p:.3f}" for p in probs], textposition='outside'))
            fig.add_vline(x=Ex, line_dash="dash", line_color="#dc2626",
                          annotation_text=f"E[X]={Ex:.2f}", annotation_position="top")
            fig.update_layout(
                title="Custom PMF Visualization",
                xaxis_title="x", yaxis_title="P(X=x)",
                paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                font_color='#111111', height=300,
                xaxis=dict(gridcolor='#e2e8f0'),
                yaxis=dict(gridcolor='#e2e8f0')
            )
            st.plotly_chart(fig, use_container_width=True)
    except:
        st.warning("Check inputs — equal number of comma-separated values and probabilities.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A game pays ₹10 for rolling a 6, ₹5 for rolling 4 or 5, and loses ₹3 otherwise on a fair die. Find E[Winnings].

**Solution:**

| Outcome | X (winnings) | P(X) |
|---------|-------------|------|
| Roll 6 | +10 | 1/6 |
| Roll 4 or 5 | +5 | 2/6 |
| Roll 1,2,3 | -3 | 3/6 |
    """)
    st.latex(r"E[X] = 10\cdot\frac{1}{6} + 5\cdot\frac{2}{6} + (-3)\cdot\frac{3}{6} = \frac{10+10-9}{6} = \frac{11}{6} \approx \textbf{₹1.83}")
    st.markdown("On average, you win ₹1.83 per game — positive expected value, so it's favorable to play.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A discrete RV X has P(X=1)=0.3, P(X=2)=0.4, P(X=3)=0.3. Find E[X²], Var(X), SD(X). Also find E[3X−2].

**Solution:**

**E[X]** = 1(0.3)+2(0.4)+3(0.3) = 0.3+0.8+0.9 = **2.0**

**E[X²]** = 1²(0.3)+2²(0.4)+3²(0.3) = 0.3+1.6+2.7 = **4.6**

**Var(X)** = E[X²]−(E[X])² = 4.6−4.0 = **0.6**

**SD(X)** = √0.6 ≈ **0.775**

**E[3X−2]** = 3·E[X]−2 = 3(2)−2 = **4**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A fair die (DUniform[1,6]) is rolled. Find: (a) P(X ≤ 4), (b) E[X], (c) Var(X), (d) P(X is prime).

**Solution:**

(a) P(X ≤ 4) = F(4) = 4/6 = **2/3 ≈ 0.667**

(b) E[X] = (1+6)/2 = **3.5**

(c) Var(X) = (6²−1)/12 = 35/12 ≈ **2.917**, SD = √(35/12) ≈ **1.708**

(d) Primes in {1,...,6}: {2,3,5} → P(X prime) = 3/6 = **0.5**
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Is E[X²] always equal to (E[X])²?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — and this is a crucial distinction.**

E[X²] = (E[X])² **only when Var(X) = 0** (i.e., X is a constant).

In general: **Var(X) = E[X²] − (E[X])² ≥ 0**, so E[X²] ≥ (E[X])².

**Example:** X ~ DUniform(1,6):  
E[X] = 3.5, (E[X])² = 12.25  
E[X²] = (1+4+9+16+25+36)/6 = 91/6 ≈ 15.17 ≠ 12.25

The difference E[X²] − (E[X])² = 15.17 − 12.25 = Var(X) ≈ 2.92 ✅

**Jensen's Inequality** generalizes this: for a convex function g, E[g(X)] ≥ g(E[X]).
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** A fair coin is flipped until the first Head appears. Let X = number of flips. Is E[X] finite? This is the geometric distribution.")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Yes, E[X] = 2** (finite, despite X having no upper bound!)

**PMF:** P(X = k) = (1/2)ᵏ for k = 1, 2, 3, ... (Geometric distribution with p=1/2)

**Verification that it sums to 1:**
        """)
        st.latex(r"\sum_{k=1}^{\infty}\left(\frac{1}{2}\right)^k = \frac{1/2}{1-1/2} = 1 \checkmark")
        st.markdown("**Expected value:**")
        st.latex(r"E[X] = \sum_{k=1}^{\infty} k\left(\frac{1}{2}\right)^k = \frac{1}{p} = \frac{1}{1/2} = 2")
        st.markdown("""
On average, you need **2 flips** to get the first head. This generalizes: for Geometric(p), E[X] = 1/p.

This lesson: **even an unbounded random variable can have a finite mean** — as long as the probabilities decrease fast enough.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
