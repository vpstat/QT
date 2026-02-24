import streamlit as st

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🧮 Formula Reference Sheet</h1>
        <p>Complete LaTeX reference of all quantitative techniques formulas — organized by category.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 How to Use</div>", unsafe_allow_html=True)
    st.markdown("""
This page is a **complete formula reference** for all topics covered in this guide.
Use the tabs below to navigate by category. Each formula is accompanied by a brief description of its purpose and variables.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📍 Center", "📏 Spread", "🎯 Z-Score", "🎲 Probability", "📐 Chebyshev", "🔔 Normal Dist."
    ])

    with tab1:
        st.markdown("### Measures of Central Tendency")
        formulas = [
            ("Population Mean", r"\mu = \frac{\sum_{i=1}^{N} x_i}{N}", "N = population size, xᵢ = observation"),
            ("Sample Mean", r"\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}", "n = sample size"),
            ("Weighted Mean", r"\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}", "wᵢ = weight of xᵢ"),
            ("Geometric Mean", r"G = \left(\prod_{i=1}^{n} x_i\right)^{1/n}", "Product of n values, n-th root"),
            ("Mean from Groups", r"\bar{x} = \frac{\sum f_i m_i}{\sum f_i}", "fᵢ = frequency, mᵢ = midpoint"),
            ("Median (odd n)", r"\text{Median} = x_{(n+1)/2}", "Middle ordered value"),
            ("Median (even n)", r"\text{Median} = \frac{x_{n/2} + x_{n/2+1}}{2}", "Average of two middle values"),
            ("Percentile Location", r"L_p = \frac{p}{100}(n+1)", "p = percentile, n = sample size"),
        ]
        for name, formula, desc in formulas:
            st.markdown(f"**{name}** — _{desc}_")
            st.latex(formula)
            st.markdown("---")

    with tab2:
        st.markdown("### Measures of Spread / Dispersion")
        formulas = [
            ("Range", r"\text{Range} = \text{Max} - \text{Min}", "Sensitive to outliers"),
            ("Population Variance", r"\sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}", "Divide by population size N"),
            ("Sample Variance", r"s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}", "Bessel's correction: divide by n−1"),
            ("Computational Variance", r"s^2 = \frac{n\sum x_i^2 - (\sum x_i)^2}{n(n-1)}", "Shortcut formula — avoids computing deviations"),
            ("Population SD", r"\sigma = \sqrt{\frac{\sum(x_i-\mu)^2}{N}}", "Square root of population variance"),
            ("Sample SD", r"s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}", "Square root of sample variance"),
            ("IQR", r"\text{IQR} = Q_3 - Q_1", "Middle 50% of data; outlier-resistant"),
            ("Coefficient of Variation", r"\text{CV} = \frac{s}{\bar{x}} \times 100\%", "Relative spread; allows cross-dataset comparison"),
            ("Mean Absolute Deviation", r"\text{MAD} = \frac{\sum |x_i - \bar{x}|}{n}", "Average absolute deviation"),
            ("Lower Outlier Fence", r"Q_1 - 1.5 \times \text{IQR}", "Tukey's mild outlier lower boundary"),
            ("Upper Outlier Fence", r"Q_3 + 1.5 \times \text{IQR}", "Tukey's mild outlier upper boundary"),
            ("Extreme Lower Fence", r"Q_1 - 3 \times \text{IQR}", "Extreme (severe) outlier lower boundary"),
            ("Variance from Groups", r"s^2 = \frac{\sum f_i(m_i - \bar{x})^2}{n-1}", "Grouped data variance"),
        ]
        for name, formula, desc in formulas:
            st.markdown(f"**{name}** — _{desc}_")
            st.latex(formula)
            st.markdown("---")

    with tab3:
        st.markdown("### Z-Score & Standardization")
        formulas = [
            ("Population Z-Score", r"z = \frac{x - \mu}{\sigma}", "How many σ above/below population mean"),
            ("Sample Z-Score", r"z = \frac{x - \bar{x}}{s}", "How many s above/below sample mean"),
            ("Unstandardize (Back-transform)", r"x = \mu + z \cdot \sigma", "Convert z-score back to original units"),
            ("Standardized Variable", r"Z = \frac{X - \mu}{\sigma}", "Z has mean 0, SD 1"),
            ("Sum of Z-Scores", r"\sum_{i=1}^{n} z_i = 0", "Always zero — fundamental identity"),
            ("Mean of Z-Scores", r"\bar{z} = 0 \text{ and } s_z = 1", "Properties of standardized data"),
            ("Outlier via Z-Score", r"|z| > 3 \Rightarrow \text{potential outlier}", "For roughly normal distributions"),
            ("Pearson's r via Z-Scores", r"r = \frac{1}{n-1}\sum_{i=1}^{n} z_{x_i} \cdot z_{y_i}", "Correlation as average product of z-scores"),
            ("Covariance", r"s_{xy} = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{n-1}", "Joint variation of X and Y"),
            ("Pearson's r", r"r = \frac{s_{xy}}{s_x \cdot s_y}", "Standardized covariance; −1 ≤ r ≤ 1"),
        ]
        for name, formula, desc in formulas:
            st.markdown(f"**{name}** — _{desc}_")
            st.latex(formula)
            st.markdown("---")

    with tab4:
        st.markdown("### Probability Rules")
        formulas = [
            ("Classical Probability", r"P(A) = \frac{n(A)}{n(S)}", "Equally likely outcomes"),
            ("Complement Rule", r"P(A^c) = 1 - P(A)", "Probability of A not occurring"),
            ("Addition Rule (General)", r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", "For any two events"),
            ("Addition Rule (Mut. Excl.)", r"P(A \cup B) = P(A) + P(B)", "When A and B cannot both occur"),
            ("Multiplication (General)", r"P(A \cap B) = P(A) \cdot P(B|A)", "General multiplication rule"),
            ("Multiplication (Independent)", r"P(A \cap B) = P(A) \cdot P(B)", "When A and B are independent"),
            ("Conditional Probability", r"P(A|B) = \frac{P(A \cap B)}{P(B)}", "Probability of A given B occurred"),
            ("Bayes' Theorem", r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}", "Reverse conditional probability"),
            ("Total Probability", r"P(B) = \sum_i P(B|A_i) \cdot P(A_i)", "Partition of sample space"),
            ("Independence Test", r"A \perp B \iff P(A \cap B) = P(A)P(B)", "Test for statistical independence"),
            ("Expected Value (Discrete)", r"E[X] = \sum_i x_i \cdot P(X=x_i)", "Mean of a random variable"),
            ("Variance of R.V.", r"\text{Var}(X) = E[X^2] - (E[X])^2", "Variance of a random variable"),
        ]
        for name, formula, desc in formulas:
            st.markdown(f"**{name}** — _{desc}_")
            st.latex(formula)
            st.markdown("---")

    with tab5:
        st.markdown("### Chebyshev's Inequality")
        formulas = [
            ("Chebyshev's Inequality", r"P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}", "For any distribution; k > 1"),
            ("Complement Form", r"P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}", "At least this proportion within k SDs"),
            ("k=2 Rule", r"P(|X-\mu| < 2\sigma) \geq 1 - \frac{1}{4} = 75\%", "At least 75% within 2 SDs"),
            ("k=3 Rule", r"P(|X-\mu| < 3\sigma) \geq 1 - \frac{1}{9} \approx 88.9\%", "At least 88.9% within 3 SDs"),
            ("k=4 Rule", r"P(|X-\mu| < 4\sigma) \geq 1 - \frac{1}{16} = 93.75\%", "At least 93.75% within 4 SDs"),
            ("General k", r"P(\mu - k\sigma < X < \mu + k\sigma) \geq 1 - \frac{1}{k^2}", "For any k > 1"),
            ("Solving for k", r"k = \frac{1}{\sqrt{1-p}} \text{ where p is desired proportion}", "Find k for a target coverage"),
        ]
        for name, formula, desc in formulas:
            st.markdown(f"**{name}** — _{desc}_")
            st.latex(formula)
            st.markdown("---")

    with tab6:
        st.markdown("### Normal Distribution")
        formulas = [
            ("Normal PDF", r"f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}", "Probability density function"),
            ("Standard Normal PDF", r"\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}", "μ=0, σ=1"),
            ("Standard Normal CDF", r"\Phi(z) = P(Z \leq z) = \int_{-\infty}^{z}\phi(t)\,dt", "Area under curve to left of z"),
            ("Symmetry Property", r"\Phi(-z) = 1 - \Phi(z)", "Standard normal symmetry"),
            ("Empirical Rule (68%)", r"P(\mu - \sigma < X < \mu + \sigma) \approx 0.6827", "68.27% within 1 SD"),
            ("Empirical Rule (95%)", r"P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 0.9545", "95.45% within 2 SDs"),
            ("Empirical Rule (99.7%)", r"P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 0.9973", "99.73% within 3 SDs"),
            ("X to Z Transform", r"Z = \frac{X - \mu}{\sigma}", "Standardize to N(0,1)"),
            ("Normal Sum", r"X+Y \sim \mathcal{N}(\mu_X+\mu_Y,\; \sigma_X^2+\sigma_Y^2)", "Sum of independent normals is normal"),
            ("Central Limit Theorem", r"\bar{X} \sim \mathcal{N}\!\left(\mu,\; \frac{\sigma^2}{n}\right) \text{ for large } n", "Sample mean approaches normality"),
        ]
        for name, formula, desc in formulas:
            st.markdown(f"**{name}** — _{desc}_")
            st.latex(formula)
            st.markdown("---")
