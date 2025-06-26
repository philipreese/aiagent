import os
from google.genai import types


def get_files_info(working_directory: str, directory: str | None = None) -> str:
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = (
        os.path.abspath(os.path.join(working_directory_abs, directory))
        if directory
        else working_directory_abs
    )

    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'

    try:
        files_info: list[str] = []
        for item in os.listdir(abs_path):
            item_path = os.path.join(abs_path, item)
            file_size = os.path.getsize(item_path)
            files_info.append(
                f"- {item} file_size={file_size} bytes, is_dir={os.path.isdir(item_path)}"
            )

        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
