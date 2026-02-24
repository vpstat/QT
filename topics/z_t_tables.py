import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📋 Z-Score & t-Score Tables</h1>
        <p>Complete reference tables with actual values for quick lookup.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 Z-Table (Standard Normal)", "📈 t-Table (Student's t)", "🧮 Value Lookup"])

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 1: Z-Table
    # ═══════════════════════════════════════════════════════════════════════════
    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 How to Read the Z-Table</div>", unsafe_allow_html=True)
        st.markdown("""
The Z-table gives **Φ(z) = P(Z ≤ z)** — the area to the **left** of z under the standard normal curve.

- **Row** = z value to one decimal (e.g. 1.9)
- **Column** = second decimal (e.g. 0.06)
- **Cell** = Φ(1.96) = 0.9750

**Useful conversions:**
- P(Z > z) = 1 − Φ(z)
- P(Z < −z) = 1 − Φ(z)  *(symmetry)*
- P(−a < Z < a) = 2Φ(a) − 1
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>📊 Standard Normal (Z) Table — Φ(z) = P(Z ≤ z)</div>", unsafe_allow_html=True)

        # Generate Z-table
        z_rows = np.arange(0.0, 3.5, 0.1)
        z_cols = np.arange(0.00, 0.10, 0.01)
        z_data = {}
        for c in z_cols:
            z_data[f".0{int(c*100)}" if c < 0.1 else f".{int(c*100)}"] = [
                f"{stats.norm.cdf(r + c):.4f}" for r in z_rows
            ]
        z_df = pd.DataFrame(z_data, index=[f"{r:.1f}" for r in z_rows])
        z_df.index.name = "z"
        st.dataframe(z_df, use_container_width=True, height=500)

        st.caption("This table shows positive z-values. For negative z: Φ(−z) = 1 − Φ(z)")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>⭐ Commonly Used Z Critical Values</div>", unsafe_allow_html=True)
        common_z = pd.DataFrame({
            'Confidence Level': ['80%', '90%', '95%', '98%', '99%', '99.5%', '99.9%'],
            'α': ['0.20', '0.10', '0.05', '0.02', '0.01', '0.005', '0.001'],
            'α/2': ['0.10', '0.05', '0.025', '0.01', '0.005', '0.0025', '0.0005'],
            'z* (one-tail)': ['0.842', '1.282', '1.645', '2.054', '2.326', '2.576', '3.090'],
            'z* (two-tail ±)': ['1.282', '1.645', '1.960', '2.326', '2.576', '2.807', '3.291'],
            'Φ(z*)': ['0.9000', '0.9500', '0.9750', '0.9900', '0.9950', '0.9975', '0.9995']
        })
        st.table(common_z)
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 2: t-Table
    # ═══════════════════════════════════════════════════════════════════════════
    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 How to Read the t-Table</div>", unsafe_allow_html=True)
        st.markdown("""
The t-table gives **critical values** for the Student's t-distribution.

- **Row** = degrees of freedom (df = n − 1)
- **Column** = upper-tail area (α for one-tailed, α/2 for two-tailed)
- **Cell** = t critical value

**Key differences from Z:**
- t-values are **always larger** than corresponding z-values (wider tails)
- As df → ∞, t-values converge to z-values
- df > 30 → t ≈ z (practical rule)
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>📈 Student's t Critical Values</div>", unsafe_allow_html=True)

        # Common alpha levels for columns
        alphas_one = [0.10, 0.05, 0.025, 0.01, 0.005, 0.001]
        dfs = list(range(1, 31)) + [35, 40, 50, 60, 80, 100, 200, 500]

        t_data = {}
        for a in alphas_one:
            col_label = f"α={a}"
            t_data[col_label] = [f"{stats.t.ppf(1-a, d):.3f}" for d in dfs]

        t_df = pd.DataFrame(t_data, index=[str(d) for d in dfs])
        t_df.index.name = "df"

        st.markdown("**Upper-tail critical values: t_{α, df}** (one-tailed α shown)")
        st.caption("For two-tailed tests, use α/2 column. E.g., two-tailed α=0.05 → use the α=0.025 column.")
        st.dataframe(t_df, use_container_width=True, height=500)

        st.markdown("---")
        st.markdown("##### Corresponding Z-values (df = ∞)")
        z_row = {f"α={a}": f"{stats.norm.ppf(1-a):.3f}" for a in alphas_one}
        st.table(pd.DataFrame(z_row, index=["z (df=∞)"]))
        st.caption("Notice how t-values decrease toward these z-values as df increases.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>⭐ Most-Used t Critical Values</div>", unsafe_allow_html=True)
        key_t = pd.DataFrame({
            'Scenario': [
                '95% CI, n=10 (df=9)',
                '95% CI, n=15 (df=14)',
                '95% CI, n=20 (df=19)',
                '95% CI, n=25 (df=24)',
                '95% CI, n=30 (df=29)',
                '99% CI, n=10 (df=9)',
                '99% CI, n=25 (df=24)',
                '99% CI, n=30 (df=29)',
            ],
            't* (two-tailed)': [
                f"{stats.t.ppf(0.975, 9):.3f}",
                f"{stats.t.ppf(0.975, 14):.3f}",
                f"{stats.t.ppf(0.975, 19):.3f}",
                f"{stats.t.ppf(0.975, 24):.3f}",
                f"{stats.t.ppf(0.975, 29):.3f}",
                f"{stats.t.ppf(0.995, 9):.3f}",
                f"{stats.t.ppf(0.995, 24):.3f}",
                f"{stats.t.ppf(0.995, 29):.3f}",
            ],
            'Corresponding z*': [
                '1.960', '1.960', '1.960', '1.960', '1.960',
                '2.576', '2.576', '2.576',
            ],
            'How much wider?': [
                f"{(stats.t.ppf(0.975, 9)/1.960 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.975, 14)/1.960 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.975, 19)/1.960 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.975, 24)/1.960 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.975, 29)/1.960 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.995, 9)/2.576 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.995, 24)/2.576 - 1)*100:.1f}%",
                f"{(stats.t.ppf(0.995, 29)/2.576 - 1)*100:.1f}%",
            ]
        })
        st.table(key_t)
        st.caption("The 'How much wider?' column shows how much larger the t* is compared to z* — this is the penalty for estimating σ.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 3: Lookup Tool
    # ═══════════════════════════════════════════════════════════════════════════
    with tab3:
        st.markdown("<div class='section-card'><div class='section-label label-solved'>🧮 Quick Value Lookup</div>", unsafe_allow_html=True)

        look_type = st.radio("What do you want to find?", [
            "Φ(z) — area given z-score",
            "z — score given area/probability",
            "t critical value given df and α",
            "P-value given t and df"
        ], key="lookup_type")

        if "Φ(z)" in look_type:
            z_in = st.number_input("Enter z-score:", value=1.96, step=0.01, key="lk_z")
            phi = stats.norm.cdf(z_in)
            col1, col2, col3 = st.columns(3)
            col1.metric(f"Φ({z_in}) = P(Z ≤ {z_in})", f"{phi:.6f}")
            col2.metric(f"P(Z > {z_in})", f"{1-phi:.6f}")
            col3.metric(f"P(-{abs(z_in)} < Z < {abs(z_in)})", f"{2*stats.norm.cdf(abs(z_in))-1:.6f}")

        elif "score given area" in look_type:
            area = st.number_input("Enter cumulative probability P(Z ≤ z):", value=0.975, min_value=0.0001, max_value=0.9999, step=0.001, key="lk_area")
            z_out = stats.norm.ppf(area)
            st.metric(f"z-score for P(Z ≤ z) = {area}", f"{z_out:.4f}")
            st.caption(f"This means {area*100:.2f}% of the standard normal distribution falls below z = {z_out:.4f}")

        elif "t critical" in look_type:
            col1, col2 = st.columns(2)
            with col1:
                df_lk = st.number_input("Degrees of freedom (df):", value=20, min_value=1, key="lk_df")
                alpha_lk = st.number_input("α (significance level):", value=0.05, min_value=0.001, max_value=0.50, step=0.005, key="lk_alpha")
                tail_lk = st.radio("Test type:", ["One-tailed", "Two-tailed"], key="lk_tail")
            with col2:
                if tail_lk == "One-tailed":
                    tc = stats.t.ppf(1 - alpha_lk, df_lk)
                    st.metric(f"t*({alpha_lk}, df={df_lk})", f"{tc:.4f}")
                else:
                    tc = stats.t.ppf(1 - alpha_lk/2, df_lk)
                    st.metric(f"t*({alpha_lk}/2, df={df_lk})", f"±{tc:.4f}")
                z_equiv = stats.norm.ppf(1 - alpha_lk/2) if tail_lk == "Two-tailed" else stats.norm.ppf(1-alpha_lk)
                st.metric("Corresponding z*", f"{z_equiv:.4f}")

        elif "P-value given t" in look_type:
            col1, col2 = st.columns(2)
            with col1:
                t_in = st.number_input("t-statistic:", value=2.10, step=0.01, key="lk_t")
                df_in = st.number_input("df:", value=15, min_value=1, key="lk_tdf")
                tail_in = st.radio("Tail:", ["Right (>)", "Left (<)", "Two-tailed (≠)"], key="lk_ttail")
            with col2:
                if "Right" in tail_in:
                    pv = 1 - stats.t.cdf(t_in, df_in)
                elif "Left" in tail_in:
                    pv = stats.t.cdf(t_in, df_in)
                else:
                    pv = 2 * (1 - stats.t.cdf(abs(t_in), df_in))
                st.metric("P-value", f"{pv:.6f}")
                for a in [0.01, 0.05, 0.10]:
                    if pv < a:
                        st.success(f"Reject H₀ at α={a}")
                    else:
                        st.warning(f"Fail to reject at α={a}")

        st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ──
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Z-Table Lookup</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Find P(Z > 1.75) and P(−1.2 < Z < 2.1).

**Solution:**
    """)
    st.latex(r"P(Z>1.75) = 1-\Phi(1.75) = 1-0.9599 = \mathbf{0.0401}")
    st.latex(r"P(-1.2<Z<2.1) = \Phi(2.1)-\Phi(-1.2) = 0.9821-0.1151 = \mathbf{0.8670}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — t-Table Lookup</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** For a 95% CI with n=12 (df=11), find the t critical value. How much larger is it than z*?
    """)
    t_ans = stats.t.ppf(0.975, 11)
    pct = (t_ans/1.960 - 1)*100
    st.latex(rf"t_{{0.025, 11}} = {t_ans:.3f} \quad \text{{vs}} \quad z_{{0.025}} = 1.960")
    st.markdown(f"The t* is **{pct:.1f}% larger** than z*, making the CI wider to account for uncertainty in estimating σ.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Finding z from probability</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** What z-score has 90% of the distribution below it?
    """)
    st.latex(rf"z = \Phi^{{-1}}(0.90) = {stats.norm.ppf(0.90):.4f}")
    st.markdown("This is the z-value used as the critical value for a one-tailed test at α=0.10.")
    st.markdown("</div>", unsafe_allow_html=True)
