import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📈 Regression & F-Test</h1>
        <p>Linear regression fundamentals, significance testing, and the overall F-test.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**Linear regression** models the relationship between a dependent variable Y and one or more independent variables X. The **F-test** assesses whether the overall regression model is statistically significant.

**Business applications:** Sales forecasting, pricing models, demand prediction, marketing ROI, risk modelling.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📐 Simple Linear Regression", "📊 F-Test & Significance", "🧮 Interactive Calculator"])

    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Simple Linear Regression</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Model")
            st.latex(r"\hat{y} = b_0 + b_1 x")
            st.latex(r"y_i = \beta_0 + \beta_1 x_i + \epsilon_i,\quad \epsilon_i \sim N(0, \sigma^2)")
            st.markdown("#### Least Squares Estimates")
            st.latex(r"b_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} = \frac{S_{xy}}{S_{xx}}")
            st.latex(r"b_0 = \bar{y} - b_1\bar{x}")
            st.markdown("#### Relationship to Correlation")
            st.latex(r"b_1 = r\,\frac{s_y}{s_x}")
        with col2:
            st.markdown("#### Decomposition of Variance")
            st.latex(r"\text{SST} = \text{SSR} + \text{SSE}")
            st.latex(r"\text{SST} = \sum(y_i - \bar{y})^2")
            st.latex(r"\text{SSR} = \sum(\hat{y}_i - \bar{y})^2 \quad\text{(explained)}")
            st.latex(r"\text{SSE} = \sum(y_i - \hat{y}_i)^2 \quad\text{(residual)}")
            st.markdown("#### Coefficient of Determination")
            st.latex(r"R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}} = r^2")
            st.caption("R² = proportion of variance in Y explained by X")
            st.markdown("#### Standard Error of Estimate")
            st.latex(r"s_e = \sqrt{\frac{\text{SSE}}{n-2}} = \sqrt{\text{MSE}}")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 F-Test for Overall Significance</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Hypotheses")
            st.latex(r"H_0: \beta_1 = 0 \quad (\text{no linear relationship})")
            st.latex(r"H_a: \beta_1 \neq 0 \quad (\text{relationship exists})")
            st.markdown("#### F-Statistic")
            st.latex(r"F = \frac{\text{MSR}}{\text{MSE}} = \frac{\text{SSR}/1}{\text{SSE}/(n-2)} \sim F_{1,\,n-2}")
            st.markdown("**Decision:** Reject H₀ if F > F_α,1,n-2 or p < α")
        with col2:
            st.markdown("#### Regression ANOVA Table")
            reg_anova = pd.DataFrame({
                'Source': ['Regression', 'Error', 'Total'],
                'SS': ['SSR', 'SSE', 'SST'],
                'df': ['1 (or p)', 'n−2 (or n−p−1)', 'n−1'],
                'MS': ['MSR = SSR/1', 'MSE = SSE/(n−2)', '—'],
                'F': ['MSR/MSE', '—', '—']
            })
            st.table(reg_anova)
            st.markdown("#### t-Test for Individual b₁")
            st.latex(r"t = \frac{b_1}{s_{b_1}} = \frac{b_1}{s_e / \sqrt{S_{xx}}}")
            st.caption("In simple regression: t² = F (equivalent tests)")

        st.markdown("---")
        st.markdown("#### Assumptions (LINE)")
        st.markdown("""
1. **L**inearity — relationship is linear
2. **I**ndependence — residuals are independent
3. **N**ormality — residuals are normally distributed
4. **E**qual variance — homoscedasticity (constant σ²)

Check via: **residual plots**, **Q-Q plot**, **Durbin-Watson test**
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<div class='section-card'><div class='section-label label-solved'>🧮 Interactive Simple Regression</div>", unsafe_allow_html=True)
        st.markdown("Enter X and Y values (comma-separated):")
        col1, col2 = st.columns(2)
        with col1:
            x_str = st.text_input("X values:", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
            y_str = st.text_input("Y values:", "2.5, 5.1, 7.2, 8.8, 11.5, 13.2, 15.8, 17.9, 20.1, 22.3")

        try:
            x = np.array([float(v.strip()) for v in x_str.split(',')])
            y = np.array([float(v.strip()) for v in y_str.split(',')])
            if len(x) == len(y) and len(x) >= 3:
                n = len(x)
                slope, intercept, r_val, p_val, se_slope = stats.linregress(x, y)
                y_hat = intercept + slope * x
                sst = np.sum((y - y.mean())**2)
                ssr = np.sum((y_hat - y.mean())**2)
                sse = np.sum((y - y_hat)**2)
                r_sq = ssr / sst
                msr = ssr / 1
                mse = sse / (n - 2)
                f_stat = msr / mse
                p_f = 1 - stats.f.cdf(f_stat, 1, n-2)

                with col2:
                    st.metric("b₁ (slope)", f"{slope:.4f}")
                    st.metric("b₀ (intercept)", f"{intercept:.4f}")
                    st.metric("R²", f"{r_sq:.4f}")
                    st.metric("F-statistic", f"{f_stat:.4f}")
                    st.metric("p-value (F-test)", f"{p_f:.6f}")

                reg_table = pd.DataFrame({
                    'Source': ['Regression', 'Error', 'Total'],
                    'SS': [f"{ssr:.4f}", f"{sse:.4f}", f"{sst:.4f}"],
                    'df': [1, n-2, n-1],
                    'MS': [f"{msr:.4f}", f"{mse:.4f}", "—"],
                    'F': [f"{f_stat:.4f}", "—", "—"],
                    'p-value': [f"{p_f:.6f}", "—", "—"]
                })
                st.table(reg_table)

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data',
                                          marker=dict(color='#4f46e5', size=10)))
                x_line = np.linspace(x.min(), x.max(), 100)
                fig.add_trace(go.Scatter(x=x_line, y=intercept + slope*x_line, mode='lines',
                                          name=f'ŷ = {intercept:.2f} + {slope:.2f}x',
                                          line=dict(color='#dc2626', width=3)))
                fig.update_layout(title=f"Regression: R² = {r_sq:.4f}, p = {p_f:.6f}",
                                  paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                                  font_color='#111111', height=350,
                                  xaxis=dict(gridcolor='#e2e8f0', title='X'),
                                  yaxis=dict(gridcolor='#e2e8f0', title='Y'))
                st.plotly_chart(fig, use_container_width=True)

                alpha_r = 0.05
                if p_f < alpha_r:
                    st.success(f"**F-test: Reject H₀ at α=0.05.** The linear relationship is statistically significant (R²={r_sq:.3f}).")
                else:
                    st.warning(f"**F-test: Fail to reject H₀.** No significant linear relationship (R²={r_sq:.3f}).")
        except:
            st.warning("Check inputs — equal number of comma-separated X and Y values.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
    st.markdown("<span class='prob-badge'>Problem 1 — Full Regression Analysis</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Advertising spend (₹'000) and sales (units):

| Ad Spend (X) | 10 | 20 | 30 | 40 | 50 |
|-------------|----|----|----|----|-----|
| Sales (Y) | 25 | 42 | 58 | 70 | 90 |

Find regression line, R², and test significance at α = 0.05.
    """)
    xp = np.array([10,20,30,40,50]); yp = np.array([25,42,58,70,90])
    sl, ic, rv, pv, seslope = stats.linregress(xp, yp)
    yh = ic + sl*xp; sstp = np.sum((yp-yp.mean())**2); ssrp = np.sum((yh-yp.mean())**2)
    ssep = np.sum((yp-yh)**2); r2p = ssrp/sstp; fp = (ssrp/1)/(ssep/3)
    pfp = 1-stats.f.cdf(fp, 1, 3)
    st.latex(rf"b_1 = {sl:.2f},\quad b_0 = {ic:.2f}")
    st.latex(rf"\hat{{y}} = {ic:.2f} + {sl:.2f}x")
    st.latex(rf"R^2 = {r2p:.4f},\quad F = {fp:.4f},\quad p = {pfp:.6f}")
    st.markdown(f"**Conclusion:** R² = {r2p:.3f} → {r2p*100:.1f}% of sales variation explained by ad spend. F-test p = {pfp:.6f} < 0.05 → **significant linear relationship.** Each ₹1000 increase in ad spend is associated with ~{sl:.1f} additional units sold.")
    st.markdown("</div>", unsafe_allow_html=True)
