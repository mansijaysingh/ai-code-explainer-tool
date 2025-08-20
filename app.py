import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain.llms import OpenAI 

load_dotenv()
app = Flask(__name__)

# The API key is automatically read from the environment
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)

@app.route("/", methods=["GET", "POST"])
def home():
    explanation = ""
    # 1. Initialize code_snippet to handle the initial page load
    code_snippet = "" 
    
    if request.method == "POST":
        language = request.form.get("language")
        # 2. Store the user's submitted code in the code_snippet variable
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
            
    # 3. Pass both the explanation AND the original code_snippet back to the page
    return render_template("index.html", explanation=explanation, code_snippet=code_snippet)

if __name__ == "__main__":
    app.run(debug=False)