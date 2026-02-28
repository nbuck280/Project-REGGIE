import os
from core.brain import Brain

brain = Brain()
# This is a placeholder for system-level commands and operations.
def handle(user_input: str) -> str:
    app_list = [os.path.basename(x) for x in os.listdir("/Applications")]
    command = brain.generate(user_input + f" (This is a system command, not a conversation. Do not respond with a conversational answer. Only respond with the system command that should be run in the terminal of a Mac computer. If it is not a valid system command, respond with 'Invalid command.' If it is in this list, open the app: {app_list})")
    os.system(command)
    return "Executed: " + command