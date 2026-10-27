import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from prompts import interview_prompt, feedback_prompt
from langchain_core.output_parsers import StrOutputParser

#groq
groq_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.4,
    api_key=os.environ["GROQ_API_KEY"],
)

#openai
openai_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.environ["OPENAI_API_KEY"],
)

# LangChain's Chaining (LCEL): Prompt -> Output -> Parser
# Extract plain text from AIMessage 
interview_chain = interview_prompt | groq_llm | StrOutputParser()
feedback_chain = feedback_prompt | openai_llm | StrOutputParser()

