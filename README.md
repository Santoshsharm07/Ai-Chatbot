# 💬 AI Chatbot

A modern AI-powered chatbot built with Streamlit and Google Gemini API, supporting text and image inputs. Interact with the chatbot in a stylish web interface with live chat history.

---

## 🚀 Features

* Real-time AI chat powered by Google Gemini API.
* Upload images to include in your messages.
* Dynamic chat display with custom styling for user and assistant messages.
* Clear chat functionality.
* Responsive, modern UI with gradient background and styled chat bubbles.

---

## 🛠 Tech Stack

* Frontend & Backend: Streamlit
* AI API: Google Generative AI (Gemini)
* Image Handling: PIL / Pillow
* Language: Python 3.x

---

## ⚡ Installation

1. Clone the repository:

```
git clone https://github.com/Santoshsharm07/Ai-Chatbot.git
cd Ai-Chatbot
```

2. Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Set up Streamlit secrets:

* Create a file `.streamlit/secrets.toml` with your API key:

```
GOOGLE_API_KEY = "your_google_gemini_api_key"
```

---

## 🏃 Running the App

```
streamlit run app.py
```

* Open the URL shown in the terminal to interact with the chatbot.
* Upload images via the sidebar or type messages in the chat input box.

---

## 🎨 UI / UX

* Gradient background with white text.
* Custom chat bubbles for user (purple) and assistant (blue).
* Scrollable chat history container.
* Interactive sidebar for settings (clear chat, upload images).

---

## 📦 Folder Structure

```
Ai-Chatbot/
├─ app.py            # Main Streamlit app
├─ requirements.txt  # Python dependencies
├─ README.md         # Project documentation
└─ .streamlit/
   └─ secrets.toml   # API keys (not committed)
```

---

## 🔑 Notes

* Ensure you have a valid Google Generative AI API key to use the Gemini model.
* Compatible with Python 3.10+.
* Tested on Streamlit 1.30+.

---

## ⚡ Deployment

* Can be deployed on Streamlit Community Cloud for free.
* Click “Deploy” and connect your GitHub repository.
* Make sure to add secrets for `GOOGLE_API_KEY` in Streamlit Cloud.
