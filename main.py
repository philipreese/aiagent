import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) == 1:
        print('Usage: python main.py "<prompt>"')
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    prompt = " ".join(sys.argv[1:])

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    generate_content(client, messages)


def generate_content(client: genai.Client, messages: list[types.Content]) -> None:
    response = client.models.generate_content(  # type: ignore
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if not response.usage_metadata:
        print("No response received.")
        return

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
