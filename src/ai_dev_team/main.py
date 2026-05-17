from dotenv import load_dotenv
from crew import AIDevTeam

load_dotenv()

project_idea = input("Enter your software project idea: ")

inputs = {
    "project_idea": project_idea
}

result = AIDevTeam().crew().kickoff(inputs=inputs)

print("\n\nFINAL RESULT:\n")
print(result)
