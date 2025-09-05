# 🤖 AI Chatbot with Streamlit + Gemini API

An interactive chatbot built using **Google Gemini API** and **Streamlit**.  
This project provides a sleek chat interface where users can interact with an AI assistant in real time.

---

## ✨ Features
- 💬 Real-time AI conversations using **Gemini API**  
- 🎨 Beautiful UI with custom styling in Streamlit  
- 📜 Chat history saved in session state  
- ⚙️ Sidebar controls to reset chat  
- 🚀 Ready for deployment on **Streamlit Cloud**  

---

## 🛠️ Tech Stack
- **Python 3.9+**
- [Streamlit](https://streamlit.io/)
- [Google Generative AI SDK](https://ai.google.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚡ Installation & Setup

Clone the repository:

1. Local Development

Create a .env file in the project root and add:

GOOGLE_API_KEY=your_api_key_here

2. Streamlit Cloud Deployment

Go to Streamlit Cloud → Settings → Secrets and add:

GOOGLE_API_KEY="your_api_key_here"

▶️ Run the App
streamlit run app.py

🚀 Deployment on Streamlit Cloud

Push your code to GitHub

Go to Streamlit Cloud

Click New App → Connect your repo → Select app.py

Add your API Key in Secrets Management

Done 🎉 Your chatbot is live!
