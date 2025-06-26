import os
import subprocess


def run_python_file(working_directory: str, file_path: str) -> str:
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory_abs, file_path))

    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python", abs_path],
            cwd=working_directory_abs,
            timeout=30,
            capture_output=True,
            encoding="utf-8",
        )

        output: list[str] = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            output.append("No output produced.")

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
