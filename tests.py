from functions.run_python_file import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for 'main.py' file:")
    print(result, "\n")

    result = run_python_file("calculator", "tests.py")
    print("Result for 'tests.py' file:")
    print(result, "\n")

    result = run_python_file("calculator", "../main.py")
    print("Result for '../main.py' file:")
    print(result, "\n")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for 'nonexistent.py' file:")
    print(result, "\n")


if __name__ == "__main__":
    test()
