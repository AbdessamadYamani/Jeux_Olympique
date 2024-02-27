from crewai.agent import Agent
from fitz import fitz
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from BusinessAnalystTool import BusinessAnalysisToolsClass
from News_AnalyzerTool import  News_AnalyzerTool

class AINewsLetterAgents():
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
    
    def extract_text_from_pdf(pdf_file_path):
        text = ""
        with fitz.open(pdf_file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    def editor_agent(self):
        return Agent(
            role='Project Manager',
            goal="""Orchestrate interactions between agents to stimulate debates among team members sending initial_ideas from  Olympics Content Loader tool to Project Manager Analysis Tool. Identifying key discussion points: Analyze the topic at hand and pinpoint crucial aspects that would benefit from diverse perspectives.
        Matching viewpoints: Strategically distribute discussion topics among agents with complementary strengths and contrasting approaches.
        Prompting meaningful engagement: Craft questions and prompts that stimulate debate, encourage critical thinking, and draw out diverse arguments.
        Facilitating exchange and response: Manage the flow of conversation, ensuring each agent has the opportunity to present their views and respond to others.
        Highlighting key points and fostering consensus: Summarize key arguments, identify areas of agreement and disagreement, and guide the team towards constructive conclusions.""",
            backstory='A seasoned project manager experienced in guiding projects to align with industry best practices.',
            allow_delegation=True,
            verbose=True,
            max_iter=15,
            default_factory=lambda: ChatOpenAI(openai_api_key=self.openai_api_key),
        )

    def Buisness_Analyst(self):
        return Agent(
            role='Business Analyst',
            goal='Use tool Business Analyst Framework Tool to Analyze and define business requirements for the ticket reservation system. Use as source of informations tools Olympics Content Loader and Website Content Loader as source of informations. You must answer in French.',
            backstory='An analytical thinker skilled in distilling complex documentation into actionable insights.',
            tools=[BusinessAnalysisToolsClass().load_content],
            allow_delegation=True,
            verbose=False,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='Product Owner',
            goal='Analyze and define business requirements for the ticket reservation system, At the end of each answer, add a reference pointing to the source from which you got the information. You must answer in French.',
    backstory='An analytical thinker skilled in distilling complex documentation into actionable insights.',
           
            tools=[News_AnalyzerTool.extract_text_from_pdf],
            verbose=True,
            allow_delegation=True,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='Analyste Fonctionnel',
            goal="Traduire les besoins métiers en exigences fonctionnelles pour le système de réservation. At the end of each answer, add a reference pointing to the source from which you got the information.",
    backstory="Compétences en conception de solutions logicielles et en liaison entre le métier et le développement technique",
            verbose=True,
            allow_delegation=True,
        )