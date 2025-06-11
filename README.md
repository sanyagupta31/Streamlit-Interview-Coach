

````markdown
<div align="center">
  <img src="https://img.shields.io/badge/Powered%20By-Google%20Gemini-ffaf00?style=for-the-badge&logo=google" alt="Gemini Badge">
  <img src="https://img.shields.io/badge/Made%20With-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge">
  <h1>💡 AI Interview Coach</h1>
  <p><strong>Practice. Improve. Succeed. 🚀</strong></p>
  <p>Get real-time interview questions and feedback using <strong>Gemini AI</strong> and <strong>Streamlit</strong></p>
  <a href="https://app-interview-coach-pxw2tcine4ajf8gbzvngvn.streamlit.app/">
    <img src="https://img.shields.io/badge/Try%20Live%20Demo-Click%20Here-brightgreen?style=for-the-badge" alt="Live Demo">
  </a>
</div>

---

## ✨ Features

- 🎯 Select your **job role** (e.g., Data Scientist, Cloud Engineer)
- 🧠 Get **technical interview questions** based on your role
- 📝 Type your answers within the app
- 🤖 Gemini evaluates with:
  - Score out of 10
  - 2 strengths
  - 2 improvement tips
- 🌐 Deployable to **Streamlit Cloud**

---

## 📸 Preview

> 📌 Add this later (optional):
> - Screenshot or GIF of your app in action here.

---

## 🛠️ Tech Stack

- 🔤 Python
- 🧠 [Google Gemini API](https://ai.google.dev/)
- 🌐 [Streamlit](https://streamlit.io/)
- 🔒 `.streamlit/secrets.toml` for API key management

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sanyagupta31/Streamlit-Interview-Coach.git
cd Streamlit-Interview-Coach
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key

Create a file at `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your_actual_api_key_here"
```

> ❗ **Do NOT share this file or upload it to GitHub.**

### 4. Run the App Locally

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push code to GitHub (excluding your secrets file).
2. Visit: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo.
4. Add your `GEMINI_API_KEY` in **App Settings > Secrets**.

---

## 🙋‍♀️ About Me

**Sanya Gupta**
🎓 BSc (Hons) CS & Data Analytics, IIT Patna
🔗 [GitHub](https://github.com/sanyagupta31) 

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

