import os
import streamlit as st
from dotenv import load_dotenv
# from langchain_community.llms import 
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant, please respond to the question asked"),
        ("user","Question:{question}")
    ]
)
st.title("langchain demo with ollama")
input_text=st.text_input("what is your question?")

llm=OllamaLLM(model="qwen2.5:0.5b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    