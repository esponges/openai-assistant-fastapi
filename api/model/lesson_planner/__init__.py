from fastapi import APIRouter
import os
import openai
import time

lesson_planner_router = APIRouter()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# declare get_prediction function that takes a query parameter as input
@lesson_planner_router.get("/get_prediction")
def get_prediction(q: str):
    try:
        assistant_id = os.getenv("OPENAI_LESSON_PLANNER_ID")

        assistant = openai.beta.assistants.retrieve(assistant_id)

        thread = openai.beta.threads.create()
        
        openai.beta.threads.messages.create(thread.id, content=q, role="user")

        run = openai.beta.threads.runs.create(thread.id, assistant_id=assistant.id)
        actual_run = openai.beta.threads.runs.retrieve(run.id, thread_id=thread.id)

        # polling mechanism to wait for the run to complete
        while actual_run.status == "queued" or actual_run.status == "in_progress":
            # add a 1 second delay
            time.sleep(1)

            # retreive again the updated run status
            actual_run = openai.beta.threads.runs.retrieve(run.id, thread_id=thread.id)
        
        # now that the run is completed, return the output
        assistant_messages = openai.beta.threads.messages.list(thread.id).data
        
        # return the last message filtered by the run id
        last_message_from_run = filter(lambda message: message.run_id == run.id and message.role == "assistant", assistant_messages)

        # if found return content, otherwise return empty string
        if last_message_from_run:
            return list(last_message_from_run)
        else:
            return "El asistente se encuentra ocupado, por favor intente más tarde"
    except Exception as e:
        print(e)
        return "Error"
    
