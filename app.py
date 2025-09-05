import streamlit as st
import google.generativeai as genai
from PIL import Image

# =========================
# 🔑 API Initialization
# =========================
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("⚠️ GOOGLE_API_KEY not found! Please add it in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# =========================
# 🎨 Page Config
# =========================
st.set_page_config(
    page_title="💬 AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .chat-container {
        max-height: 70vh;
        overflow-y: auto;
        padding: 10px;
        border-radius: 10px;
        background: rgba(255,255,255,0.05);
        margin-bottom: 10px;
    }
    .user-message {
        background: #2a2a72;
        border-radius: 12px;
        padding: 10px;
        margin: 5px 0;
        color: white;
        max-width: 70%;
    }
    .assistant-message {
        background: #4e54c8;
        border-radius: 12px;
        padding: 10px;
        margin: 5px 0;
        color: white;
        max-width: 70%;
    }
    .stButton>button {
        background: #6a11cb;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("💬 AI Chatbot")
st.caption("Streamlit + Gemini API with image support 🚀")

# =========================
# 💾 Chat History
# =========================
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# =========================
# 🖼 Sidebar for Settings
# =========================
with st.sidebar:
    st.header("⚙️ Settings")
    uploaded_image = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
    if st.button("🗑️ Clear Chat"):
        st.session_state["messages"] = []
        st.experimental_rerun()
    st.markdown("---")
    st.write("Powered by Streamlit + Gemini API")

# =========================
# 📜 Display Chat History
# =========================
chat_container = st.container()
with chat_container:
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
            if "image" in msg:
                st.image(msg["image"], width=200)
        else:
            st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)
            if "image" in msg:
                st.image(msg["image"], width=200)

# =========================
# ⌨️ User Input
# =========================
with st.chat_input("Type your message...") as prompt_input:
    prompt = prompt_input

if prompt or uploaded_image:
    user_msg = {"role": "user", "content": prompt if prompt else ""}
    if uploaded_image:
        user_msg["image"] = uploaded_image
    st.session_state["messages"].append(user_msg)

    # Display user message immediately
    with chat_container:
        st.markdown(f'<div class="user-message">{user_msg["content"]}</div>', unsafe_allow_html=True)
        if uploaded_image:
            st.image(uploaded_image, width=200)

    # Generate AI response
    with st.spinner("🤔 Thinking..."):
        try:
            inputs = [m["content"] for m in st.session_state["messages"] if m["role"] == "user"]
            response = model.generate_content(inputs)
            reply = response.text
        except Exception as e:
            reply = f"⚠️ Error: {e}"

    st.session_state["messages"].append({"role": "assistant", "content": reply})
    with chat_container:
        st.markdown(f'<div class="assistant-message">{reply}</div>', unsafe_allow_html=True)
