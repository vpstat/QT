import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📬 Poisson Distribution</h1>
        <p>Counting rare events that occur at a constant average rate over time or space.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
The **Poisson distribution** models the number of events occurring in a fixed interval of time, space, or volume, when events:
1. Occur at a **constant average rate** λ (lambda)
2. Are **independent** of each other
3. Two events cannot occur at the **exact same instant**

**Business & real-world applications:**
- Number of customer arrivals per hour (queuing theory)
- Server requests per second (web traffic)
- Defects per square meter of fabric
- Calls received by a helpdesk per day
- Number of accidents at an intersection per year
- Emails per hour, insurance claims per quarter
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### PMF")
        st.latex(r"X \sim \text{Poisson}(\lambda)")
        st.latex(r"P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}, \quad k = 0, 1, 2, \ldots")
        st.caption("e ≈ 2.71828, λ > 0 is the rate parameter")
        st.markdown("#### Key Statistics")
        st.latex(r"E[X] = \lambda")
        st.latex(r"\text{Var}(X) = \lambda")
        st.latex(r"\sigma = \sqrt{\lambda}")
        st.caption("⭐ Mean = Variance = λ — unique and distinctive property!")
    with col2:
        st.markdown("#### CDF")
        st.latex(r"F(x) = e^{-\lambda}\sum_{k=0}^{\lfloor x\rfloor}\frac{\lambda^k}{k!}")
        st.markdown("#### Additive Property")
        st.latex(r"\text{If } X\sim\text{Pois}(\lambda_1),\; Y\sim\text{Pois}(\lambda_2),\; X\perp Y")
        st.latex(r"\text{then } X+Y \sim \text{Pois}(\lambda_1+\lambda_2)")
        st.markdown("#### Poisson Process")
        st.markdown("""
- Events in **non-overlapping intervals are independent**
- P(event in tiny interval Δt) ≈ λΔt
- P(2+ events in Δt) ≈ 0 (negligible)
        """)
        st.markdown("#### Shape")
        st.markdown("""
- **λ < 1** → Strongly right-skewed
- **λ = 1** → Moderately right-skewed
- **λ large (≥10)** → Approximately Normal(μ=λ, σ²=λ)
        """)

    st.markdown("---")
    st.markdown("#### 🎛️ Interactive Poisson PMF")
    col1, col2 = st.columns([1, 2])
    with col1:
        lam = st.slider("λ (mean rate):", 0.1, 20.0, 4.0, 0.1)
        st.metric("Mean = Var = λ", f"{lam}")
        st.metric("SD = √λ", f"{lam**0.5:.4f}")
    with col2:
        max_k = max(20, int(lam*3))
        x_p = list(range(max_k+1))
        pmf_p = [stats.poisson.pmf(k, lam) for k in x_p]
        cdf_p = [stats.poisson.cdf(k, lam) for k in x_p]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_p, y=pmf_p, name='PMF', marker_color='#4f46e5', opacity=0.8))
        fig.add_trace(go.Scatter(x=x_p, y=cdf_p, name='CDF', mode='lines+markers',
                                  line=dict(color='#dc2626', width=2), yaxis='y2'))
        fig.update_layout(
            title=f"Poisson(λ={lam})",
            paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc', font_color='#111111', height=320,
            xaxis=dict(gridcolor='#e2e8f0', title='k'),
            yaxis=dict(gridcolor='#e2e8f0', title='P(X=k)'),
            yaxis2=dict(title='F(k)', overlaying='y', side='right', range=[0, 1.05]),
            legend=dict(x=0.7, y=0.95)
        )
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A call center receives an average of 6 calls per hour. Find: (a) P(exactly 4 calls in an hour), (b) P(≤ 3 calls).

**Solution:** X ~ Poisson(λ=6)
    """)
    st.latex(r"(a)\;P(X=4)=\frac{e^{-6}\cdot6^4}{4!}=\frac{0.00248\times1296}{24}=\mathbf{0.1339}")
    st.latex(r"(b)\;P(X\leq3)=\sum_{k=0}^{3}P(X=k)=e^{-6}(1+6+18+36)=0.00248\times61=\mathbf{0.1512}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A website gets 3 errors per day on average. What is P(no errors in 2 days)? *Hint: use additive property.*

**Solution:**

In 2 days, λ₂ = 3 × 2 = **6 errors per 2 days** (by additive property for Poisson process)
    """)
    st.latex(r"P(X=0) = \frac{e^{-6}\cdot6^0}{0!} = e^{-6} \approx \mathbf{0.00248}")
    st.markdown("There's only a **0.25% chance** of zero errors over 2 days.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced: Business Application</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A hospital emergency ward admits on average 10 patients per night. They have 15 beds. What is the probability they can accommodate all patients (P(X ≤ 15))?
    """)
    prob = stats.poisson.cdf(15, 10)
    st.latex(rf"P(X\leq15) = \sum_{{k=0}}^{{15}}\frac{{e^{{-10}}\cdot10^k}}{{k!}} \approx \mathbf{{{prob:.4f}}}")
    st.markdown(f"""
There is a **{prob*100:.1f}%** chance all patients can be accommodated.

That means **{(1-prob)*100:.1f}% chance of overflow** — needing to divert patients. Management might add 2–3 extra beds to bring overflow risk below 1%.

P(X ≤ 17) = {stats.poisson.cdf(17, 10):.4f} → Only {(1-stats.poisson.cdf(17,10))*100:.2f}% overflow risk with 18 beds.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)
    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** If Var(X) < E[X] for a count variable, can it be Poisson?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No.** For a Poisson distribution, **Var(X) = E[X] = λ exactly**.

- If **Var(X) < E[X]** → **Under-dispersion** — suggests data is more regular than Poisson (e.g., scheduled arrivals). Use Binomial or negative binomial.
- If **Var(X) > E[X]** → **Over-dispersion** — events cluster together (e.g., accidents in high-risk zones). Use Negative Binomial or Zero-Inflated Poisson.

**Checking the mean-variance equality** is a quick empirical test for whether Poisson is an appropriate model.
        """)
    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** λ = 5 events per hour. What is the distribution for events in 30 minutes?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
For a Poisson process, the rate **scales linearly with time**.

30 minutes = 0.5 hours → **λ₃₀ = 5 × 0.5 = 2.5 events per 30 minutes**

The distribution is Poisson(λ=2.5).

**General rule:** If events occur at rate λ per unit time, then in time interval t, X ~ Poisson(λt).

This is the fundamental property of Poisson processes — constant rate, scaling time.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
