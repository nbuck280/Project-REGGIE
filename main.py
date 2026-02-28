from core.orchestrator import Orchestrator

def main():
    # Initialize the orchestrator
    orchestrator = Orchestrator()
    
    # Welcome message
    print("Welcome to R.E.G.G.I.E. (Reliable Engine for Guidance, Goofiness, and Intelligent Execution)!")
    print("Type 'exit' to quit.")
    
    # Main loop to handle user input
    while True:
        user_input = input("> ")
        # Check for exit commands
        if user_input.lower() in {'exit', 'quit', 'bye', 'goodbye', 'later'}:
            print("Goodbye!")
            break
        
        # Take user input and get a response from the orchestrator
        response = orchestrator.handle(user_input)
        print(response)

if __name__ == "__main__":
    main()
