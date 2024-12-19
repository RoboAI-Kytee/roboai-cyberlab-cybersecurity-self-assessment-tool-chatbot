from openai import OpenAI
import yaml
from sys_prompt_handler import get_sys_prompt
import os
'''
How to use it:
Change sys_prompt.txt,run this code. 
'''
# Set up your OpenAI API key
client = OpenAI()

# Define the function to update assistant's instructions
def update_assistant_4o_instructions(new_instructions):
    try:
        config = yaml.safe_load(open("config.yml"))

        # Make the API call to update the assistant's instructions
        response = client.beta.assistants.update(
            assistant_id=config['openAIAssistant']['assistant_id_4o'],
            instructions=new_instructions
        )
        print("Assistant 4o instructions updated successfully!")
        # return response
        return "Assistant 4o instructions updated successfully!"
    except Exception as e:
        print(f"An error occurred: {e}")
        return None            

# Define the function to update assistant's instructions
def update_assistant_4omini_instructions(new_instructions):
    try:
        config = yaml.safe_load(open("config.yml"))

        # Make the API call to update the assistant's instructions
        response = client.beta.assistants.update(
            assistant_id=config['openAIAssistant']['assistant_id_4o_mini'],
            instructions=new_instructions
        )
        print("Assistant 4omini instructions updated successfully!")
        # return response
        return "Assistant 4omini instructions updated successfully!"
    except Exception as e:
        print(f"An error occurred: {e}")
        return None    

if __name__ == "__main__":
    update_assistant_4o_instructions(get_sys_prompt())
    update_assistant_4omini_instructions(get_sys_prompt())
