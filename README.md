<p align="center">
    <a href=".github/version.json" title="Go to changelog" target="_blank">
        <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=Groq+AI+Toolkit&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2Fgroq-ai-toolkit%2Fmain%2F.github%2Fversion.json" alt="Version">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to changelog" target="_blank"><img src="https://img.shields.io/badge/maintained-yes-2ea44f?style=for-the-badge" alt="maintained - yes"></a>
    <a href=".github/CONTRIBUTING.md" title="Go to contributions doc" target="_blank"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f?style=for-the-badge" alt="contributions - welcome"></a>
</p>

## Overview

The Groq AI Toolkit is a comprehensive API wrapper and command-line interface designed for Groq's breakthrough Language Processing Unit (LPU) Inference Engine. This toolkit facilitates near-real-time responses (300 tokens/sec), leveraging the power of GroqCloud's advanced offering of open-source AI models.

## Features

- **Chat Mode**: Engage in interactive conversations with the model of your choice using Groq's superfast LPU engine.
- **Text Mode**: Submit text prompts and receive responses, ideal for scripting and automation.
- **Streaming Support**: Utilize streaming responses for real-time interaction with models.
- **Flexible Configuration**: Customize model parameters, including API keys, model selection, token limits, and more.

## Prerequisites

- Python 3.6+

## Dependencies
The following Python packages are required:
- `requests`: For making HTTP requests to the Groq API.

The following Python packages are optional:
- `python-dotenv`: For managing API keys and other environment variables.

## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/RMNCLDYO/groq-ai-toolkit.git
    ```

2. Navigate to the folder
    ```shell
    cd groq-ai-toolkit
    ```

3. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Getting Started

#### Obtaining an API Key

1. Sign up and verify your account at [Groq AI](https://console.groq.com/).
2. Navigate to API Keys in your account settings.
3. Click Create API Key, name it, and save it securely.

### Configuration (*Optional*)

Create a .env file in the root directory and add your API key:
```shell
GROQ_API_KEY=your_api_key_here
```

## Usage

### CLI

*Chat with Groq*:
```shell
python cli.py --chat
```

*Ask a question*:
```shell
python cli.py --text --prompt "What is the meaning of life?"
```

*Get usage details and options*:
```shell
python cli.py --help
```

### Wrapper

*Chat with Groq*:
```python
from groq import Chat

Chat().run()
```

> An executable version of this example can be found [here](./examples/example_chat.py). (*You must move this file to the root folder before running the program.*)

*Ask a question*:
```python
from groq import Text

Text().run(prompt="What is the meaning of life?")
```

> An executable version of this example can be found [here](./examples/example_text.py). (*You must move this file to the root folder before running the program.*)

## Advanced Configuration

### Wrapper Options
| Option(s)        | Description                          | Example Usage                                    |
|------------------|--------------------------------------|--------------------------------------------------|
| `prompt`         | User prompt                          | prompt="Hello, how can I assist you today?"      |
| `image`          | Image file path or url               | image="path_or_url_goes_here"                    |
| `api_key`        | Groq API key for authentication      | api_key="api_key_goes_here"                      |
| `model`          | The model you would like to use      | model="model_name_goes_here"                     |
| `system_prompt`  | System prompt (instructions)         | system_prompt="You are an advanced AI assistant" |
| `temperature`    | Sampling temperature                 | temperature=0.7                                  |
| `max_tokens`     | Maximum number of tokens to generate | max_tokens=1024                                  |
| `-top_p`         | Nucleus sampling threshold           | top_p=0.9                                        |
| `stream`         | Enable streaming mode for responses  | stream=True                                      |
| `stop`           | Stop sequences for completion        | stop=", 6"                                       |

### CLI Options
| Option(s)                  | Description                          | Example Usage                                      |
|----------------------------|--------------------------------------|----------------------------------------------------|
| `-c`,  `--chat`            | Enable chat mode                     | --chat                                             |
| `-t`,  `--text`            | Enable text mode                     | --text                                             |
| `-p`,  `--prompt`          | User prompt                          | --prompt "Hello, how can I assist you today?"      |
| `-a`,  `--api_key`         | Groq API key for authentication      | --api_key "api_key_goes_here"                      |
| `-m`,  `--model`           | The model you would like to use      | --model "model_name_goes_here"                     |
| `-sp`, `--system_prompt`   | System prompt (instructions)         | --system_prompt "You are an advanced AI assistant" |
| `-tm`, `--temperature`     | Sampling temperature                 | --temperature 0.7                                  |
| `-mt`, `--max_tokens`      | Maximum number of tokens to generate | --max_tokens 1024                                  |
| `-tp`, `--top_p`           | Nucleus sampling threshold           | --top_p 0.9                                        |
| `-st`, `--stream`          | Enable streaming mode for responses  | --stream                                           |
| `-ss`, `--stop`            | Stop sequences for completion        | --stop ", 6"                                       |

## Advanced Usage

### CLI

*Initiate a chat session passing your API key, with streaming mode set, and a custom system prompt*:
```shell
python cli.py --chat --api_key "your_api_key" --stream --system_prompt "You are a comedian, you respond to all questions as if they are a funny joke."
```

### Wrapper

*Initiate a chat session using the Mixtral 8x7b model, with top_p and max_tokens set to 100*:
```python
from groq import Chat

Chat().run(model="mixtral-8x7b-32768", max_tokens=100, top_p=0.9)
```

## Available Models

| **Model**       	          | **Latest API model name**  	| **Max Tokens** 	|
|----------------------------	|----------------------------	|----------------	|
| LLaMA2-70b-chat             | `llama2-70b-4096`   	      | 4096 tokens    	|
| Mixtral-8x7b-Instruct-v0.1 	| `mixtral-8x7b-32768` 	      | 32768 tokens    |

## Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## Reporting Issues
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/groq-ai-toolkit/issues).

Your report will help us make the project better for everyone.

## Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/groq-ai-toolkit/issues).

Your suggestions for improvements are always welcome.

## Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
