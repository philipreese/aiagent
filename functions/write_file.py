import os
from google.genai import types


def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory_abs, file_path))

    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path):
        try:
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        except Exception as e:
            return f"Error creating directory: {e}"

    if os.path.exists(abs_path) and os.path.isdir(abs_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory, not a file'

    try:
        with open(abs_path, "w", encoding="utf-8") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error writing to file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
