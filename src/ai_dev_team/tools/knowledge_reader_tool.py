from pathlib import Path

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from utils.path_manager import PathManager

# Input 
class KnowledgeReaderInput(BaseModel):
    file_name: str = Field(
        ...,
        description="Knowledge file name to read"
    )

# Tool
class KnowledgeReaderTool(BaseTool):
    name: str = "knowledge_reader_tool"
    description: str = (
        "Read knowledge files from the knowledge directory."
    )

    args_schema: type[BaseModel] = KnowledgeReaderInput

    def _run(self, file_name: str) -> str:
        knowledge_path = PathManager.knowledge_dir()/file_name
        if not knowledge_path.exists():
         return f"Knowledge file not found: {knowledge_path}"
         
        return knowledge_path.read_text(encoding="utf-8")