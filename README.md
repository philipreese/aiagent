# aiagent

An AI agent that uses Google Gemini (via Google AI Studio) to help automate codebase tasks, answer questions, and perform code operations by calling functions in your workspace.

## Features
- Uses Gemini models to process user prompts and generate responses.
- Supports function-calling for:
  - Listing files and directories
  - Reading file contents
  - Executing Python files
  - Writing or overwriting files
- Iterative loop: the agent can plan and execute multiple steps to fulfill complex requests.

## Setup
1. **Clone the repository** and navigate to the `aiagent` directory.
2. **Setup and initialize virtual environment (Recommended)**
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your environment:**
   - Create a `.env` file with your Gemini API key:
     ```env
     GEMINI_API_KEY=your_google_gemini_api_key_here
     ```

## Usage
Run the agent with a prompt:
```bash
python main.py "<your prompt>" [--verbose]
```
- Example:
  ```bash
  python main.py "List all Python files in the project and show me the contents of config.py" --verbose
  ```

## How it works
- The agent receives your prompt and uses Gemini to generate a plan.
- It can call functions to interact with your codebase (list, read, write, execute files).
- The agent loops, making further function calls as needed, until it can answer your request.

## Configuration
- `MAX_ITERS` (in `config.py`): Maximum number of iterations per prompt.
- `WORKING_DIR` (in `config.py`): The root directory for file operations.

## Extending
- Add new function schemas and implementations in the `functions/` directory.
- Register new functions in `call_function.py`.

