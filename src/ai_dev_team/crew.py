from crewai import Agent, Crew, Knowledge, Process, Task
from crewai.project import CrewBase, agent, crew, task

from tools.knowledge_reader_tool import KnowledgeReaderInput, KnowledgeReaderTool

@CrewBase
class AIDevTeam:
    """AI Software Development Team"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ---------------- AGENTS ---------------- #

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["product_manager"],
            verbose=True
        )

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config["software_architect"],
            verbose=True
        )

    @agent
    def backend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["backend_developer"],
            verbose=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["qa_engineer"],
            verbose=True
        )

    @agent 
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_reviewer"],
            tools=[KnowledgeReaderTool()],
            verbose=True
        )

    # ---------------- TASKS ---------------- #

    @task
    def gather_requirements(self):
        return Task(
            config=self.tasks_config["gather_requirements"],
            agent=self.product_manager(),
        )

    @task
    def design_architecture(self) -> Task:
        return Task(
            config=self.tasks_config["design_architecture"],
            agent=self.software_architect(),
            context=[self.gather_requirements()]
        )

    @task
    def develop_backend(self) -> Task:
        return Task(
            config=self.tasks_config["develop_backend"],
            agent=self.backend_developer(),
            context=[self.design_architecture()],
        )

    @task
    def review_backend_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_backend_code"],
            agent=self.code_reviewer(),
            context=[self.develop_backend()]
        )
    
    @task
    def create_test_cases(self) -> Task:
        return Task(
            config=self.tasks_config["create_test_cases"],
            agent=self.qa_engineer(),
            context=[
                self.develop_backend(),
                self.review_backend_code()
                ]
        )

    # ---------------- CREW ---------------- #

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True
        )
