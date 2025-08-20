# AI Code Explainer 🧑‍💻

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2-black.svg)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-green.svg)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-purple.svg)](https://openai.com/)

A simple yet powerful web application built with Flask and LangChain that leverages Large Language Models (LLMs) to explain complex code snippets in a clear, structured, and easy-to-understand format.

## 🚀 Live Demo

**Check out the live version of the app deployed on Render:**

[**https://your-app-name.onrender.com**]([https://your-app-name.onrender.com](https://ai-code-explainer-tool.onrender.com))

*(Note: Free Render instances may take a minute to spin up if they've been inactive.)*

---

## 📸 Screenshot

![App Screenshot](<img width="1192" height="879" alt="image" src="https://github.com/user-attachments/assets/cf508714-d8a6-4343-a129-5bdf1a38d5b2" />
)

---

## ✨ Key Features

* **Structured Explanations**: Get a clear summary, line-by-line breakdown, and predicted output for any code snippet.
* **Multi-Language Support**: Supports over 15 popular programming languages, selectable from a user-friendly dropdown.
* **Interactive UI**: The submitted code is retained in the text box for easy reference and modification.
* **Smart Controls**: A "Clear" button dynamically appears when there's text, allowing users to easily clear the input and output.
* **Modern Frontend**: A clean, responsive, and visually appealing UI with a "glassmorphism" design for a premium feel.

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask, Gunicorn
* **AI/LLM**: LangChain, OpenAI API
* **Frontend**: HTML, CSS, JavaScript

---

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-code-explainer-tool.git](https://github.com/your-username/ai-code-explainer-tool.git)
    cd ai-code-explainer-tool
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create
    python -m venv venv
    # Activate (Windows)
    venv\Scripts\activate
    # Activate (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    * Create a file named `.env` in the root directory.
    * Add your OpenAI API key to this file:
        ```
        OPENAI_API_KEY="sk-YourSecretKeyGoesHere"
        ```

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.
