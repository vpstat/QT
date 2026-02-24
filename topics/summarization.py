import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📋 Data Summarization</h1>
        <p>Organizing and presenting data using tabular, graphical, and numerical techniques.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Raw data is rarely useful on its own. **Data summarization** transforms raw observations into understandable patterns through:

1. **Tabular methods** — organize data into tables (frequency tables, cross-tabs)
2. **Graphical methods** — visualize data (histograms, bar charts, pie charts)
3. **Numerical methods** — compute summary statistics (mean, median, SD, five-number summary)

The goal is to extract meaningful **signal** from noisy data.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋 Tabular Methods", "📊 Graphical Methods", "🔢 Numerical Methods"])

    with tab1:
        st.markdown("### Frequency Table")
        st.markdown("Counts how often each value (or range) occurs.")
        data = {
            'Score Range': ['50–60', '60–70', '70–80', '80–90', '90–100'],
            'Frequency (f)': [3, 7, 12, 10, 5],
            'Relative Freq (f/n)': ['0.081', '0.189', '0.324', '0.270', '0.135'],
            'Cumulative Freq': [3, 10, 22, 32, 37],
        }
        st.table(pd.DataFrame(data))
        st.markdown("### Cross-Tabulation (Contingency Table)")
        st.markdown("Shows the relationship between two categorical variables.")
        ct = pd.DataFrame({
            'Male': [15, 10],
            'Female': [12, 18],
        }, index=['Passed', 'Failed'])
        st.table(ct)

    with tab2:
        st.markdown("### Types of Graphical Summaries")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- **Bar Chart** — frequencies of categorical data
- **Pie Chart** — proportional representation
- **Histogram** — frequencies of quantitative data (grouped)
- **Ogive** — cumulative frequency curve
            """)
        with col2:
            st.markdown("""
- **Stem-and-Leaf Plot** — retains individual values
- **Box Plot** — five-number summary visual
- **Scatter Plot** — relationship between two variables
- **Line Chart** — trends over time
            """)

        # Interactive bar chart example
        categories = ['A', 'B', 'C', 'D', 'F']
        counts = [5, 12, 18, 8, 3]
        fig = go.Figure(go.Bar(
            x=categories, y=counts,
            marker_color=['#667eea','#764ba2','#56c8f5','#34d399','#fbbf24'],
            text=counts, textposition='outside'
        ))
        fig.update_layout(
            title="Grade Distribution (Bar Chart)",
            paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
            font_color='#111111', title_font_size=14,
            xaxis=dict(gridcolor='#e2e8f0'),
            yaxis=dict(gridcolor='#e2e8f0'),
            height=320
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("### Five-Number Summary")
        st.markdown("Quick numerical portrait of any dataset:")
        st.latex(r"\text{Min},\quad Q_1,\quad \text{Median}(Q_2),\quad Q_3,\quad \text{Max}")
        st.markdown("### Key Numerical Summaries")
        st.markdown("""
| Measure | Purpose |
|---------|---------|
| Mean | Center of data |
| Median | Middle value (robust to outliers) |
| Mode | Most frequent value |
| Range | Spread: Max − Min |
| Variance / SD | Spread around mean |
| IQR | Middle 50% spread (Q3 − Q1) |
        """)
        np.random.seed(42)
        sample = np.array([45, 52, 58, 60, 62, 65, 67, 68, 70, 72, 73, 75, 78, 80, 85, 90, 92, 55, 88, 76])
        st.markdown(f"""
**Example dataset (n=20):**  
Mean = `{np.mean(sample):.2f}`, Median = `{np.median(sample):.2f}`, SD = `{np.std(sample, ddof=1):.2f}`, IQR = `{np.percentile(sample,75)-np.percentile(sample,25):.2f}`
        """)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("**Q:** The scores of 10 students are: 55, 70, 65, 80, 75, 60, 90, 85, 70, 75. Construct a frequency table with class intervals of width 10.\n\n**Solution:**")
    ft = pd.DataFrame({
        'Class': ['50–60', '60–70', '70–80', '80–90', '90–100'],
        'Tally': ['II', 'II', 'IIII', 'II', 'I'],
        'Frequency': [2, 2, 4, 2, 1],
        'Rel. Freq': [0.20, 0.20, 0.40, 0.20, 0.10],
    })
    st.table(ft)
    st.markdown("Total = 10 (check: 0.20+0.20+0.40+0.20+0.10 = 1.00 ✅)")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A company surveys 50 employees on their preferred work mode (Remote/Hybrid/Office) and their department (Tech/Non-Tech). Results: Tech Remote=15, Tech Hybrid=8, Tech Office=2; Non-Tech Remote=5, Non-Tech Hybrid=12, Non-Tech Office=8. Build the contingency table and compute row percentages.

**Solution:**
    """)
    ct2 = pd.DataFrame({
        'Remote': [15, 5, 20],
        'Hybrid': [8, 12, 20],
        'Office': [2, 8, 10],
        'Total': [25, 25, 50]
    }, index=['Tech', 'Non-Tech', 'Total'])
    st.table(ct2)
    st.markdown("""
Row %: Tech → Remote 60%, Hybrid 32%, Office 8%  
Row %: Non-Tech → Remote 20%, Hybrid 48%, Office 32%  
→ Tech employees strongly prefer Remote; Non-Tech prefer Hybrid.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** From the frequency table below, compute: (a) the relative frequency, (b) the cumulative frequency, (c) which method — bar chart or histogram — is appropriate, and why?

| Class | Frequency |
|-------|-----------|
| 0–10  | 4         |
| 10–20 | 8         |
| 20–30 | 15        |
| 30–40 | 10        |
| 40–50 | 3         |

**Solution:**

(a) **Relative Frequency** = f / n (n = 40):
    0.10, 0.20, 0.375, 0.25, 0.075  
(b) **Cumulative Frequency**: 4, 12, 27, 37, 40  
(c) **Histogram** is appropriate — the data is *quantitative continuous* with class intervals. Bar charts are for categorical/discrete data with gaps between bars. Histograms have no gaps because the classes are continuous.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can a dataset have more than one mode? What if all values are unique — what is the mode?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Yes**, a dataset can be:
- **Unimodal**: one mode (most common case)
- **Bimodal**: two modes (e.g., exam scores cluster around 60 and 80)
- **Multimodal**: more than two modes

If **all values are unique** (no value repeats), the dataset has **no mode** (or every value is a mode — convention varies). This often signals you're working with continuous data, where a histogram with a peak is more informative than a mode.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** A pie chart shows that Department A has 40% and Department B has 60% of employees. Is it correct to say Department B has 1.5× as many employees as A? What information do you still not know?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Yes, the ratio 60%:40% = 1.5:1 is correct** — B has 1.5× as many employees as A.  
However, the pie chart tells you only **relative proportions**, not absolute counts.

**You cannot determine:**
- Total number of employees in the company
- Whether the company is growing or shrinking
- Any time-based trends

A pie chart is useful for showing **proportional composition at a single point in time**, but combining it with a table showing absolute counts provides fuller information.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
