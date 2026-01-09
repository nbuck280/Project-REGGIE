from core.router import route
from skills import conversation,system

def think(user_input: str) -> str:
    """
    Central decision-making function for R.E.G.G.I.E.
    It takes what the router returns and decides which skill to invoke based on the user's input.
    """

    decision = route(user_input)

    if decision == 'conversation':
        return conversation.handle(user_input)
    
    if decision == 'system':
        return system.handle(user_input)
    
    return "I'm not sure how to help with that just yet."