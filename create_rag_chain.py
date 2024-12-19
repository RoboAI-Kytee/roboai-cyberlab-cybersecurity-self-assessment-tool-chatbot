from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from sys_prompt_handler import get_sys_prompt
from init_chroma import init_local_vector_db

import yaml

config = yaml.safe_load(open("config.yml"))

def create_rag_chain(modelName):
    # Initialize or load the vector database
    vector_db = init_local_vector_db()
    # Adjust retrieval settings for faster queryte
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    # Define prompt template
    PROMPT = PromptTemplate(
        input_variables=["question"],
        template = get_sys_prompt() + "Alkuperäinen kysymys: {question} Vastauksesi tulee olla suomeksi."
    )

    # Initialize Claude model
    llm = ChatAnthropic(
        model= modelName, #    # Choose appropriate Claude model
        temperature=0
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | PROMPT
        | llm
        | StrOutputParser()
    )
    return chain