from utils.path_manager import PathManager

print("BASE:", PathManager.BASE_DIR)
print("Knowledge:", PathManager.knowledge_dir())
print("Output:", PathManager.output_dir())
print("Generated:", PathManager.generated_projects_dir())
print("Memory:", PathManager.memory_dir())