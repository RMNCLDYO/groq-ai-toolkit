import json
import requests
from config import load_config
from loading import Loading

print("------------------------------------------------------------------\n")
print("                          Groq AI Toolkit                         \n")     
print("               API Wrapper & Command-line Interface               \n")   
print("                       [v1.0.1] by @rmncldyo                      \n")  
print("------------------------------------------------------------------\n")

class Client:
    def __init__(self, api_key=None):
        self.config = load_config(api_key=api_key)
        self.api_key = api_key if api_key else self.config.get('api_key')
        self.base_url = self.config.get('base_url')
        self.version = self.config.get('version')
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{self.version}/{endpoint}"
        try:
            loading.start()
            response = requests.post(url, headers=self.headers, json=data)
            response = response.json()
            try:
                response["error"]["message"]
                if "Failed to generate JSON" in response["error"]["message"]:
                    response = "Failed to generate JSON"
                    return response
                else:
                    response = response["error"]["message"]
                    return response
            except:
                pass
            try:
                response = response["choices"][0]["message"]["content"]
                return response
            except Exception as e:
                loading.stop()
                raise Exception(f"Error: {response}")
        except Exception as e:
            print(f"HTTP Error: {e}")
            raise
        finally:
            loading.stop()

    def stream_post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{self.version}/{endpoint}"
        full_response = []
        try:
            loading.start()
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            response.raise_for_status()
            loading.stop()
            response_content = ""
            print("Assistant: ", end="", flush=True)
            for chunk in response.iter_lines():
                if chunk:
                    json_data = chunk.decode('utf-8').split('data: ')[1]
                    try:
                        data_dict = json.loads(json_data)
                        if data_dict['choices'][0]['delta'] != {}:
                            print(data_dict['choices'][0]['delta']['content'], end="", flush=True)
                            response_content += data_dict['choices'][0]['delta']['content']
                        else:
                            if data_dict['choices'][0]['finish_reason'] == "stop":
                                break
                    except Exception as e:
                        if json_data == "[DONE]":
                            break
                        else:
                            print(f"An error occurred: {json_data}")
            full_response.append(response_content)
            print()
            return full_response[0]
        except Exception as e:
            print(f"Stream HTTP Error: {e}")
            raise
        finally:
            loading.stop()
