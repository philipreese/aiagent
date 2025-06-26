import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory_abs, file_path))

    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_path, "r", encoding="utf-8") as file:
            content = file.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += (
                    f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return content
    except Exception as e:
        return f"Error reading file: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
    ),
)
