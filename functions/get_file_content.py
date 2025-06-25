import os
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
