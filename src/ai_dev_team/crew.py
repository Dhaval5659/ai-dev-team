from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.memory import ShortTermMemory
from crewai.memory.storage.rag_storage import RAGStorage


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

    # ---------------- TASKS ---------------- #

    @task
    def gather_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["gather_requirements"],
            agent=self.product_manager()
        )

    @task
    def design_architecture(self) -> Task:
        return Task(
            config=self.tasks_config["design_architecture"],
            agent=self.software_architect()
        )

    @task
    def develop_backend(self) -> Task:
        return Task(
            config=self.tasks_config["develop_backend"],
            agent=self.backend_developer()
        )

    @task
    def create_test_cases(self) -> Task:
        return Task(
            config=self.tasks_config["create_test_cases"],
            agent=self.qa_engineer()
        )

    # ---------------- CREW ---------------- #

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            short_term_memory=ShortTermMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "openai",
                        "config": {
                            "model": "text-embedding-3-small"
                        }
                    },
                    type="short_term",
                    path="./memory"
                )
            )
        )