import requests
class Brain:
    
    def __init__(self, model="llama3"):
        self.model = model
        self.url = 'http://localhost:11434/api/generate'
    
    # Simple method to send a prompt to the language model and get a response
    def generate(self, prompt: str) -> str:
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        return result["response"]