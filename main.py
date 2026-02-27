from core.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()
    
    print("Welcome to R.E.G.G.I.E. (Reliable Engine for Guidance, Goofiness, and Intelligent Execution)!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("> ")
        if user_input.lower() in {'exit', 'quit', 'bye', 'goodbye', 'later'}:
            print("Goodbye!")
            break

        response = orchestrator.handle(user_input)
        print(response)

if __name__ == "__main__":
    main()
