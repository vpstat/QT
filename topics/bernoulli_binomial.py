import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from math import comb as math_comb

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🪙 Bernoulli & Binomial Distribution</h1>
        <p>Modeling success/failure experiments — single trial and repeated trials.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🪙 Bernoulli", "📊 Binomial"])

    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
        st.markdown("""
The **Bernoulli distribution** models a **single trial** with exactly two outcomes: success (1) or failure (0).
It is the simplest probability distribution and the building block of the Binomial.

**Business applications:** Product quality pass/fail, customer churns or stays, ad clicked or not, loan default or not.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Formulas</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### PMF")
            st.latex(r"X \sim \text{Bernoulli}(p)")
            st.latex(r"P(X=x) = p^x(1-p)^{1-x}, \quad x \in \{0,1\}")
            st.markdown("Or equivalently:")
            st.latex(r"P(X=1)=p, \quad P(X=0)=1-p=q")
        with col2:
            st.markdown("#### Key Statistics")
            st.latex(r"E[X] = p")
            st.latex(r"\text{Var}(X) = p(1-p) = pq")
            st.latex(r"\sigma = \sqrt{pq}")
            st.markdown("#### CDF")
            st.latex(r"F(x) = \begin{cases} 0 & x < 0 \\ 1-p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
        st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A quality check accepts 95% of items. One item is inspected. Find E[X], Var(X), and P(item accepted).

**Solution:** X ~ Bernoulli(p=0.95)
        """)
        st.latex(r"P(X=1)=0.95,\quad E[X]=0.95,\quad \text{Var}(X)=0.95\times0.05=0.0475,\quad\sigma=0.218")

        st.markdown("<span class='prob-badge'>Problem 2 — Business</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** Click-through rate (CTR) for an ad is 3%. If one user sees the ad, what is the expected revenue if a click earns ₹50?

**Solution:** X ~ Bernoulli(0.03). Revenue R = 50X.

E[R] = 50 · E[X] = 50 × 0.03 = **₹1.50 expected revenue per impression**

Var(R) = 50² · Var(X) = 2500 × 0.03 × 0.97 = **72.75**
        """)
        with st.expander("🔍 Tricky Q: If p=0.5, which Bernoulli variable has maximum variance?"):
            st.markdown("**p = 0.5** gives maximum variance: Var(X) = 0.5 × 0.5 = **0.25**. This makes intuitive sense — maximum uncertainty (50/50) gives maximum spread. Variance decreases as p moves toward 0 or 1 (more predictable outcomes).")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
        st.markdown("""
The **Binomial distribution** models the number of successes in **n independent Bernoulli trials**, each with success probability p.

**Business applications:** Number of defective items in a batch, number of customers who purchase, number of loan defaults in a portfolio, number of ad clicks in n impressions.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Formulas</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### PMF")
            st.latex(r"X \sim B(n,\, p)")
            st.latex(r"P(X=k) = \binom{n}{k}p^k(1-p)^{n-k},\quad k=0,1,\ldots,n")
            st.markdown("#### CDF")
            st.latex(r"F(x) = P(X\leq x) = \sum_{k=0}^{\lfloor x\rfloor}\binom{n}{k}p^k(1-p)^{n-k}")
        with col2:
            st.markdown("#### Key Statistics")
            st.latex(r"E[X] = np")
            st.latex(r"\text{Var}(X) = np(1-p) = npq")
            st.latex(r"\sigma = \sqrt{npq}")
            st.markdown("#### Shape")
            st.markdown("""
- **p < 0.5** → Right-skewed
- **p = 0.5** → Symmetric
- **p > 0.5** → Left-skewed
- **n large, p moderate** → Approximates Normal
- **n large, p small (np<5)** → Approximates Poisson(λ=np)
            """)
        st.markdown("---")
        st.markdown("#### 🎛️ Interactive Binomial PMF")
        col1, col2 = st.columns([1,2])
        with col1:
            n_b = st.slider("n:", 1, 50, 20, key="bin_n")
            p_b = st.slider("p:", 0.01, 0.99, 0.3, 0.01, key="bin_p")
        with col2:
            x_b = list(range(n_b+1))
            pmf_b = [math_comb(n_b, k)*p_b**k*(1-p_b)**(n_b-k) for k in x_b]
            fig = go.Figure(go.Bar(x=x_b, y=pmf_b, marker_color='#4f46e5',
                                   text=[f"{v:.3f}" if v > 0.02 else "" for v in pmf_b], textposition='outside'))
            fig.add_vline(x=n_b*p_b, line_dash="dash", line_color="#dc2626",
                          annotation_text=f"Mean={n_b*p_b:.1f}")
            fig.update_layout(title=f"B({n_b}, {p_b}) | E[X]={n_b*p_b:.2f} | SD={np.sqrt(n_b*p_b*(1-p_b)):.3f}",
                              paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                              font_color='#111111', height=300,
                              xaxis=dict(gridcolor='#e2e8f0'), yaxis=dict(gridcolor='#e2e8f0'))
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
        st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A production line has 8% defect rate. 15 items sampled. Find P(exactly 2 defective) and E[defective items].
        """)
        st.latex(r"P(X=2)=\binom{15}{2}(0.08)^2(0.92)^{13}=105\times0.0064\times0.3677\approx\mathbf{0.2457}")
        st.latex(r"E[X]=np=15\times0.08=\mathbf{1.2},\quad \text{Var}=1.104,\quad \sigma\approx1.051")

        st.markdown("<span class='prob-badge'>Problem 2 — Advanced</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A call centre converts 30% of calls to sales. In 20 calls, find: (a) P(≥8 sales), (b) P(between 4 and 7 inclusive).

**Solution:** X ~ B(20, 0.3)
        """)
        pa = 1 - stats.binom.cdf(7, 20, 0.3)
        pb = stats.binom.cdf(7, 20, 0.3) - stats.binom.cdf(3, 20, 0.3)
        st.latex(rf"(a)\;P(X\geq8) = 1-P(X\leq7) = 1-F(7) \approx \mathbf{{{pa:.4f}}}")
        st.latex(rf"(b)\;P(4\leq X\leq7) = F(7)-F(3) \approx \mathbf{{{pb:.4f}}}")

        with st.expander("🔍 Tricky Q: When does Binomial ≈ Poisson?"):
            st.markdown("""
**Poisson approximation** to Binomial: use when **n is large (n ≥ 20) and p is small (p ≤ 0.05)**, with λ = np.

**Example:** B(1000, 0.002) ≈ Poisson(λ=2). The error is negligible and Poisson is easier to compute.

**Rule of thumb:** n ≥ 20, p ≤ 0.05, np = λ ≤ 5
            """)
        st.markdown("</div>", unsafe_allow_html=True)
