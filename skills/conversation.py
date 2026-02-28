from core.brain import Brain

# Initialize a single instance of Brain for conversation handling
brain = Brain()
# Handle conversation tasks by generating a response using the Brain
def handle(user_input: str) -> str:
    return brain.generate(user_input)