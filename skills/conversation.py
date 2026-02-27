from core.brain import Brain

brain = Brain()
def handle(user_input: str) -> str:
    return brain.generate(user_input)