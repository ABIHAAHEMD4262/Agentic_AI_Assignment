from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled,RunConfig
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv(override=True)
set_tracing_disabled(True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model=gemini_model_name
)
#AGENT LEVEL CONFIGURATION
math_agent:Agent  = Agent(
    name="Math Agent",
    instructions="""
   -You are a helpful math agent
   - you can solve complex math question and expression.
   -DO NOT answer if request is not about math question.
   -DO NOT generate answer on yourself if question are not about MATH
   -You can simply refuse the answer if you don't know
    """,
    model=model

)

physics_agent:Agent  = Agent(
    name="Physics Agent",
    instructions="""
   -You are a helpful Physics agent
   - you can solve complex Physics numerical,eqautions and derivation.
   -DO NOT answer if request is not about Physics question.
   -DO NOT generate answer on yourself if question are not about Physics
   -You can simply refuse the answer in a polite way if you don't know
    """,
    # model=model

)
config = RunConfig(model=gemini_model_name)

