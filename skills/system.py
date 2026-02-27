import os

def handle(user_input: str) -> str:
    os.system(user_input)
    return "Executed command: " + user_input