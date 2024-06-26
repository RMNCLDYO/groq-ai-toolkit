from client import Client

class Chat:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, stream=None, json=None, temperature=None, max_tokens=None, top_p=None, seed=None, stop=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')

        conversation_history = []

        if system_prompt:
            conversation_history.append({"role": "system", "content": system_prompt})

        print("Type 'exit' or 'quit' at any time to end the conversation.\n")
        
        print("Assistant: Hello! How can I assist you today?")
        while True:
            if prompt:
                user_input = prompt.strip()
                print(f"User: {user_input}")
                prompt = None
            else:
                user_input = input("User: ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("\nThank you for using the Groq AI toolkit. Have a great day!")
                    break

                if not user_input:
                    print("Invalid input detected. Please enter a valid message.")
                    continue
            
            if json:
                if stream:
                    print("Error: JSON mode does not support streaming.")
                    exit(1)
                if stop:
                    print("Error: JSON mode does not support stop sequences.")
                    exit(1)
                if "json" not in user_input:
                    user_input = user_input + " | Respond in JSON. The JSON schema should include at minimum: {'response': 'string', 'status': 'string'}"
                response_format = {"type": "json_object"}
            else:
                response_format = None
            
            conversation_history.append({"role": "user", "content": user_input})
            
            data = {
                "messages": conversation_history,
                "response_format": response_format,
                "model": self.model,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "top_p": top_p,
                "stream": stream,
                "seed": seed,
                "stop": stop
            }
            data = {k: v for k, v in data.items() if v is not None}
            
            endpoint = self.client.config.get('completions_endpoint')

            if stream:
                response = self.client.stream_post(endpoint, data)
                assistant_response = response
            else:
                response = self.client.post(endpoint, data)
                assistant_response = response
                print(f"Assistant: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})

class Text:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, stream=None, json=None, temperature=None, max_tokens=None, top_p=None, seed=None, stop=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        if not prompt:
            print("Error: { Invalid input detected }. Please enter a valid message.")
            exit(1)

        if json:
            if stream:
                print("Error: JSON mode does not support streaming.")
                exit(1)
            if stop:
                print("Error: JSON mode does not support stop sequences.")
                exit(1)
            if "json" not in prompt:
                prompt = prompt + " | Respond in JSON. The JSON schema should include at minimum: {'response': 'string', 'status': 'string'}"
            response_format = {"type": "json_object"}
        else:
            response_format = None

        if system_prompt:
            message = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        else:
            message = [{"role": "user", "content": prompt}]
    
        data = {
            "messages": message,
            "response_format": response_format,
            "model": self.model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "stream": stream,
            "seed": seed,
            "stop": stop
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        endpoint = self.client.config.get('completions_endpoint')

        if stream:
            response = self.client.stream_post(endpoint, data)
            assistant_response = response
        else:
            response = self.client.post(endpoint, data)
            assistant_response = response
            print(f"Assistant: {assistant_response}")
        
        print("\nThank you for using the Groq AI toolkit. Have a great day!")