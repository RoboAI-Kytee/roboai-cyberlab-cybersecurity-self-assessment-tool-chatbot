from fastapi import FastAPI,Form
from models.claude_haiku import haiku_query_rag
from models.claude_sonnet import sonnet_query_rag
from models.openAIAssistant_4o import openai_4o_query_rag
from models.openAIAssistant_4omini import openai_4o_mini_query_rag
# from update_assistant4omini_instructions import update_assistant_instructions
# from update_assistant4o_instructions import update_assistant_4oinstructions

app = FastAPI()
@app.get("/")
async def root():
    return {"msg":"Hello, It is an API for NIS2"}

@app.get("/test")
async def test():
    return {"msg":"Test, It is an API for NIS2"}


@app.get("/getAnswerFromClaudeHaiku")
async def getAnswerFromClaudeHaiku(query):
    response = haiku_query_rag(query)
    print(response)
    return {
        "msg":f"/getAnswer: question is {query}"
        ,"answer": response
        }


@app.get("/getAnswerFromClaudeSonnet")
async def getAnswerFromClaudeSonnet(query):
    response = sonnet_query_rag(query)
    print(response)
    return {
        "msg":f"/getAnswer: question is {query}"
        ,"answer": response
        }

@app.get("/getAnswerFromOpenaiAssistant4o")
async def getAnswerFromOpenaiAssistant4o(query):
    response = openai_4o_query_rag(query)
    print(response)
    return {
        "msg":f"/getAnswer: question is {query}"
        ,"answer": response
        }

@app.get("/getAnswerFromOpenaiAssistant4omini")
async def getAnswerFromOpenaiAssistant4omini(query):
    response = openai_4o_mini_query_rag(query)
    print(response)
    return {
        "msg":f"/getAnswer: question is {query}"
        ,"answer": response
        }


# @app.get("/api_update_assistant4omini_instructions")
# async def api_update_assistant4omini_instructions(new_instructions):
#     response = update_assistant_instructions(new_instructions)
#     print(response)
#     return {
#         "msg":f"/new_instructions {new_instructions}"
#         ,"answer": response
#         }

# @app.get("/api_update_assistant4o_instructions")
# async def api_update_assistant4o_instructions(new_instructions):
#     response = update_assistant_4oinstructions(new_instructions)
#     print(response)
#     return {
#         "msg":f"/new_instructions {new_instructions}"
#         ,"answer": response
#         }