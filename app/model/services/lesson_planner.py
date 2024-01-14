import os
import openai
import time


class LessonPlannerService:
    "Lesson Planner Service"
    def __init__(self):
        self.client = openai.api_key = os.getenv("OPENAI_API_KEY")
        self.assistant_id = os.getenv("OPENAI_LESSON_PLANNER_ID")

    def get_prediction(self, q: str):
        "Get prediction from the OpenAI API"
        try:
            assistant = openai.beta.assistants.retrieve(self.assistant_id)

            thread = openai.beta.threads.create()

            openai.beta.threads.messages.create(thread.id, content=q, role="user")

            run = openai.beta.threads.runs.create(thread.id, assistant_id=assistant.id)
            actual_run = openai.beta.threads.runs.retrieve(run.id, thread_id=thread.id)

            # polling mechanism to wait for the run to complete
            while actual_run.status == "queued" or actual_run.status == "in_progress":
                # add a 1 second delay
                time.sleep(1)

                # retreive again the updated run status
                actual_run = openai.beta.threads.runs.retrieve(
                    run.id, thread_id=thread.id
                )

            # now that the run is completed, return the output
            assistant_messages = openai.beta.threads.messages.list(thread.id).data

            # return the last message filtered by the run id
            last_message_from_run = filter(
                lambda message: message.run_id == run.id
                and message.role == "assistant",
                assistant_messages,
            )

            # if found return content, otherwise return empty string
            if last_message_from_run:
                return list(last_message_from_run)

            return "El asistente se encuentra ocupado, por favor intente más tarde"
        except IOError as e:
            print(e)
            return "Error"
