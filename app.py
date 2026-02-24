import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Quantitative Techniques",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Background ── */
.stApp {
    background-color: #ffffff;
    color: #111111;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: #f5f7fa;
    border-right: 1px solid #dde3ec;
}
[data-testid="stSidebar"] .stRadio label {
    color: #333344 !important;
    font-size: 0.9rem;
    padding: 4px 0;
}
[data-testid="stSidebar"] .stRadio label:hover {
    color: #4f46e5 !important;
}

/* ── Topic header banner ── */
.topic-header {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    border-radius: 14px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 18px rgba(79,70,229,0.2);
}
.topic-header h1 { color: #fff; margin: 0; font-size: 1.9rem; font-weight: 700; }
.topic-header p  { color: rgba(255,255,255,0.88); margin: 0.4rem 0 0; font-size: 1rem; }

/* ── Section cards ── */
.section-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}
.section-label {
    font-size: 0.70rem;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    padding: 3px 10px;
    border-radius: 20px;
    display: inline-block;
}
.label-intro   { color: #0284c7; background: #e0f2fe; }
.label-concept { color: #7c3aed; background: #ede9fe; }
.label-solved  { color: #059669; background: #d1fae5; }
.label-tricky  { color: #b45309; background: #fef3c7; }

/* ── Home grid cards ── */
.home-card {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    transition: all 0.25s ease;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.home-card:hover {
    border-color: #4f46e5;
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(79,70,229,0.15);
}
.home-card .icon  { font-size: 2.2rem; }
.home-card .title { font-size: 0.95rem; font-weight: 600; color: #1e1b4b; margin-top: 0.5rem; }
.home-card .desc  { font-size: 0.75rem; color: #6b7280; margin-top: 0.3rem; }

/* ── Formula box ── */
.formula-box {
    background: #f8fafc;
    border-left: 4px solid #4f46e5;
    border-radius: 8px;
    padding: 1rem 1.4rem;
    margin: 0.8rem 0;
    font-family: 'JetBrains Mono', monospace;
}

/* ── Problem number badge ── */
.prob-badge {
    display: inline-block;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: white;
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
}
.tricky-badge {
    display: inline-block;
    background: linear-gradient(135deg, #dc2626, #b45309);
    color: white;
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
}

/* ── Divider ── */
hr { border-color: #e2e8f0 !important; }

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #f8fafc !important;
    border-radius: 8px !important;
    color: #1e1b4b !important;
}

/* ── General text ── */
p, li, td, th, label { color: #111111; }
h1, h2, h3, h4, h5, h6 { color: #1e1b4b; }
code { background: #f1f5f9; color: #1e40af; border-radius: 4px; padding: 1px 5px; }
</style>
""", unsafe_allow_html=True)

# ── Topic registry ────────────────────────────────────────────────────────────
TOPICS = [
    ("🏠", "Home",                             "home"),
    # ── Data & Summarization ──
    ("📦", "Data Types & Variables",            "data_types"),
    ("📋", "Data Summarization",               "summarization"),
    ("📊", "Frequency Distribution",           "frequency_distribution"),
    ("🔵", "Scatter Plots & Correlation",      "scatter_plots"),
    ("📏", "Measures of Spread",               "measures_spread"),
    ("📦", "Box Plot & Outliers",              "box_plot"),
    ("🎯", "Z-Score & Standardization",        "zscore"),
    # ── Probability ──
    ("🔵", "Sets & Venn Diagrams",             "sets_venn"),
    ("🎲", "Types of Probability & Events",    "probability_types"),
    ("🔀", "Conditional Probability",          "conditional_probability"),
    ("🔄", "Bayes' Theorem",                   "bayes_theorem"),
    ("🎲", "Probability Concepts (Advanced)",  "probability"),
    ("🔢", "Counting Rules",                   "counting_rules"),
    # ── Random Variables & Distributions ──
    ("🎰", "Random Variables",                 "random_variables"),
    ("➗", "Mean, Variance & IQR",             "mean_variance"),
    ("📊", "PMF, Expected Value & Discrete Uniform", "pmf_distributions"),
    # ── Advanced Topics ──
    ("📐", "Chebyshev's Inequality",           "chebyshev"),
    ("🔔", "Normal Distribution",              "normal_distribution"),
    # ── Reference ──
    ("🧮", "Formula Reference Sheet",          "formulas"),
]


# ── Sidebar navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 Quant Techniques")
    st.markdown("---")
    labels = [f"{icon}  {name}" for icon, name, _ in TOPICS]
    choice = st.radio("Navigate to:", labels, index=0, label_visibility="collapsed")
    selected_key = TOPICS[labels.index(choice)][2]
    st.markdown("---")
    st.markdown(
        "<small style='color:#556;'>📘 Each topic includes Introduction, "
        "Concepts, Solved Problems & Tricky Questions.</small>",
        unsafe_allow_html=True,
    )

# ── Page router ──────────────────────────────────────────────────────────────
if selected_key == "home":
    # ── Home page ──
    st.markdown("""
    <div class='topic-header'>
        <h1>📊 Quantitative Techniques</h1>
        <p>An interactive study guide covering statistics, probability & data analysis — from basics to advanced concepts.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 Choose a Topic to Study")
    st.markdown("")

    topics_for_grid = TOPICS[1:]  # skip Home
    cols_per_row = 3
    for i in range(0, len(topics_for_grid), cols_per_row):
        row = topics_for_grid[i:i+cols_per_row]
        cols = st.columns(cols_per_row)
        for j, (icon, name, _) in enumerate(row):
            with cols[j]:
                st.markdown(f"""
                <div class='home-card'>
                    <div class='icon'>{icon}</div>
                    <div class='title'>{name}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📖 Topics Covered", "12")
    with col2:
        st.metric("🧮 LaTeX Formulas", "50+")
    with col3:
        st.metric("✅ Solved Problems", "40+")

else:
    try:
        import importlib
        mod = importlib.import_module(f"topics.{selected_key}")
        mod.render()
    except ModuleNotFoundError:
        st.error(f"Topic module `topics/{selected_key}.py` not found.")
    except Exception as e:
        st.error(f"Error loading topic: {e}")
        import traceback
        st.code(traceback.format_exc())
