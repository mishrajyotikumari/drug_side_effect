
import streamlit as st
from database import authenticate_user, init_db

init_db()   # ⭐ VERY IMPORTANT

st.set_page_config(page_title="Drug Analysis System", layout="wide")

# ---------- SESSION INIT ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ---------- LOGIN PAGE ----------
def login_page():
    st.markdown("<h1 style='text-align:center'>💊 Drug Analysis System</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>Login to continue</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid credentials")

# ---------- MAIN APP ----------
def main_app():
    st.sidebar.success(f"Logged in as {st.session_state.username}")

    st.title("Welcome 👋")
    st.info("Select a feature from the sidebar")

# ---------- ROUTING ----------
if not st.session_state.logged_in:
    st.sidebar.empty()   
    login_page()
else:
    main_app()
