import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

app=Flask(__name__)

openai_api_key=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.7)


prompt=PromptTemplate(
  input_variables=["language", "code_snippet"],
    template="""
    You are an expert code assistant. Your task is to explain the following {language} code snippet in a clear and easy-to-understand manner.

    Please provide the explanation in the following structured format:

    1.  **Overall Summary:** A brief, one-sentence summary of what the code does.
    2.  **Line-by-Line Explanation:** Explain the key lines or blocks of the code. Be concise.
    3.  **Predicted Output:** If the code were to be executed, what would be its final output? If there is no output, please state "No output".

    ---

    Here is the code you need to explain:
    ```{code_snippet}```
    """
)

chain=LLMChain(llm=llm, prompt=prompt)

@app.route("/",methods=["GET","POST"])
def home():
  if request.method=="POST":
    language=request.form.get("language")
    code_snippet=request.form.get("code_snippet")

    if code_snippet:
      result=chain.invoke({language: language, "code_snippet": code_snippet})
      explanation=result['text']


  return render_template("index.html",explanation=explanation)


if __name__=="__main__":
  app.run(debug=True)