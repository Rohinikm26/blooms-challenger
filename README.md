# 🌻 Bloom's Challenger (The Socratic Garden)

[![Track](https://img.shields.io/badge/Track-Agents_for_Good-green)](https://www.kaggle.com/competitions/agents-intensive-capstone-project)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Model](https://img.shields.io/badge/AI-Google_Gemini_1.5_Flash-orange)](https://deepmind.google/technologies/gemini/)

> **"An AI gym for your brain: sequential agents debate you, prune fallacies, and force your logic to grow from simple recall to deep analysis."**

---

## 📖 Table of Contents
- [Problem Statement](#-problem-statement)
- [Why Agents?](#-why-agents)
- [The Solution](#-the-solution)
- [Architecture](#-architecture)
- [Demo](#-demo-transcript)
- [The Build](#-the-build)
- [Installation](#-installation)
- [Future Roadmap](#-future-roadmap)

---

## 🚩 Problem Statement
In the age of information overload and generative AI, **lazy thinking** and **surface-level understanding** are becoming critical issues. 
- Students and lifelong learners often struggle to move beyond simple recall of facts (the lowest level of Bloom's Taxonomy) to true critical analysis and evaluation.
- Traditional AI tutors often just "give the answer," which reinforces passivity rather than intellectual growth.
- **Cognitive Atrophy:** Without active challenge, critical thinking muscles weaken, leaving people vulnerable to misinformation and logical fallacies.

**The Educational Gap:** There is a lack of accessible tools that act as "Socratic partners"—mentors who force you to defend your ideas rather than just correcting your grammar.

---

## 🤖 Why Agents?
Standard LLMs (like ChatGPT) are passive and people-pleasing. If a user argues poorly, the LLM often politely agrees to avoid conflict. This fails to solve the problem of "lazy thinking."

**Bloom's Challenger** solves this using a **Multi-Agent System**:

1.  **Goal-Oriented Autonomy:** Unlike a chatbot that just "chats," this system has a specific goal: *Push the user up Bloom's Taxonomy.* It doesn't stop until it detects cognitive depth.
2.  **Specialization:**
    * **The Challenger Agent** is optimized for engagement and debate.
    * **The Evaluator Agent** is optimized for objective judgment and metrics (Pass/Fail).
    * *Why this matters:* Splitting them ensures one agent stays "in character" while the other remains an unbiased referee.
3.  **Tool Use (The Logic Pruner):** The agent actively uses a **Custom Tool** (Fallacy Checker) to "scan" arguments objectively before responding.
4.  **State Management:** Critical thinking is a process. The agents track a "Game State" (e.g., Round 1 of 3) to enforce a rigorous educational workflow.

---

## 💡 The Solution
I created **Bloom's Challenger**, a **Sequential Multi-Agent System** designed to gamify critical thinking. 

Unlike a standard chatbot, this system uses two specialized AI agents working in tandem to:
1.  Actively **debate** the user.
2.  **Detect** logical fallacies using custom tools.
3.  **Measure** cognitive growth based on Bloom's Taxonomy.

---

## 🏗 Architecture
The system follows a **Human-in-the-Loop Sequential Architecture**.

```mermaid
graph TD
    User[👤 User Input] --> Tool[🛠️ Tool: Logic Pruner]
    Tool -- "JSON Report (Fallacies Found)" --> AgentA
    
    subgraph "The Brain (Sequential Agents)"
        AgentA[🌻 Agent 1: The Challenger]
        AgentA -- "Socratic Response" --> UI[💬 Streamlit Interface]
        
        UI --> AgentB[⚖️ Agent 2: The Evaluator]
        AgentB -- "Analyzes History" --> State{Check State}
    end
    
    State -- "Growth Detected (3 Rounds)" --> Win[🏆 WIN STATE: Full Bloom]
    State -- "Fallacies/Weak Logic" --> Lose[🥀 LOSE STATE: Withered]
    State -- "Keep Going" --> Loop[🔄 Continue Debate]
    Here is your complete, professional README.md file.

I have formatted it with GitHub-ready Markdown, including a Mermaid.js diagram for your architecture (which renders automatically on GitHub) and professional badges.

Instructions:
Create a file named README.md in your project folder.

Copy the code block below exactly.

Paste it into the file and save.

Markdown

# 🌻 Bloom's Challenger (The Socratic Garden)

[![Track](https://img.shields.io/badge/Track-Agents_for_Good-green)](https://www.kaggle.com/competitions/agents-intensive-capstone-project)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)](https://streamlit.io/)
[![Model](https://img.shields.io/badge/AI-Google_Gemini_1.5_Flash-orange)](https://deepmind.google/technologies/gemini/)

> **"An AI gym for your brain: sequential agents debate you, prune fallacies, and force your logic to grow from simple recall to deep analysis."**

---

## 📖 Table of Contents
- [Problem Statement](#-problem-statement)
- [Why Agents?](#-why-agents)
- [The Solution](#-the-solution)
- [Architecture](#-architecture)
- [Demo](#-demo-transcript)
- [The Build](#-the-build)
- [Installation](#-installation)
- [Future Roadmap](#-future-roadmap)

---

## 🚩 Problem Statement
In the age of information overload and generative AI, **lazy thinking** and **surface-level understanding** are becoming critical issues. 
- Students and lifelong learners often struggle to move beyond simple recall of facts (the lowest level of Bloom's Taxonomy) to true critical analysis and evaluation.
- Traditional AI tutors often just "give the answer," which reinforces passivity rather than intellectual growth.
- **Cognitive Atrophy:** Without active challenge, critical thinking muscles weaken, leaving people vulnerable to misinformation and logical fallacies.

**The Educational Gap:** There is a lack of accessible tools that act as "Socratic partners"—mentors who force you to defend your ideas rather than just correcting your grammar.

---

## 🤖 Why Agents?
Standard LLMs (like ChatGPT) are passive and people-pleasing. If a user argues poorly, the LLM often politely agrees to avoid conflict. This fails to solve the problem of "lazy thinking."

**Bloom's Challenger** solves this using a **Multi-Agent System**:

1.  **Goal-Oriented Autonomy:** Unlike a chatbot that just "chats," this system has a specific goal: *Push the user up Bloom's Taxonomy.* It doesn't stop until it detects cognitive depth.
2.  **Specialization:**
    * **The Challenger Agent** is optimized for engagement and debate.
    * **The Evaluator Agent** is optimized for objective judgment and metrics (Pass/Fail).
    * *Why this matters:* Splitting them ensures one agent stays "in character" while the other remains an unbiased referee.
3.  **Tool Use (The Logic Pruner):** The agent actively uses a **Custom Tool** (Fallacy Checker) to "scan" arguments objectively before responding.
4.  **State Management:** Critical thinking is a process. The agents track a "Game State" (e.g., Round 1 of 3) to enforce a rigorous educational workflow.

---

## 💡 The Solution
I created **Bloom's Challenger**, a **Sequential Multi-Agent System** designed to gamify critical thinking. 

Unlike a standard chatbot, this system uses two specialized AI agents working in tandem to:
1.  Actively **debate** the user.
2.  **Detect** logical fallacies using custom tools.
3.  **Measure** cognitive growth based on Bloom's Taxonomy.

---

## 🏗 Architecture
The system follows a **Human-in-the-Loop Sequential Architecture**.

```mermaid
graph TD
    User[👤 User Input] --> Tool[🛠️ Tool: Logic Pruner]
    Tool -- "JSON Report (Fallacies Found)" --> AgentA
    
    subgraph "The Brain (Sequential Agents)"
        AgentA[🌻 Agent 1: The Challenger]
        AgentA -- "Socratic Response" --> UI[💬 Streamlit Interface]
        
        UI --> AgentB[⚖️ Agent 2: The Evaluator]
        AgentB -- "Analyzes History" --> State{Check State}
    end
    
    State -- "Growth Detected (3 Rounds)" --> Win[🏆 WIN STATE: Full Bloom]
    State -- "Fallacies/Weak Logic" --> Lose[🥀 LOSE STATE: Withered]
    State -- "Keep Going" --> Loop[🔄 Continue Debate]
1. The Agents
Agent A: The Challenger ("The Socratic Gardener")

Role: Rigorous debate partner.

Tool: Logic Pruner (scans for Ad Hominem, Strawman, etc.).

Agent B: The Evaluator ("The Inspector")

Role: Invisible referee.

Logic: Enforces a State Machine rule (User must survive 3 rounds).

2. State Management
Uses st.session_state to persist conversation history and round counts across the multi-turn debate.

🗣️ Demo Transcript
A real example of the system pruning weak logic:

OUTPUT :

🌱 Plant your idea: "AI agents like you will eventually make human teachers obsolete."

[SYSTEM]: Garden initialized.

👤 You: "AI will replace all teachers."

[TOOL] 🍂 Scanning for dead branches... -> ⚠️ Detected: Sweeping Generalization (Dicto Simpliciter)

🌻 Challenger: "That is a potent seed of an idea, but sweeping generalizations often stunt conceptual growth. To prune this statement, let’s analyze the roots: What specific, irreducible teaching functions—like emotional mediation—would AI find truly impossible to replicate?"

--- Growth Stage 1 Complete ---

👤 You: "Yes, because AI knows everything."

[TOOL] 🍂 Scanning for dead branches... -> ⚠️ Detected: Appeal to False Authority

🌻 Challenger: "That's a beautiful, yet brittle, leaf of logic. We must distinguish between raw information retrieval and true pedagogical knowing. How would the AI assess a student's emotional readiness?"

⚖️  Evaluator is measuring growth...
--- Growth Stage 2 Complete ---


🗣️  You: AI is learning 

🌻 Bloom's Challenger is analyzing root structure...

[TOOL] 🍂 Scanning for dead branches (fallacies) in: 'AI is learning ...'

🌻 Challenger: That is a wonderful observation—the AI seedling is certainly growing! For deeper analysis, differentiate for me: Is the machine's 'learning' based solely on statistical optimization and pattern fitting, or does it incorporate the subjective, ethical wisdom required to mentor a developing human being?

⚖️  Evaluator is measuring growth...
--- Growth Stage 3 Complete ---


🗣️  You: how can i say it

🌻 Challenger: This is the critical juncture where we choose the right words to cultivate understanding. Try contrasting the AI's goal—statistical optimization and pattern recognition for *efficiency*—against the human teacher's imperative: ethical wisdom and character development for *flourishing*. How do those opposing primary objectives fundamentally alter the teaching outcome?

⚖️  Evaluator is measuring growth...

🥀 WITHERED. Your argument could not sustain growth.

🛠 The Build
Built as a lightweight but robust Python application.

Core Logic: Python 3.x

AI Model: Google Gemini 1.5 Flash (Chosen for speed/stability)

SDK: google-genai

Security: python-dotenv for API key management

🚀 Installation
Clone the repository

Bash

git clone [https://github.com/yourusername/blooms-challenger.git](https://github.com/yourusername/blooms-challenger.git)
cd blooms-challenger
Install dependencies

Bash

pip install -r requirements.txt
Set up API Key Create a .env file in the root directory:

Bash

GOOGLE_API_KEY=your_api_key_here
Run the Application

Bash

python blooms_challenger.py

🔮 Future Roadmap
If I had more time, this is what I'd do:

Integrate "Grounding" with Google Search: Add a tool to fact-check user claims in real-time, preventing them from "winning" with made-up statistics.

Long-Term Memory: Implement a Vector Database (ChromaDB) to track a user's debate history over weeks (e.g., "You're getting better at avoiding Strawman arguments!").

Voice-to-Voice Debate: Enable Audio Input/Output so users can practice verbal argumentation.

Visual "Garden" Generation: Use Imagen 3 to generate a dynamic image of a plant that blooms or withers based on the debate quality.