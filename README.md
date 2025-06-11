
````markdown
# 💡 Streamlit Interview Coach

An interactive AI-powered interview preparation app built with **Streamlit** and **Google Gemini API**. It allows users to practice mock interview questions tailored to their selected role, and receive personalized feedback on their answers.

👉 **Live App:** [Click here to try it out!](https://app-interview-coach-pxw2tcine4ajf8gbzvngvn.streamlit.app/)

---

## 🚀 Features

- ✅ Select a job role (e.g., Software Engineer, Data Scientist, etc.)
- ✅ Choose number of interview questions (1 to 10)
- ✅ AI-generated role-specific technical questions
- ✅ Write your answers directly in the app
- ✅ Get Gemini-based feedback with:
  - Score out of 10
  - 2 strengths
  - 2 suggestions for improvement

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web app framework  
- [Google Gemini API](https://ai.google.dev/) – Generative AI for questions & evaluation  
- Python

---

## 📦 Installation Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/sanyagupta31/Streamlit-Interview-Coach.git
cd Streamlit-Interview-Coach
````

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key

Create a file at `.streamlit/secrets.toml` and paste the following:

```toml
GEMINI_API_KEY = "your_actual_api_key_here"
```

> 🔐 Replace `"your_actual_api_key_here"` with your valid Gemini API key.

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📂 File Structure

```
.
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
└── .streamlit/
    └── secrets.toml         # Secure place for your API key
```

---

## 🔐 Security Note

⚠️ **Never push your `.streamlit/secrets.toml` to GitHub.**
Use `.gitignore` to keep it private, or securely manage secrets using [Streamlit Cloud Secrets Manager](https://docs.streamlit.io/streamlit-cloud/secrets-management).

---

## 🙋‍♀️ Author

**Sanya Gupta**
🔗 [GitHub](https://github.com/sanyagupta31) 
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```

---


```
