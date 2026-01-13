import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .hero {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 100px;
        border-radius: 25px;
        color: white;
        text-align: center;
    }
    .hero h1 {
        font-size: 58px;
    }
    .hero p {
        font-size: 22px;
        opacity: 0.9;
    }
    </style>

    <div class="hero">
        <h1>💊 Drug Analysis Dashboard</h1>
        <p>Search • Compare • Analyze • Recommend</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 🚀 Available Features")
col1, col2, col3 = st.columns(3)

col1.success("🔍 Search Drugs")
col2.info("⚠ Side Effects Analysis")
col3.warning("🤰 Pregnancy Safety")
