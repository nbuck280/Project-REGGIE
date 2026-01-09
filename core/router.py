def route(user_input: str) -> str:
    """
    Decides what kind of request made by the user and routes it to the appropriate handler or skill
    it should use.
    """
    # Example routing logic (to be replaced with actual implementation)
    if any(word in user_input for word in ["open", "launch", "run"]):
        return "system"
    elif any(word in user_input for word in ["remember", "save", "note"]):
        return "memory"
    else:
        return "conversation"