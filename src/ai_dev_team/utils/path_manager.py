from pathlib import Path


class PathManager:
    """
    Centralized path manager for the AI Dev Team project.
    """

    # Project Root
    BASE_DIR = Path(__file__).resolve().parents[3]

    @classmethod
    def knowledge_dir(cls) -> Path:
        return cls.BASE_DIR / "knowledge"

    @classmethod
    def output_dir(cls) -> Path:
        path = cls.BASE_DIR / "output"
        path.mkdir(exist_ok=True)
        return path

    @classmethod
    def generated_projects_dir(cls) -> Path:
        path = cls.BASE_DIR / "generated_projects"
        path.mkdir(exist_ok=True)
        return path

    @classmethod
    def memory_dir(cls) -> Path:
        path = cls.BASE_DIR / "memory"
        path.mkdir(exist_ok=True)
        return path