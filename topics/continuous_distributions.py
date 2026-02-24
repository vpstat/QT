import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🌊 Continuous Probability Distributions</h1>
        <p>Expectation, probability over intervals, variance & SD for continuous random variables.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Unlike discrete RVs (which have a PMF), continuous random variables use a **Probability Density Function (PDF)**. 
The key difference: **P(X = any exact value) = 0**. Probabilities are computed as areas under the PDF curve.

**Business applications:** Modelling time-between-events (Exponential), service times, product lifetimes, measurement errors (Normal), resource utilisation (Uniform).
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📐 PDF & Probability Over Intervals", "🧮 E[X] & Var(X)", "📊 Distributions Summary"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### PDF Properties")
            st.latex(r"f(x) \geq 0 \;\forall x")
            st.latex(r"\int_{-\infty}^{\infty} f(x)\,dx = 1")
            st.markdown("#### Probability Over an Interval")
            st.latex(r"P(a \leq X \leq b) = \int_a^b f(x)\,dx")
            st.latex(r"P(a \leq X \leq b) = P(a < X < b) = P(a < X \leq b)")
            st.caption("Endpoints don't matter for continuous RVs (point prob = 0)")
        with col2:
            st.markdown("#### CDF")
            st.latex(r"F(x) = P(X\leq x) = \int_{-\infty}^{x} f(t)\,dt")
            st.latex(r"f(x) = F'(x)")
            st.markdown("#### Interval via CDF")
            st.latex(r"P(a < X \leq b) = F(b) - F(a)")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Expected Value")
            st.latex(r"E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx")
            st.markdown("#### Expected Value of g(X)")
            st.latex(r"E[g(X)] = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx")
            st.markdown("#### Properties of E[X]")
            st.latex(r"E[aX+b] = a\,E[X]+b")
            st.latex(r"E[X+Y] = E[X]+E[Y]")
        with col2:
            st.markdown("#### Variance")
            st.latex(r"\text{Var}(X) = E[(X-\mu)^2] = \int_{-\infty}^{\infty}(x-\mu)^2 f(x)\,dx")
            st.markdown("#### Shortcut")
            st.latex(r"\text{Var}(X) = E[X^2] - (E[X])^2")
            st.latex(r"E[X^2] = \int_{-\infty}^{\infty} x^2 f(x)\,dx")
            st.markdown("#### Properties")
            st.latex(r"\text{Var}(aX+b) = a^2\text{Var}(X)")
            st.latex(r"\sigma = \sqrt{\text{Var}(X)}")

    with tab3:
        st.markdown("### Variance & SD Summary — All Distributions Covered")
        st.markdown(r"""
| Distribution | Parameters | E[X] | Var(X) | σ |
|-------------|-----------|------|--------|---|
| Bernoulli(p) | p | p | p(1−p) | √(pq) |
| Binomial(n,p) | n, p | np | np(1−p) | √(npq) |
| Poisson(λ) | λ | λ | λ | √λ |
| Discrete Uniform(a,b) | a, b | (a+b)/2 | (n²−1)/12 | √((n²−1)/12) |
| Continuous Uniform(a,b) | a, b | (a+b)/2 | (b−a)²/12 | (b−a)/√12 |
| Normal(μ,σ²) | μ, σ² | μ | σ² | σ |
| Exponential(λ) | λ | 1/λ | 1/λ² | 1/λ |
| Standard Normal | — | 0 | 1 | 1 |
        """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Continuous Uniform</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Waiting time at a traffic light is uniformly distributed on [0, 90] seconds. Find: (a) P(wait > 60s), (b) E[wait], (c) SD.

**Solution:** X ~ Uniform(0, 90), f(x) = 1/90 for 0 ≤ x ≤ 90
    """)
    st.latex(r"(a)\; P(X>60) = \frac{90-60}{90-0} = \frac{30}{90} = 0.333")
    st.latex(r"(b)\; E[X]=\frac{0+90}{2}=45\text{ seconds}")
    st.latex(r"(c)\; \text{Var}=\frac{(90-0)^2}{12}=675,\quad\sigma=\sqrt{675}\approx26.0\text{ seconds}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Exponential</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Average time between customer arrivals is 5 minutes (λ=1/5 per min). Find P(next customer within 3 min).

**Solution:** X ~ Exponential(λ=0.2)
    """)
    st.latex(r"P(X\leq3)=1-e^{-\lambda t}=1-e^{-0.2\times3}=1-e^{-0.6}\approx1-0.5488=\mathbf{0.4512}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Custom PDF</span>", unsafe_allow_html=True)
    st.markdown(r"""
**Q:** f(x) = 3x² for 0 ≤ x ≤ 1 (0 otherwise). Find E[X], Var(X), P(0.5 < X < 0.8).
    """)
    st.latex(r"E[X]=\int_0^1 x\cdot 3x^2\,dx=3\int_0^1 x^3\,dx=3\cdot\frac{1}{4}=\frac{3}{4}=0.75")
    st.latex(r"E[X^2]=\int_0^1 x^2\cdot 3x^2\,dx=3\cdot\frac{1}{5}=\frac{3}{5}=0.60")
    st.latex(r"\text{Var}=E[X^2]-(E[X])^2=0.60-0.5625=\mathbf{0.0375},\;\sigma=0.1936")
    st.latex(r"P(0.5<X<0.8)=\int_{0.5}^{0.8}3x^2\,dx=[x^3]_{0.5}^{0.8}=0.512-0.125=\mathbf{0.387}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)
    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can a PDF value f(x) exceed 1? If so, give an example.")
    with st.expander("🔍 Reveal Solution"):
        st.markdown(r"""
**Yes!** f(x) is a *density*, not a probability. The constraint is ∫f(x)dx = 1, not f(x) ≤ 1.

**Example:** Uniform(0, 0.5): f(x) = 1/(0.5−0) = **2** for 0 ≤ x ≤ 0.5.

Check: ∫₀^0.5 2 dx = 2 × 0.5 = 1 ✅

The "taller" the density, the "narrower" the support to maintain total area = 1.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
