from tools.knowledge_reader_tool import KnowledgeReaderTool

tool = KnowledgeReaderTool()

result = tool._run(
    file_name="api_design_guidelines.md"
)

print(result)