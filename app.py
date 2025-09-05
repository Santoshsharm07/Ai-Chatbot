import streamlit as st
import google.generativeai as genai
import os

# Initialize Google Generative AI
# =========================
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("⚠️ GOOGLE_API_KEY not found! Please add it in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# =========================
# 🎨 Streamlit Page Config
# =========================
st.set_page_config(
    page_title="💬 AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    .stChatMessage.user {
        background: #2a2a72;
        color: white;
    }
    .stChatMessage.assistant {
        background: #4e54c8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💬 AI Chatbot")
st.caption("Built with Streamlit + Gemini API 🚀")

# =========================
# 💾 Chat History (Session State)
# =========================
if "messages" not in st.session_state:
    st.session_state["messages"] = []   # No "system" role, Gemini doesn’t allow it

# =========================
# 📜 Display Chat History
# =========================
for msg in st.session_state["messages"]:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# =========================
# ⌨️ User Input
# =========================
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                # Gemini expects only text parts, no role
                response = model.generate_content(
                    [m["content"] for m in st.session_state["messages"]]
                )
                reply = response.text
                st.markdown(reply)
            except Exception as e:
                st.error(f"❌ Error: {e}")
                reply = "⚠️ Sorry, I couldn’t process your request."

    # Save assistant reply
    st.session_state["messages"].append({"role": "assistant", "content": reply})

# =========================
# 🧹 Sidebar Options
# =========================
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Manage your chatbot session.")
    if st.button("🗑️ Clear Chat"):
        st.session_state["messages"] = []
        st.experimental_rerun()

    st.markdown("---")
   
