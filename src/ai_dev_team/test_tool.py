from tools.file_writer_tool import FileWriterTool

tool = FileWriterTool()

result = tool._run(
    file_name="test.txt",
    content="Hello AI Team"
)

print(result)