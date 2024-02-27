from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_task(self, agent):
        return Task(
            description=f'Load and process the content of BABOK_Guide_v3_Member_2015.pdf, filtered by the search phrase if specified.',
            agent=agent,
            async_execution=True,
            expected_output="""A comprehensive analysis incorporating insights from multiple frameworks.
                
            """
        )

    def analyze_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""Conduct a comprehensive analysis by first developing the product strategy and vision,
        and then analyzing user needs and market situation to prioritize strategic actions.
        This method chains productStrategyAndVision and userNeedsAndPrioritization together.
        Input: Comprehensive context including expert opinions, project changes, market data, and user feedback.
        Output: A comprehensive analysis that includes both strategy and user needs prioritization..\n\n'
            """
        )

    def compile_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""Engage in unfiltered ideation to define challenges and evolve ideas.
        This might involve using a virtual whiteboard tool for collaboration.
        Output: Expanded and evolved ideas.
            """,
            callback=callback_function
        )
