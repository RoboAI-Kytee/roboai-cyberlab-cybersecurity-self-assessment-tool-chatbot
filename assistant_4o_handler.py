from openai import OpenAI
from list_all_documents import list_pdfs_in_folder
from sys_prompt_handler import get_sys_prompt
import yaml
# if dont have vector store, generation and save id in yml file.
def initialize_openai_assistant():
    config_file = "config.yml"
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    client = OpenAI()
    assistant = client.beta.assistants.create(
            name="NIS2 Assistant 4o",
            instructions=get_sys_prompt(),
            model="gpt-4o",
            tools=[{"type": "file_search"}],
        )
    assistant_id = assistant.id
    
    config['openAIAssistant']['assistant_id_4o'] = assistant_id  
    with open(config_file, "w") as file:
        yaml.dump(config, file, default_flow_style=False)
    return assistant_id

if __name__ == "__main__":
    initialize_openai_assistant()
