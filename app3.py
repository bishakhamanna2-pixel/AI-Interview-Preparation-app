import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import google.generativeai as genai

# =========================
# STREAMLIT CONFIG
# =========================

st.set_page_config(
    page_title="AI Interview Preparation System",
    layout="wide"
)

# =========================
# GEMINI CONFIGURATION
# =========================

GEMINI_API_KEY = " API_KEY "

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash")

# =========================
# SESSION STATE
# =========================

if "scores" not in st.session_state:
    st.session_state.scores = {}

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# =========================
# SIDEBAR
# =========================

st.sidebar.title("AI Interview Preparation")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Student Profile",
        "Skill Assessment",
        "Dashboard",
        "AI Roadmap",
        "Interview Questions",
        "Progress Tracker"
    ]
)

# =========================
# HOME
# =========================

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
    col3.metric("Success Rate", "87%")

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

# =========================
# PROFILE
# =========================

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

# =========================
# SKILL ASSESSMENT
# =========================

elif menu == "Skill Assessment":

    st.title("Skill Assessment")

    st.markdown("Rate yourself out of 100")

    arrays = st.slider("Arrays", 0, 100, 50)
    linked_list = st.slider("Linked List", 0, 100, 50)
    stack = st.slider("Stack", 0, 100, 50)
    queue = st.slider("Queue", 0, 100, 50)
    dbms = st.slider("DBMS", 0, 100, 50)
    os = st.slider("Operating System", 0, 100, 50)

    if st.button("Analyze Skills"):

        st.session_state.scores = {
            "Arrays": arrays,
            "Linked List": linked_list,
            "Stack": stack,
            "Queue": queue,
            "DBMS": dbms,
            "OS": os
        }

        st.success("Skill Analysis Completed")

# =========================
# DASHBOARD
# =========================

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

# =========================
# AI ROADMAP
# =========================

elif menu == "AI Roadmap":

    st.title("AI Learning Roadmap")

    if not st.session_state.scores:
        st.warning("Complete Skill Assessment first")

    else:

        scores = st.session_state.scores

        weak_topics = [
            k for k, v in scores.items()
            if v < 50
        ]

        if not weak_topics:
            st.success(
                "Excellent performance. Continue advanced practice."
            )

        else:

            if st.button("Generate AI Roadmap"):

                prompt = f"""
                Student Role:
                {st.session_state.role}

                Weak Topics:
                {weak_topics}

                Create a 4-week learning roadmap.

                Include:
                - Weekly plan
                - Resources
                - Practice strategy
                - Interview preparation tips
                """

                try:

                    response = gemini_model.generate_content(
                        prompt
                    )

                    st.write(response.text)

                except Exception as e:
                    st.error(str(e))

# =========================
# INTERVIEW QUESTIONS
# =========================

elif menu == "Interview Questions":

    st.title("AI Interview Question Generator")

    role = st.selectbox(
        "Select Role",
        [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "ML Engineer"
        ]
    )

    topic = st.text_input(
        "Topic",
        placeholder="Python, DBMS, SQL, React, DSA..."
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

            Role: {role}
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

# =========================
# PROGRESS TRACKER
# =========================

elif menu == "Progress Tracker":

    st.title("Progress Tracker")

    if not st.session_state.scores:
        st.warning(
            "Please complete Skill Assessment first"
        )

    else:

        scores = st.session_state.scores

        progress_df = pd.DataFrame(
            {
                "Topic": list(scores.keys()),
                "Current Score": list(scores.values()),
                "Target Score": [100] * len(scores)
            }
        )

        st.dataframe(progress_df)

        avg_score = (
            sum(scores.values())
            / len(scores)
        )

        X = [
            [20],
            [35],
            [45],
            [55],
            [65],
            [75],
            [85],
            [95]
        ]

        y = [
            "Low",
            "Low",
            "Medium",
            "Medium",
            "Good",
            "Good",
            "Excellent",
            "Excellent"
        ]

        clf = DecisionTreeClassifier()

        clf.fit(X, y)

        prediction = clf.predict(
            [[avg_score]]
        )

        st.subheader(
            "Interview Readiness"
        )

        st.success(
            f"Level: {prediction[0]}"
        )

        if prediction[0] == "Low":
            st.error(
                "You need more preparation."
            )

        elif prediction[0] == "Medium":
            st.warning(
                "Practice consistently."
            )

        elif prediction[0] == "Good":
            st.info(
                "Good preparation level."
            )

        else:
            st.success(
                "Excellent preparation level."
            )