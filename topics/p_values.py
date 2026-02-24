import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📊 P-Values — Complete Guide</h1>
        <p>What they are, how to compute them, how to interpret them, and what they are NOT.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
The **p-value** is one of the most used — and most misunderstood — concepts in all of statistics. It is the bridge between a test statistic and a decision.

**In one sentence:** The p-value is the probability of observing data as extreme as (or more extreme than) what was actually observed, **assuming H₀ is true**.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ──
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts</div>", unsafe_allow_html=True)

    st.markdown("### Formal Definition")
    st.latex(r"p\text{-value} = P\!\left(\text{Test statistic as extreme or more extreme than observed}\;\middle|\;H_0\text{ is true}\right)")

    st.markdown("### How It Works (Intuition)")
    st.markdown("""
1. You **assume H₀ is true** (status quo)
2. You compute a test statistic from sample data
3. You ask: *"If H₀ were true, how often would I see a result this extreme or more?"*
4. That probability is the **p-value**
5. If p-value is very small → the data is very unlikely under H₀ → **reject H₀**
    """)

    st.markdown("---")
    st.markdown("### Computing P-Values for Each Test Type")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Right-tailed")
        st.markdown("Hₐ: μ > μ₀")
        st.latex(r"p = P(Z \geq z_{obs})")
        st.latex(r"= 1 - \Phi(z_{obs})")
    with col2:
        st.markdown("#### Left-tailed")
        st.markdown("Hₐ: μ < μ₀")
        st.latex(r"p = P(Z \leq z_{obs})")
        st.latex(r"= \Phi(z_{obs})")
    with col3:
        st.markdown("#### Two-tailed")
        st.markdown("Hₐ: μ ≠ μ₀")
        st.latex(r"p = 2 \times P(Z \geq |z_{obs}|)")
        st.latex(r"= 2[1 - \Phi(|z_{obs}|)]")

    st.markdown("---")
    st.markdown("### Decision Rule")
    st.latex(r"\text{If } p\text{-value} < \alpha \implies \text{Reject } H_0")
    st.latex(r"\text{If } p\text{-value} \geq \alpha \implies \text{Fail to reject } H_0")

    st.markdown("---")
    st.markdown("### Strength of Evidence Scale")
    evidence = pd.DataFrame({
        'P-value Range': ['p > 0.10', '0.05 < p ≤ 0.10', '0.01 < p ≤ 0.05', '0.001 < p ≤ 0.01', 'p ≤ 0.001'],
        'Evidence Against H₀': ['None', 'Weak (marginal)', 'Moderate', 'Strong', 'Very strong'],
        'Stars': ['—', '•', '*', '**', '***'],
        'Decision at α=0.05': ['Fail to reject', 'Fail to reject', 'Reject', 'Reject', 'Reject']
    })
    st.table(evidence)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── MISCONCEPTIONS ──
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🚫 Common P-Value Misconceptions</div>", unsafe_allow_html=True)

    misconceptions = [
        ("❌ 'p = 0.03 means there's a 3% chance H₀ is true'",
         "**WRONG.** The p-value does NOT give P(H₀ true). It gives P(data | H₀ true). To get P(H₀ true | data), you need Bayes' theorem with a prior."),
        ("❌ 'p = 0.001 means the effect is large and important'",
         "**WRONG.** A tiny p-value means strong *statistical* evidence against H₀, but the actual effect could be practically trivial. With n=100,000, even a 0.01-unit difference can yield p<0.001. Always report **effect size** too."),
        ("❌ 'Not significant means no effect'",
         "**WRONG.** Failing to reject H₀ ≠ H₀ is true. The study may have been underpowered (too small n). Absence of evidence ≠ evidence of absence."),
        ("❌ 'p = 0.06 means the study failed'",
         "**WRONG.** p = 0.06 is marginal — it's weak evidence, not zero evidence. Reporting 'we failed to reach the arbitrary 0.05 cutoff' is more honest than 'no effect'."),
        ("❌ 'If p < 0.05, the result will replicate'",
         "**WRONG.** p-values vary from sample to sample. A p = 0.04 result has roughly a 50% chance of yielding p > 0.05 on a replication of the same size (this is the replication crisis).")
    ]

    for wrong, explanation in misconceptions:
        st.markdown(f"**{wrong}**")
        st.markdown(explanation)
        st.markdown("")
    st.markdown("</div>", unsafe_allow_html=True)

    # ── INTERACTIVE CALCULATOR ──
    st.markdown("<div class='section-card'><div class='section-label label-solved'>🧮 Interactive P-Value Calculator</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        dist = st.radio("Distribution:", ["Z (Normal)", "t (Student's t)"], key="pv_d")
        stat = st.number_input("Test statistic:", value=1.96, step=0.01, key="pv_s")
    with col2:
        tail = st.radio("Tail:", ["Right (>)", "Left (<)", "Two-tailed (≠)"], key="pv_t")
        if "t" in dist:
            df = st.number_input("df:", value=20, min_value=1, key="pv_df")
    with col3:
        if "Z" in dist:
            if "Right" in tail:
                pv = 1 - stats.norm.cdf(stat)
            elif "Left" in tail:
                pv = stats.norm.cdf(stat)
            else:
                pv = 2 * (1 - stats.norm.cdf(abs(stat)))
        else:
            if "Right" in tail:
                pv = 1 - stats.t.cdf(stat, df)
            elif "Left" in tail:
                pv = stats.t.cdf(stat, df)
            else:
                pv = 2 * (1 - stats.t.cdf(abs(stat), df))

        st.metric("P-value", f"{pv:.6f}")
        if pv <= 0.001: lvl = "*** Very strong evidence"
        elif pv <= 0.01: lvl = "** Strong evidence"
        elif pv <= 0.05: lvl = "* Significant"
        elif pv <= 0.10: lvl = "• Marginal"
        else: lvl = "Not significant"
        st.info(lvl)
        for a in [0.01, 0.05, 0.10]:
            if pv < a:
                st.success(f"Reject H₀ at α={a}")
            else:
                st.warning(f"Fail to reject at α={a}")

    # Visual
    x_r = np.linspace(-4, 4, 300)
    if "Z" in dist:
        y_c = stats.norm.pdf(x_r)
    else:
        y_c = stats.t.pdf(x_r, df)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_r, y=y_c, mode='lines',
                              line=dict(color='#1a1a2e', width=2), name='Distribution'))
    # Shade
    if "Right" in tail:
        xs = x_r[x_r >= stat]
        ys = stats.norm.pdf(xs) if "Z" in dist else stats.t.pdf(xs, df)
        fig.add_trace(go.Scatter(x=xs, y=ys, fill='tozeroy',
                                  fillcolor='rgba(220,38,38,0.3)', line=dict(width=0), name=f'p={pv:.4f}'))
    elif "Left" in tail:
        xs = x_r[x_r <= stat]
        ys = stats.norm.pdf(xs) if "Z" in dist else stats.t.pdf(xs, df)
        fig.add_trace(go.Scatter(x=xs, y=ys, fill='tozeroy',
                                  fillcolor='rgba(220,38,38,0.3)', line=dict(width=0), name=f'p={pv:.4f}'))
    else:
        for sv in [abs(stat), -abs(stat)]:
            xs = x_r[x_r >= abs(stat)] if sv > 0 else x_r[x_r <= -abs(stat)]
            ys = stats.norm.pdf(xs) if "Z" in dist else stats.t.pdf(xs, df)
            fig.add_trace(go.Scatter(x=xs, y=ys, fill='tozeroy',
                                      fillcolor='rgba(220,38,38,0.3)', line=dict(width=0), showlegend=False))
    fig.add_vline(x=stat, line_dash="dash", line_color="#dc2626", annotation_text=f"stat={stat:.2f}")
    fig.update_layout(title=f"P-value = {pv:.6f} (red shaded area)",
                      paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                      font_color='#111111', height=300,
                      xaxis=dict(gridcolor='#e2e8f0'), yaxis=dict(gridcolor='#e2e8f0'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ──
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** z = 2.33 in a right-tailed test. Find the p-value and decide at α = 0.01.
    """)
    st.latex(r"p = 1 - \Phi(2.33) = 1 - 0.9901 = \mathbf{0.0099}")
    st.markdown("Since 0.0099 < 0.01 → **Reject H₀** (barely!). This is right at the α = 0.01 boundary.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** t = −1.75, df = 24 in a two-tailed test. Find the p-value and decide at α = 0.05.
    """)
    pv2 = 2 * stats.t.cdf(-1.75, 24)
    st.latex(rf"p = 2 \times P(t_{{24}} \leq -1.75) = 2 \times {stats.t.cdf(-1.75,24):.4f} = \mathbf{{{pv2:.4f}}}")
    st.markdown(f"Since {pv2:.4f} > 0.05 → **Fail to reject H₀**.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A researcher reports "F(2, 27) = 4.35, p = 0.023". Interpret at α = 0.05 and 0.01.
    """)
    st.markdown("""
- At **α = 0.05**: 0.023 < 0.05 → **Reject H₀**. Significant difference among groups.
- At **α = 0.01**: 0.023 > 0.01 → **Fail to reject H₀** at this stricter level.
- Evidence level: **moderate** (* significant)
    """)
    st.markdown("</div>", unsafe_allow_html=True)
