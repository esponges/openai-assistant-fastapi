from fastapi import APIRouter
import os
import openai
import time

item_router = APIRouter()

# declare get_prediction function that takes a query parameter as input
@item_router.get("/get_prediction")
def get_prediction(query: str):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        assistant_id = os.getenv("OPENAI_ASSISTANT_ID")

        assistant = openai.beta.assistants.retrieve(assistant_id)
        
        print(assistant)

        thread = openai.beta.threads.create()
        
        openai.beta.threads.messages.create(thread.id, text=query)

        run = openai.beta.threads.runs.create(thread.id, assistant_id=assistant.id)
        actual_run = openai.beta.threads.runs.retrieve(run.id, thread_id=thread.id)

        # polling mechanism to wait for the run to complete
        while actual_run.status == "queued" or actual_run.status == "in_progress":
            # add a 1 second delay
            time.sleep(1)

            # retreive again the updated run status
            actual_run = openai.beta.threads.runs.retrieve(run.id, thread_id=thread.id)
        
        # now that the run is completed, return the output
        assistant_messages = openai.beta.threads.messages.list(thread.id)
        
        # return the last message filtered by the run id
        last_message_from_run = assistant_messages.data[-1]

        return last_message_from_run
    except Exception as e:
        print(e)
        return "Error"
    
    