import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain.llms import OpenAI # Note the different import

load_dotenv()
app = Flask(__name__)

# With this library version, the API key is automatically read from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)

@app.route("/", methods=["GET", "POST"])
def home():
    explanation = ""
    if request.method == "POST":
        language = request.form.get("language")
        code_snippet = request.form.get("code_snippet")
        
        if code_snippet:
            # Create the prompt string
            prompt = f"""
            You are an expert code assistant. Your task is to explain the following {language} code snippet.
            Provide a structured explanation with a summary, line-by-line breakdown, and predicted output.
            Here is the code: ```{code_snippet}```
            """
            # Call the LLM directly
            explanation = llm(prompt)
            
    return render_template("index.html", explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)