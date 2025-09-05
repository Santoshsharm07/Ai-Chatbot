import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# =========================
# 🔑 API Key Configuration
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except (KeyError, ValueError):
    st.error("⚠️ GOOGLE_API_KEY not found or is invalid! Please add it in Streamlit Secrets.")
    st.stop()

# =========================
# 🎨 Page Configuration
# =========================
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# ✨ Custom CSS for a more impactful UI
# =========================
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Hide the default Streamlit header/footer */
    #MainMenu, footer {
        visibility: hidden;
    }

    /* Chat input styling */
    .stChatInputContainer {
        background-color: #203a43;
        border-radius: 12px;
    }

    /* Chat message styling */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #4e54c8;
        color: white;
        border: none;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #6a11cb;
    }
    </style>
    """, unsafe_allow_html=True
)


# =========================
# 🤖 Model and Chat History Initialization
# =========================
# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# =========================
# 🖼️ Sidebar for Settings
# =========================
with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("🗑️ Clear Chat History"):
        st.session_state["messages"] = []
        st.rerun()
    st.markdown("---")
    st.write("🚀 Powered by Gemini & Streamlit")


# =========================
# 📜 Main Chat Interface
# =========================
st.title("💬 AI Chatbot")
st.caption("A smart assistant with image support")

# Display previous messages from history
for msg in st.session_state.messages:
    # Use Streamlit's native chat message component
    with st.chat_message(msg["role"], avatar="👤" if msg["role"] == "user" else "🤖"):
        # Display text content
        st.markdown(msg["content"])
        # Display image if it exists
        if "image" in msg:
            st.image(msg["image"], width=200)

# =========================
# ⌨️ User Input Handling
# =========================
# Create a container for the input elements for better layout
input_container = st.container()

with input_container:
    # Use columns to place the popover (+) button and chat input side-by-side
    col1, col2 = st.columns([1, 10])

    with col1:
        # The "+" button opens a popover for file uploads
        with st.popover("+", use_container_width=True):
            uploaded_file = st.file_uploader(
                "Upload an image...",
                type=["png", "jpg", "jpeg"],
                label_visibility="collapsed"
            )

    with col2:
        prompt = st.chat_input("What's on your mind?")

# Process the input when the user sends a message
if prompt or uploaded_file:
    # Handle image upload
    image_data = None
    if uploaded_file is not None:
        # Read the uploaded file into a PIL Image
        image_data = Image.open(uploaded_file)
        # If there's no text prompt, create a default one
        if not prompt:
            prompt = "Describe this image."

    # Add user message to session state and display it
    user_msg = {"role": "user", "content": prompt}
    if image_data:
        user_msg["image"] = image_data
    st.session_state.messages.append(user_msg)

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        if image_data:
            st.image(image_data, width=200)

    # =========================
    # 🧠 Generate AI Response
    # =========================
    with st.spinner("🤔 Thinking..."):
        try:
            # Prepare the content for the Gemini API
            # This now correctly handles both text and images
            content_to_send = [prompt]
            if image_data:
                content_to_send.append(image_data)
            
            # Call the model
            response = model.generate_content(content_to_send)
            reply = response.text

            # Add AI response to session state
            st.session_state.messages.append({"role": "assistant", "content": reply})

            # Display AI response
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(reply)

        except Exception as e:
            st.error(f"An error occurred: {e}")