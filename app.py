import streamlit as st
import pandas as pd
from chatbot import ask_chatbot



st.set_page_config(
    page_title="UPI AI Analytics Assistant",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- HEADER ----------
st.markdown("""
<style>
.big-title {
    font-size: 36px !important;
    font-weight: 700 !important;
    color: #4A90E2;
}
.sub {
    font-size: 18px !important;
    color: #666;
}
.chatbox {
    background-color: #F7F9FC;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #E0E6ED;
}
.responsebox {
    background-color: #E8F3FF;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #4A90E2;
}
</style>
""", unsafe_allow_html=True)



st.markdown("<p class='big-title'>💳 UPI Transaction AI Assistant</p>", unsafe_allow_html=True)
st.markdown("<p class='sub'>Ask anything about merchants, cities, spending, months, and patterns.</p>", unsafe_allow_html=True)
# Load data preview
df = pd.read_csv("data/Transaction details.csv")

with st.expander("View Dataset"):
    st.dataframe(df)

    

# ---------- CHAT AREA ----------
st.write("### 💬 Ask a question")

user_query = st.text_input("", placeholder="e.g., How much did I spend at Amazon in Mumbai?", label_visibility="collapsed")

if user_query:
    st.markdown("<div class='chatbox'>"+user_query+"</div>", unsafe_allow_html=True)

    with st.spinner("Analyzing data…"):
        response = ask_chatbot(user_query)

    st.markdown("<div class='responsebox'>"+response+"</div>", unsafe_allow_html=True)



# ---------- FOOTER ----------
st.markdown("---")
st.markdown("🔹 Built with Streamlit + OpenAI + Python • Designer: **Arundhati Thakur**")


