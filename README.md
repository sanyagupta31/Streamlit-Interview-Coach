
````markdown
# 💡 AI Interview Coach

An interactive web app to practice mock interviews, get personalized AI feedback, and improve your answers — powered by Google Gemini and Streamlit.

🔗 **Live App:** [Click here to try](https://app-interview-coach-pxw2tcine4ajf8gbzvngvn.streamlit.app/)  
📁 **GitHub Repo:** https://github.com/sanyagupta31/Streamlit-Interview-Coach

---

## ✨ Features

- Choose from 10 different job roles (e.g. Software Engineer, Data Scientist, etc.)
- Generate realistic technical interview questions
- Write your own answers to each question
- Get smart AI feedback:
  - Score out of 10
  - 2 strengths
  - 2 suggestions for improvement

---

## 🚀 How to Run Locally

### 1. Clone this repository

```bash
git clone https://github.com/sanyagupta31/Streamlit-Interview-Coach.git
cd Streamlit-Interview-Coach
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a file at `.streamlit/secrets.toml` and paste:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

> ⚠️ Do **NOT** push this file to GitHub.

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🌐 How to Deploy on Streamlit Cloud

1. Push your code to GitHub (excluding `.streamlit/secrets.toml`)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **New app** → Connect your GitHub repo
4. Under **Advanced settings → Secrets**, paste:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
```

5. Click **Deploy**

---

## 🛠️ Built With

* Python
* Streamlit
* Google Generative AI (Gemini 1.5 Flash)

---

## 🙋‍♀️ About the Creator

**Sanya Gupta**
BSc (Hons) Computer Science & Data Analytics, IIT Patna
GitHub: [@sanyagupta31](https://github.com/sanyagupta31)
LinkedIn: [linkedin.com/in/sanyagupta31](https://www.linkedin.com/in/sanyagupta31)

---

## 📄 License

This project is open-source under the MIT License.

```

---

```
