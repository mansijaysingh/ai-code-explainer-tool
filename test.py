import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

print("--- Starting Test Script ---")

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    print("ERROR: OPENAI_API_KEY not found in .env file.")
else:
    print("API Key loaded successfully.")

try:
    # Initialize the LLM
    print("Initializing ChatOpenAI...")
    llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")
    print("ChatOpenAI initialized successfully.")

    # Create the chain
    prompt = ChatPromptTemplate.from_template("Explain this Python code: ```{code}```")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # Invoke the chain with a simple example
    print("Invoking chain...")
    code_to_explain = "def hello():\n    print('Hello, World!')"
    explanation = chain.invoke({"code": code_to_explain})

    # Print the result
    print("\n--- SUCCESS! ---")
    print("Explanation Received:")
    print(explanation)

except Exception as e:
    # Print any error that occurs
    print("\n--- AN ERROR OCCURRED ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Details: {e}")