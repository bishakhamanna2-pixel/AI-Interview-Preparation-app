import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import google.generativeai as genai
import os
from dotenv import load_dotenv

# STREAMLIT CONFIG
st.set_page_config(
    page_title="AI Interview Preparation System",
    layout="wide"
)

# GEMINI CONFIGURATION
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)

# SESSION STATE

if "scores" not in st.session_state:
    st.session_state.scores = {}

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# SIDEBAR
st.sidebar.title("AI Interview Preparation")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Student Profile",
        "Skill Assessment",
        "Dashboard",
        "Personalized Roadmap",
        "Interview Questions",
    ]
)

# HOME
if menu == "Home":

    st.title("AI Interview Preparation System")

    st.markdown("""
    ### Crack Technical Interviews with AI-Powered Analysis

    Analyze your skills, detect weak areas,
    generate interview questions,
    and build a smart learning roadmap.
    """)
    col1, col2, col3 = st.columns(3)

    col1.metric("Students Practicing", "100+")
    col2.metric("Questions Generated", "1000+")
    col3.metric("Success Rate", "97%")

    st.divider()

    st.subheader("Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📊 Skill Assessment")
        st.info("⚠ Weak Topic Detection")
        st.info("🛣 AI Learning Roadmap")

    with col2:
        st.info("💡 AI Interview Questions")
        st.info("📈 Progress Tracking")
        st.info("🤖 Interview Readiness Prediction")

# PROFILE
elif menu == "Student Profile":

    st.title("Student Profile")

    name = st.text_input("Enter your name")

    role = st.selectbox(
        "Preferred Role",
        [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "ML Engineer"
        ]
    )
    branch = st.selectbox(
        "Branch",
        [
            "BCA",
            "BTech",
            "MCA",
            "BSc(IT)",
            "MSc(IT)"
        ]
    )
    year = st.selectbox(
        "Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "Final Year"
        ]
    )
    if st.button("Save Profile"):

        st.session_state.student_name = name
        st.session_state.role = role
        st.success("Profile Saved Successfully")

# SKILL ASSESSMENT
elif menu == "Skill Assessment":

    st.title("Skill Assessment")
    st.markdown("Rate yourself out of 100")

    DSA = st.slider("DSA", 0, 100, 50)
    OOP = st.slider("OOP", 0, 100, 50)
    DBMS = st.slider("DBMS & SQL", 0, 100, 50)
    CC = st.slider("Cloud Computing", 0, 100, 50)
    AIML = st.slider("AI/ML", 0, 100, 50)
    os = st.slider("Operating System", 0, 100, 50)

    if st.button("Analyze Skills"):

        st.session_state.scores = {
            "DSA": DSA,
            "OOP": OOP,
            "DBMS": DBMS,
            "Cloud Computing": CC,
            "AI/ML": AIML,
            "OS": os
        }
        st.success("Skill Analysis Completed")
# DASHBOARD

elif menu == "Dashboard":

    st.title("Dashboard Analytics")

    if not st.session_state.scores:
        st.warning("Complete Skill Assessment first")

    else:

        scores = st.session_state.scores

        df = pd.DataFrame({
            "Topic": list(scores.keys()),
            "Score": list(scores.values())
        })

        avg_score = sum(scores.values()) / len(scores)

        weak_topics = [
            k for k, v in scores.items()
            if v < 50
        ]

        strong_topics = [
            k for k, v in scores.items()
            if v >= 75
        ]

        col1, col2, col3 = st.columns(3)

        col1.metric("Average Score", f"{avg_score:.2f}%")
        col2.metric("Weak Topics", len(weak_topics))
        col3.metric("Strong Topics", len(strong_topics))

        st.subheader("Topic Performance")

        fig, ax = plt.subplots(figsize=(7, 4))

        ax.bar(df["Topic"], df["Score"])

        plt.xticks(rotation=20)

        st.pyplot(fig)

        st.subheader("Weak Topics")

        if weak_topics:
            for topic in weak_topics:
                st.error(topic)
        else:
            st.success("No weak topics detected")

# PERSONALIZED ROADMAP

elif menu == "Personalized Roadmap":

    st.title("🎯 7-Day Personalized Roadmap")

    scores = st.session_state.get("scores", {})

    if not scores:

        st.warning("⚠️ Please complete the Skill Assessment first.")

    else:

        st.subheader("📊 Your Assessment Scores")
        st.write(scores)

        # Topics with score 50 or below
        weak_topics = [
            topic for topic, score in scores.items()
            if score <= 50
        ]

        if weak_topics:

            st.info(
                "Topics selected for improvement: "
                + ", ".join(weak_topics)
            )

        else:

            st.success(
                "🎉 Your scores are good. The roadmap will focus on revision and advanced practice."
            )

        if st.button("🚀 Generate 7-Day Roadmap"):

            prompt = f"""
You are a student learning mentor.

Create a SHORT 7-DAY personalized study roadmap based ONLY on the
student's assessment results below.

Student Role:
{st.session_state.get("role", "Student")}

Assessment Scores:
{scores}

Topics that need improvement:
{weak_topics}

IMPORTANT RULES:
- Do NOT introduce random subjects.
- Focus ONLY on the topics listed above.
- Do NOT give a long explanation.
- Do NOT create a 4-week roadmap.
- The roadmap must be exactly 7 days.
- Give only 2 or 3 tasks per day.
- Keep each day's plan short and practical.
- Include learning + small practice.
- Include revision on Day 7.
- Make it suitable for a college student preparing for interviews.
- Bold the words Day,Topic and learn
Use this exact format:

Day 1:
Topic:
Learn:
Practice:

Day 2:
Topic:
Learn:
Practice:

Day 3:
Topic:
Learn:
Practice:

Day 4:
Topic:
Learn:
Practice:

Day 5:
Topic:
Learn:
Practice:

Day 6:
Topic:
Learn:
Practice:

Day 7:
Topic:
Revision:
Practice:

At the end, give:
Interview Tip:
One short interview preparation tip related to the weak topics.

Keep the complete answer SHORT.
"""

            try:

                with st.spinner("🤖 Creating your 7-day roadmap..."):

                    response = gemini_model.generate_content(prompt)

                if response and response.text:

                    st.subheader("🗓️ Your 7-Day Roadmap")
                    st.markdown(response.text)

                else:

                    st.error("Gemini returned an empty response.")

            except Exception as e:

                st.error("❌ Gemini Error")
                st.code(str(e))
# INTERVIEW QUESTIONS

elif menu == "Interview Questions":

    st.title("AI Interview Question Generator")

    topic = st.text_input(
        "Topic",
        placeholder="Python, DBMS, SQL, React, DSA ,HR ..."
    )
    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        3,
        15,
        5
    )

    if st.button("Generate Questions"):

        try:

            prompt = f"""
            You are an expert interviewer.

            Generate {num_questions}
            interview questions.

            Topic: {topic}
            Difficulty: {difficulty}

            Requirements:
            - Questions only
            - Numbered format
            - No answers
            - Placement interview level
            """

            response = gemini_model.generate_content(
                prompt
            )

            st.subheader("Generated Questions")

            st.write(response.text)

        except Exception as e:

            st.error(
                f"Gemini Error: {e}"
            )