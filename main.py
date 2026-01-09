from core.brain import think

def main():
    print("Welcome to R.E.G.G.I.E. (Reliable Engine for Guidance, Goofiness, and Intelligent Execution)!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("> ")
        if user_input.lower() in {'exit', 'quit'}:
            print("Goodbye!")
            break

        response = think(user_input)
        print(response)