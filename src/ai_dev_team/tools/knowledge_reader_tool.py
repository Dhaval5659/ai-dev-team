from pathlib import Path

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class KnowledgeReaderInput(BaseModel):
    file_name: str = Field(
        ...,
        description="Knowledge file name to read"
    )


class KnowledgeReaderTool(BaseTool):
    name: str = "knowledge_reader_tool"
    description: str = (
        "Read knowledge files from the knowledge directory."
    )

    args_schema: type[BaseModel] = KnowledgeReaderInput

    def _run(self, file_name: str) -> str:
        BASE_DIR = Path(__file__).resolve().parents[3]
        knowledge_path = BASE_DIR / "knowledge" / file_name
        if not knowledge_path.exists():
         return f"Knowledge file not found: {knowledge_path}"
        return knowledge_path.read_text(encoding="utf-8")