import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📊 ANOVA — Analysis of Variance</h1>
        <p>Comparing means across 3+ groups using MSTR, MSE, and the F-test.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**ANOVA** (Analysis of Variance) tests whether the means of **three or more groups** differ significantly. Instead of running many two-sample t-tests (which inflates Type I error), ANOVA uses a single F-test.

**Business applications:** Comparing sales across regions, marketing campaign effectiveness, product yields across factory lines, customer satisfaction by age group.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋 One-Way ANOVA", "🧮 Interactive ANOVA", "📝 Reporting Results"])

    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)
        st.markdown("#### Hypotheses")
        st.latex(r"H_0: \mu_1 = \mu_2 = \cdots = \mu_k \quad\text{(all group means equal)}")
        st.latex(r"H_a: \text{At least one } \mu_i \text{ differs}")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Decomposition of Variance")
            st.latex(r"\text{SST} = \text{SSTR} + \text{SSE}")
            st.markdown("""
| Term | Full Name | Measures |
|------|-----------|----------|
| SST | Total Sum of Squares | Total variation |
| SSTR | Sum of Sq. b/w Treatments | Between-group variation |
| SSE | Sum of Sq. Error | Within-group variation |
            """)
            st.latex(r"\text{SST} = \sum_{i}\sum_j (x_{ij} - \bar{x})^2")
            st.latex(r"\text{SSTR} = \sum_{i=1}^k n_i(\bar{x}_i - \bar{x})^2")
            st.latex(r"\text{SSE} = \sum_{i=1}^k \sum_{j=1}^{n_i}(x_{ij} - \bar{x}_i)^2")
        with col2:
            st.markdown("#### Mean Squares")
            st.latex(r"\text{MSTR} = \frac{\text{SSTR}}{k-1}")
            st.latex(r"\text{MSE} = \frac{\text{SSE}}{n_T - k}")
            st.caption("k = number of groups, n_T = total observations")
            st.markdown("#### F-Statistic")
            st.latex(r"F = \frac{\text{MSTR}}{\text{MSE}} \;\sim\; F_{k-1,\;n_T-k}")
            st.markdown("**Decision:** Reject H₀ if F > F_α or p-value < α")
            st.markdown("#### Assumptions")
            st.markdown("""
1. **Independence** — observations are independent
2. **Normality** — each group is approximately normal
3. **Equal variances** — σ₁² ≈ σ₂² ≈ ... ≈ σₖ² (homoscedasticity)
            """)
        st.markdown("---")
        st.markdown("#### ANOVA Table Template")
        anova_template = pd.DataFrame({
            'Source': ['Between (Treatments)', 'Within (Error)', 'Total'],
            'SS': ['SSTR', 'SSE', 'SST'],
            'df': ['k−1', 'n_T−k', 'n_T−1'],
            'MS': ['MSTR = SSTR/(k−1)', 'MSE = SSE/(n_T−k)', '—'],
            'F': ['MSTR/MSE', '—', '—'],
            'p-value': ['P(F > F_obs)', '—', '—']
        })
        st.table(anova_template)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>🧮 Interactive ANOVA Calculator</div>", unsafe_allow_html=True)
        st.markdown("Enter data for each group (comma-separated):")
        n_groups = st.number_input("Number of groups:", value=3, min_value=2, max_value=6)
        groups_data = []
        cols = st.columns(int(n_groups))
        for i in range(int(n_groups)):
            with cols[i]:
                defaults = ["82,87,79,93,88", "75,68,72,80,71", "91,95,89,97,93"]
                default = defaults[i] if i < len(defaults) else "80,85,78,82"
                raw = st.text_input(f"Group {i+1}:", default, key=f"anova_g{i}")
                try:
                    g = [float(x.strip()) for x in raw.split(',')]
                    groups_data.append(np.array(g))
                except:
                    st.error("Invalid input")

        if len(groups_data) >= 2 and all(len(g) >= 2 for g in groups_data):
            f_stat, p_val = stats.f_oneway(*groups_data)
            all_data = np.concatenate(groups_data)
            grand_mean = all_data.mean()
            k = len(groups_data)
            n_T = len(all_data)
            sstr = sum(len(g) * (g.mean() - grand_mean)**2 for g in groups_data)
            sse = sum(np.sum((g - g.mean())**2) for g in groups_data)
            sst = sstr + sse
            mstr = sstr / (k - 1)
            mse = sse / (n_T - k)

            col1, col2 = st.columns(2)
            with col1:
                anova_df = pd.DataFrame({
                    'Source': ['Between', 'Within', 'Total'],
                    'SS': [f"{sstr:.4f}", f"{sse:.4f}", f"{sst:.4f}"],
                    'df': [k-1, n_T-k, n_T-1],
                    'MS': [f"{mstr:.4f}", f"{mse:.4f}", "—"],
                    'F': [f"{f_stat:.4f}", "—", "—"],
                    'p-value': [f"{p_val:.6f}", "—", "—"]
                })
                st.table(anova_df)
            with col2:
                for i, g in enumerate(groups_data):
                    st.metric(f"Group {i+1}: x̄", f"{g.mean():.3f} (n={len(g)}, s={g.std(ddof=1):.3f})")
                st.metric("Grand Mean x̄", f"{grand_mean:.3f}")

            alpha_anova = st.selectbox("α:", [0.01, 0.05, 0.10], index=1, key="anova_alpha")
            if p_val < alpha_anova:
                st.error(f"**Reject H₀** (F={f_stat:.4f}, p={p_val:.6f} < {alpha_anova}). At least one group mean differs significantly.")
            else:
                st.success(f"**Fail to reject H₀** (F={f_stat:.4f}, p={p_val:.6f} ≥ {alpha_anova}). No significant difference among group means.")

            # Box plot
            fig = go.Figure()
            for i, g in enumerate(groups_data):
                fig.add_trace(go.Box(y=g, name=f"Group {i+1}", marker_color=['#4f46e5','#059669','#dc2626','#b45309','#7c3aed','#0284c7'][i]))
            fig.update_layout(title="Group Comparison Box Plot",
                              paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                              font_color='#111111', height=300,
                              yaxis=dict(gridcolor='#e2e8f0'))
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>📝 How to Report ANOVA Results</div>", unsafe_allow_html=True)
        st.markdown("""
#### APA-Style Reporting Format

> A one-way ANOVA revealed a statistically significant difference in [DV] across groups, *F*(df₁, df₂) = [F-value], *p* = [p-value].

**Example:**
> A one-way ANOVA revealed a statistically significant difference in test scores across the three teaching methods, *F*(2, 27) = 8.45, *p* = .001.

#### Post-Hoc Tests
When ANOVA rejects H₀, we know **at least one** group differs — but not **which** pairs differ. Use:

| Test | When to Use |
|------|------------|
| **Tukey's HSD** | Equal sample sizes, most common |
| **Bonferroni** | Conservative, any sample sizes |
| **Scheffe** | Most conservative, complex contrasts |
| **Games-Howell** | Unequal variances |

#### Effect Size
        """)
        st.latex(r"\eta^2 = \frac{\text{SSTR}}{\text{SST}} \quad \text{(proportion of variance explained)}")
        st.markdown("""
| η² | Interpretation |
|----|---------------|
| 0.01 – 0.06 | Small |
| 0.06 – 0.14 | Medium |
| > 0.14 | Large |

#### Checking Assumptions
1. **Levene's test** for equal variances (H₀: σ₁² = σ₂² = ... = σₖ²)
2. **Shapiro-Wilk test** for normality within each group
3. If assumptions violated → use **Kruskal-Wallis** (non-parametric alternative)
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
    st.markdown("<span class='prob-badge'>Problem 1</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Three fertilisers tested on crop yield (kg):
- Fertiliser A: 20, 22, 19, 24, 21
- Fertiliser B: 28, 30, 27, 29, 31
- Fertiliser C: 23, 25, 22, 26, 24

Test at α = 0.05 whether fertiliser type affects yield.
    """)
    a = np.array([20,22,19,24,21]); b = np.array([28,30,27,29,31]); c = np.array([23,25,22,26,24])
    f_s, p_s = stats.f_oneway(a, b, c)
    all_d = np.concatenate([a,b,c]); gm = all_d.mean()
    sstr_s = 5*(a.mean()-gm)**2 + 5*(b.mean()-gm)**2 + 5*(c.mean()-gm)**2
    sse_s = np.sum((a-a.mean())**2) + np.sum((b-b.mean())**2) + np.sum((c-c.mean())**2)
    st.latex(rf"\bar{{x}}_A={a.mean()},\;\bar{{x}}_B={b.mean()},\;\bar{{x}}_C={c.mean()},\;\bar{{x}}={gm:.2f}")
    st.latex(rf"\text{{SSTR}}={sstr_s:.2f},\;\text{{SSE}}={sse_s:.2f},\;\text{{SST}}={sstr_s+sse_s:.2f}")
    st.latex(rf"\text{{MSTR}}={sstr_s/2:.2f},\;\text{{MSE}}={sse_s/12:.2f},\;F={f_s:.4f}")
    st.latex(rf"p\text{{-value}}={p_s:.6f} < 0.05")
    eta_sq = sstr_s / (sstr_s + sse_s)
    st.markdown(f"**Reject H₀.** Fertiliser type significantly affects crop yield. η² = {eta_sq:.3f} (large effect).")
    st.markdown("</div>", unsafe_allow_html=True)
