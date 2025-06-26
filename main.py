import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    if len(sys.argv) == 1:
        print('Usage: python main.py "<prompt>" [--verbose]')
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    generate_content(client, messages, available_functions, verbose)


def generate_content(
    client: genai.Client,
    messages: list[types.Content],
    available_functions: types.Tool,
    verbose: bool = False,
) -> None:
    response = client.models.generate_content(  # type: ignore
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if not response.usage_metadata:
        print("No response received.")
        return

    if verbose:
        print("User prompt:", messages[0])
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print(response.text)
        return

    function_responses: list[types.Part] = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
            or not function_call_result.parts[0].function_response.response
        ):
            raise Exception(f"empty function call result for {function_call.name}")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")


if __name__ == "__main__":
    main()
