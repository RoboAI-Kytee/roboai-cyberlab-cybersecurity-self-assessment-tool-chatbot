from openai import OpenAI
import os
from list_all_documents import list_pdfs_in_folder
from event_handler import EventHandler
from sys_prompt_handler import get_sys_prompt
import yaml
import os
# Load the YAML configuration file
config = yaml.safe_load(open("config.yml"))

client = OpenAI()

def openai_4o_query_rag(query):
    print(f"Query: {query}")

    try:
        vector_store_id = config['openAIAssistant']['vector_store_id']
        assistant_id = config['openAIAssistant']['assistant_id_4o']
        thread = client.beta.threads.create(
            messages=[
                {"role": "user", "content": query}
            ],
            tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
        )
        final_message_content = None
        event_handler = EventHandler()
        with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant_id,
            instructions="",
            event_handler=event_handler,
        ) as stream:
            stream.until_done()
        return  event_handler.final_message_content  

    except Exception as e:
        print(f"Error in openai_4o_query_rag: {e}")
        return f"Error in openai_4o_query_rag: {e}"  

# test
if __name__ == "__main__":
    openai_4o_query_rag("how are youuuuu???")