from pathlib import Path

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from utils.path_manager import PathManager


class FileWriterInput(BaseModel):
    file_name: str = Field(..., description="Name of the file")
    content: str = Field(..., description="Content to write into the file")


class FileWriterTool(BaseTool):
    name: str = "file_writer_tool"
    description: str = "Write content into a file in the output directory."

    args_schema: type[BaseModel] = FileWriterInput

    def _run(self, file_name: str, content: str) -> str:
        output_dir = PathManager.output_dir()

        file_path = output_dir / file_name

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully wrote file: {file_path}"