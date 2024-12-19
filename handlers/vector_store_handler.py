from openai import OpenAI
from handlers.list_all_documents import list_pdfs_in_folder
import yaml
# if dont have vector store, generation and save id in yml file.
def initialize_vector_store():
    config_file = "config/config.yml"
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    client = OpenAI()
    vector_store = client.beta.vector_stores.create(name="NIS2")
    vector_store_id = vector_store.id

    config['openAIAssistant']['vector_store_id'] = vector_store_id  
    with open(config_file, "w") as file:
        yaml.dump(config, file, default_flow_style=False)

    file_streams =file_streams = [open(path, "rb") for path in list_pdfs_in_folder()]  
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id, files=file_streams
    )
        
    print(file_batch.status)
    print(file_batch.file_counts)
    
    return vector_store_id

    
if __name__ == "__main__":
    initialize_vector_store()