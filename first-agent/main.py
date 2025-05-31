# def main():
#     print("Hello from first-agent!")


# if __name__ == "__main__":
#     main()
#  install dotenv use command uv add python-dotenv
from dotenv import load_dotenv
import os
from agents import Agent , AsyncOpenAI ,OpenAIChatCompletionsModel ,RunConfig ,Runner


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     
agent = Agent(
    name = "Translator",
    instructions = "You are a helpful translator always translate english sentence into urdu" 
)

#  runner function fro run agents

response = Runner.run_sync(
    agent,
    input = "My name is Rashida shaikh, I am Computer Engineer",
run_config = config

)

print(response)
 