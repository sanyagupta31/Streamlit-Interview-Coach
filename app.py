import streamlit as st
import google.generativeai as genai
import re
import datetime

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Interview Coach", page_icon="💡")
st.title("💡 One-Shot AI Interview Coach")

# Select role and number of questions
role = st.selectbox("Choose a Role", [
    "Software Engineer", "Data Scientist", "Product Manager", "Designer",
    "Data Analyst", "Machine Learning Engineer", "DevOps Engineer",
    "Cybersecurity Analyst", "Business Analyst", "Cloud Engineer"
])
n_questions = st.slider("Number of Questions", 1, 10, 2)

# Session state to store questions
if "questions" not in st.session_state:
    st.session_state.questions = []

# Generate interview questions
if st.button("🎯 Generate Interview Questions"):
    prompt = f"""Generate exactly {n_questions} technical interview questions for the role of {role}.
List each question starting with a number, like 1., 2., etc. Do NOT include explanations or headings."""
    response = model.generate_content(prompt)
    # Robust question extraction using regex
    questions_raw = re.findall(r"\d+\.\s.*?(?=\n\d+\.|$)", response.text.strip(), re.DOTALL)
    st.session_state.questions = questions_raw[:n_questions]

# Show questions and input fields
user_answers = []
if st.session_state.questions:
    st.subheader("📝 Interview Questions and Your Answers")
    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**Q{i+1}: {q}**")
        ans = st.text_area(f"Your Answer to Q{i+1}", key=f"answer_{i}")
        user_answers.append(ans)

    # Evaluate answers
    if st.button("🧠 Evaluate My Answers"):
        joined_questions = "\n".join([f"{i+1}. {q}" for i, q in enumerate(st.session_state.questions)])
        joined_answers = "\n".join([f"{i+1}. {a}" for i, a in enumerate(user_answers)])

        eval_prompt = f"""
You are a technical interviewer for the role of {role}.
Evaluate the candidate's answers to the following questions.

Questions:
{joined_questions}

Candidate Answers:
{joined_answers}

For each answer:
- Give a score out of 10
- Mention 2 strengths
- Suggest 2 improvements
If an answer is missing, skip its evaluation.
"""
        feedback = model.generate_content(eval_prompt)
        st.subheader("📋 AI Feedback on Your Answers")
        st.write(feedback.text)

        # Download feedback
        filename = f"{role}_interview_feedback_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        st.download_button("📥 Download Feedback", data=feedback.text, file_name=filename)

        # Score summary
        scores = re.findall(r"Score\s*[:\-]?\s*(\d+)/10", feedback.text)
        numeric_scores = [int(s) for s in scores if s.isdigit()]
        if numeric_scores:
            avg_score = sum(numeric_scores) / len(numeric_scores)
            st.metric(label="📊 Average Score", value=f"{avg_score:.1f}/10")

    # Show ideal answers (optional)
    if st.checkbox("✅ Show Ideal Answers"):
        joined_questions = "\n".join([f"{i+1}. {q}" for i, q in enumerate(st.session_state.questions)])
        ideal_prompt = f"""As an expert {role}, provide ideal answers to the following interview questions:

{joined_questions}"""
        ideal_response = model.generate_content(ideal_prompt)
        st.subheader("💼 Model Answers (Ideal)")
        st.write(ideal_response.text)
