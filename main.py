
from datetime import datetime
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown

from dotenv import load_dotenv
load_dotenv()

# Your OpenAI API key
openai_api_key = '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'

# Initialize the agents and tasks
agents = AINewsLetterAgents(openai_api_key=openai_api_key)
tasks = AINewsLetterTasks()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model="gpt-4",
    openai_api_key=openai_api_key  # Pass the API key here as well
)

# Instantiate the agents
editor = agents.editor_agent()
analyzer = agents.Buisness_Analyst()
fetcher = agents.news_analyzer_agent()
compiler = agents.newsletter_compiler_agent()

# Instantiate the tasks
fetch_task = tasks.fetch_task(fetcher)
analyze_task = tasks.analyze_task(analyzer, [fetch_task])
compile_task = tasks.compile_task(
    compiler, [analyze_task], 
    lambda task_output: save_markdown(f"newsletter_{datetime.now().strftime('%Y%m%d%H%M%S')}", task_output.output)
)

# Form the crew
crew = Crew(
    agents=[editor, analyzer, fetcher, compiler],
    tasks=[fetch_task, analyze_task, compile_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4,
    verbose=2
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)