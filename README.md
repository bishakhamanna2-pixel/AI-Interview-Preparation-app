# 🤖 AI Interview Preparation System

An AI-powered **Interview Preparation System** built with **Python, Streamlit, and Google Gemini API** to help students prepare for technical interviews through AI-generated questions, skill assessment, personalized feedback, and a structured learning roadmap.

---

## ✨ Features

* 🤖 AI-generated interview questions using Google Gemini
* 📝 Technical skill assessment
* 📊 Score and performance tracking
* 🎯 Personalized 7-Day Roadmap
* 💬 AI-based interview practice
* 📈 Progress tracking
* 📚 Preparation for important technical subjects
* 🎓 Student-friendly Streamlit interface

### 📚 Core Technical Subjects

1. **DSA**
2. **OOP**
3. **DBMS & SQL**
4. **Operating Systems**
5. **Computer Networks**
6. **Cloud Computing**

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Gemini API**
* **Pandas**
* **Matplotlib**
* **python-dotenv**

---

## 📁 Project Structure

```text
AI-Interview-Preparation-System/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> 🔐 `.env` is used locally and should **not** be uploaded to GitHub.

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/demohit37-jpg/AI-Interview-Preparation-System.git
cd AI-Interview-Preparation-System
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 3️⃣ Activate Virtual Environment

### Windows

```powershell
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Setup

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

**`.env` stores your Gemini API key securely as an environment variable instead of putting the key directly inside the Python code.**

⚠️ **Never upload your `.env` file or API key to GitHub.**

---

## 📦 Required Packages

The project uses:

```text
streamlit
pandas
matplotlib
scikit-learn
google-generativeai
python-dotenv
```

---

# ▶️ Run the Application

Make sure the virtual environment is activated, then run:

```bash
streamlit run app.py
```

Or:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

# 🔄 Application Workflow

1. 👤 Create Student Profile
2. 📝 Complete Skill Assessment
3. 📊 View Dashboard Analytics
4. 🎯 Generate AI Learning Roadmap
5. 🤖 Practice AI Interview Questions
6. 📈 Track Progress & Readiness

---

# 🤖 Machine Learning Model

The system uses a **Decision Tree Classifier** to predict interview readiness based on assessment scores.

| Score Range | Readiness Level |
| ----------- | --------------- |
| 0–35        | Low             |
| 36–55       | Medium          |
| 56–75       | Good            |
| 76–100      | Excellent       |


---

# 🎯 Expected Outcomes

* Improved interview readiness
* Personalized learning guidance
* Better technical preparation
* Enhanced confidence in placements
* Data-driven skill improvement

---

# 👨‍💻 Author

**Bishakha Manna**

**Project:** AI Interview Preparation System

