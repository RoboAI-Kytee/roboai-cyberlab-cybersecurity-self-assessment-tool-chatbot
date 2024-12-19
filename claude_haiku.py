import yaml
from create_rag_chain import create_rag_chain
# Load the YAML configuration file
config = yaml.safe_load(open("config.yml"))

def haiku_query_rag(query):
    """
    Query the pre-configured RAG chain
    
    Args:
        query (str): Question to be asked
    
    Returns:
        str: Response from the RAG system
    """
    chain = create_rag_chain(config["claude_haiku_model"])
    response = chain.invoke(query)

    return response
if __name__ == "__main__":
    print(haiku_query_rag("how are you ...."))