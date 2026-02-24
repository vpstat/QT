import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🎰 Random Variables</h1>
        <p>Assigning numerical values to random outcomes — bridging sets and analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
A **random variable (RV)** is a function that assigns a real number to each outcome in a sample space. It transforms qualitative outcomes into numbers we can compute with.

Instead of working with events like "head, tail", we work with numbers like X = 1 (head), X = 0 (tail).

There are two fundamental types:
- **Discrete RV** — countable values (number of defects, students, coin flips)
- **Continuous RV** — uncountable values in an interval (height, time, temperature)
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎯 Definition & Types", "📊 PMF & PDF", "🔢 CDF & Properties"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Formal Definition")
            st.latex(r"X: S \to \mathbb{R}")
            st.markdown("X maps each outcome ω ∈ S to a real number X(ω).")

            st.markdown("#### Discrete Random Variable")
            st.markdown("""
Takes values from a **countable set** {x₁, x₂, x₃, ...}

**Examples:**
- X = number of heads in 3 coin flips → X ∈ {0,1,2,3}
- X = roll of a die → X ∈ {1,2,3,4,5,6}
- X = number of calls per hour → X ∈ {0,1,2,3,...}
- X = number of defects in a batch → X ∈ {0,1,...,n}
            """)

        with col2:
            st.markdown("#### Continuous Random Variable")
            st.markdown("""
Takes values from a **continuous interval** (uncountably infinite)

**Examples:**
- X = height of a person → X ∈ (0, ∞)
- X = temperature → X ∈ (-∞, ∞)
- X = waiting time → X ∈ [0, ∞)
- X = proportion defective → X ∈ [0, 1]

**Key difference:** For continuous RV, P(X = any exact value) = 0. Only P(a < X < b) > 0.
            """)

            st.markdown("#### Key Distinction")
            st.markdown("""
| Feature | Discrete | Continuous |
|---------|----------|------------|
| Values | Countable | Uncountable |
| Tool | PMF: P(X=x) | PDF: f(x) |
| P(X=x) | Possible > 0 | Always = 0 |
| Summation | Σ | ∫ |
            """)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Probability Mass Function (PMF) — Discrete")
            st.latex(r"p(x) = P(X = x), \quad x \in \{x_1, x_2, \ldots\}")
            st.markdown("**Conditions (axioms) for a valid PMF:**")
            st.latex(r"1.\quad p(x) \geq 0 \text{ for all } x")
            st.latex(r"2.\quad \sum_{\text{all }x} p(x) = 1")

            st.markdown("#### Expected Value (Mean) — Discrete")
            st.latex(r"\mu = E[X] = \sum_{\text{all }x} x \cdot p(x)")

            st.markdown("#### Variance — Discrete")
            st.latex(r"\text{Var}(X) = E[(X-\mu)^2] = \sum_{\text{all }x}(x-\mu)^2 p(x)")
            st.latex(r"\text{Var}(X) = E[X^2] - (E[X])^2 \quad \text{(shortcut)}")
            st.latex(r"E[X^2] = \sum x^2 \cdot p(x)")

        with col2:
            st.markdown("#### Probability Density Function (PDF) — Continuous")
            st.latex(r"f(x) \geq 0 \text{ for all } x")
            st.latex(r"\int_{-\infty}^{\infty} f(x)\,dx = 1")
            st.latex(r"P(a \leq X \leq b) = \int_a^b f(x)\,dx")

            st.markdown("#### Expected Value — Continuous")
            st.latex(r"E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx")

            st.markdown("#### Variance — Continuous")
            st.latex(r"\text{Var}(X) = \int_{-\infty}^{\infty}(x-\mu)^2 f(x)\,dx")

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Cumulative Distribution Function (CDF)")
            st.latex(r"F(x) = P(X \leq x)")
            st.markdown("**Discrete:**")
            st.latex(r"F(x) = \sum_{t \leq x} p(t)")
            st.markdown("**Continuous:**")
            st.latex(r"F(x) = \int_{-\infty}^{x} f(t)\,dt")

            st.markdown("#### CDF Properties")
            st.latex(r"0 \leq F(x) \leq 1")
            st.latex(r"\lim_{x\to-\infty}F(x)=0, \quad \lim_{x\to+\infty}F(x)=1")
            st.markdown("F(x) is non-decreasing and right-continuous.")

        with col2:
            st.markdown("#### Properties of E[X] and Var(X)")
            st.latex(r"E[aX + b] = a\,E[X] + b")
            st.latex(r"\text{Var}(aX+b) = a^2\,\text{Var}(X)")
            st.latex(r"E[X+Y] = E[X]+E[Y] \quad \text{(always)}")
            st.latex(r"\text{Var}(X+Y) = \text{Var}(X)+\text{Var}(Y) \quad \text{(if independent)}")
            st.latex(r"\sigma_X = \text{SD}(X) = \sqrt{\text{Var}(X)}")

            st.markdown("#### Functions of RV")
            st.latex(r"E[g(X)] = \sum_x g(x)\,p(x) \quad \text{(discrete)}")

    st.markdown("---")
    st.markdown("#### 🎛️ Interactive PMF Explorer (Number of Heads in n Coin Flips)")
    col1, col2 = st.columns([1, 2])
    with col1:
        n_flips = st.slider("Number of flips (n):", 1, 10, 3)
    with col2:
        x_vals = list(range(n_flips + 1))
        probs = [comb(n_flips, k) * (0.5**n_flips) for k in x_vals]
        from math import comb as math_comb
        probs = [math_comb(n_flips, k) * (0.5**n_flips) for k in x_vals]
        mean_val = sum(x * p for x, p in zip(x_vals, probs))
        var_val = sum((x - mean_val)**2 * p for x, p in zip(x_vals, probs))
        fig = go.Figure(go.Bar(x=x_vals, y=probs, marker_color='#4f46e5',
                               marker_line_color='#1e1b4b', marker_line_width=1.5,
                               text=[f"{p:.4f}" for p in probs], textposition='outside'))
        fig.update_layout(
            title=f"PMF: X = # Heads in {n_flips} flips | E[X]={mean_val:.2f} | SD={var_val**0.5:.3f}",
            xaxis_title="x (# Heads)", yaxis_title="P(X=x)",
            paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
            font_color='#111111', height=320,
            xaxis=dict(gridcolor='#e2e8f0', tickmode='linear'),
            yaxis=dict(gridcolor='#e2e8f0')
        )
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** PMF of X: P(X=0)=0.1, P(X=1)=0.3, P(X=2)=0.4, P(X=3)=k. Find k, E[X], and Var(X).

**Solution:**

**k:** 0.1+0.3+0.4+k = 1 → **k = 0.2**

**E[X]** = 0(0.1)+1(0.3)+2(0.4)+3(0.2) = 0+0.3+0.8+0.6 = **1.7**

**E[X²]** = 0²(0.1)+1²(0.3)+2²(0.4)+3²(0.2) = 0+0.3+1.6+1.8 = **3.7**

**Var(X)** = E[X²] − (E[X])² = 3.7 − (1.7)² = 3.7 − 2.89 = **0.81**

**SD(X)** = √0.81 = **0.9**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A continuous RV has PDF f(x) = cx² for 0 ≤ x ≤ 3, 0 otherwise. Find: (a) c, (b) E[X], (c) P(1 ≤ X ≤ 2).

**Solution:**

**(a)** Valid PDF requires ∫₀³ cx² dx = 1:
    """)
    st.latex(r"\int_0^3 cx^2\,dx = c\cdot\frac{x^3}{3}\Big|_0^3 = c\cdot\frac{27}{3} = 9c = 1 \implies c = \frac{1}{9}")
    st.latex(r"E[X] = \int_0^3 x\cdot\frac{x^2}{9}\,dx = \frac{1}{9}\int_0^3 x^3\,dx = \frac{1}{9}\cdot\frac{81}{4} = \frac{9}{4} = 2.25")
    st.latex(r"P(1\leq X\leq 2) = \int_1^2 \frac{x^2}{9}\,dx = \frac{1}{9}\cdot\frac{x^3}{3}\Big|_1^2 = \frac{1}{27}(8-1) = \frac{7}{27} \approx 0.259")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** For a continuous RV, P(X = 5) = 0. Does this mean X = 5 is impossible?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — it can absolutely occur, but has probability zero.**

For continuous RVs, the probability of any *specific* value is zero because there are uncountably infinitely many values, and probability is spread continuously across them.

**Analogy:** Pick a random point on a 1-meter ruler. The probability of landing on *exactly* the 0.5000000... meter mark is zero, but you always land *somewhere*.

P(X = 5) = 0 means the event has no probability mass at that point, not that it cannot occur. This is why we always talk about **P(a < X < b) = P(a ≤ X ≤ b)** for continuous RVs — the endpoints don't matter.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Var(X + X) vs 2·Var(X) — are they the same?")
    with st.expander("🔍 Reveal Solution"):
        st.latex(r"\text{Var}(X+X) = \text{Var}(2X) = 4\,\text{Var}(X)")
        st.latex(r"2\,\text{Var}(X) \neq 4\,\text{Var}(X) \text{ (in general)}")
        st.markdown("""
**They are NOT the same.** 

X+X is literally 2X (same variable, same observation doubled). Var(2X) = 2²·Var(X) = 4·Var(X).

The formula Var(X+Y) = Var(X)+Var(Y) only applies when X and Y are **independent variables**. Here, X and X are *perfectly correlated* (they're the same variable), so the covariance term (Cov(X,X) = Var(X)) is non-zero.

Full formula: Var(X+X) = Var(X)+Var(X)+2·Cov(X,X) = Var(X)+Var(X)+2·Var(X) = 4·Var(X). ✅
        """)
    st.markdown("</div>", unsafe_allow_html=True)
