import argparse
from groq import Chat, Text

def main():
    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
        pass
    parser = argparse.ArgumentParser(
        description="""
    ------------------------------------------------------------------
                             Groq AI Toolkit                           
                   API Wrapper & Command-line Interface               
                          [v1.0.1] by @rmncldyo                      
    ------------------------------------------------------------------

    An API wrapper & CLI for Groq AI's breakthrough LPU Inference Engine, allowing seamless interactions with the latest LLMs.

    | Option(s)              | Description                          | Example Usage                                          |
    |------------------------|--------------------------------------|--------------------------------------------------------|
    | -c,  --chat            | Enable chat mode                     | --chat                                                 |
    | -t,  --text            | Enable text mode                     | --text                                                 |
    | -p,  --prompt          | User prompt                          | --prompt "Explain the importance of low latency LLMs." |
    | -a,  --api_key         | API key for authentication           | --api_key "api_key_goes_here"                          |
    | -m,  --model           | The model you would like to use      | --model "llama3-8b-8192"                               |
    | -sp, --system_prompt   | System prompt (instructions)         | --system_prompt "You are a helpful assistant."         |
    | -st, --stream          | Enable streaming mode for responses  | --stream                                               |
    | -js, --json            | Output response in JSON format       | --json                                                 |
    | -tm, --temperature     | Sampling temperature                 | --temperature 0.7                                      |
    | -mt, --max_tokens      | Maximum number of tokens to generate | --max_tokens 1024                                      |
    | -tp, --top_p           | Nucleus sampling threshold           | --top_p 0.9                                            |
    | -sd, --seed            | Seed for sampling                    | --seed 123456789                                       |
    | -ss, --stop            | Stop sequences for completion        | --stop ", 6"                                           |
    """,
        formatter_class=CustomFormatter,
        epilog="For detailed usage information, visit our ReadMe here: github.com/RMNCLDYO/groq-ai-toolkit"
    )
    parser.add_argument('-c', '--chat', action='store_true', help='Enable chat mode')
    parser.add_argument('-t', '--text', action='store_true', help='Enable text mode')
    parser.add_argument('-p', '--prompt', type=str, help='User prompt', metavar='')
    parser.add_argument('-a', '--api_key', type=str, help='API key for authentication', metavar='')
    parser.add_argument('-m', '--model', type=str, default='llama3-8b-8192', help='The model you would like to use', metavar='')
    parser.add_argument('-sp', '--system_prompt', type=str, help='System prompt (instructions)', metavar='')
    parser.add_argument('-st', '--stream', action='store_true', help='Enable streaming mode for responses')
    parser.add_argument('-js', '--json', action='store_true', help='Output response in JSON format')
    parser.add_argument('-tm', '--temperature', type=float, help='Sampling temperature', metavar='')
    parser.add_argument('-mt', '--max_tokens', type=int, help='Maximum number of tokens to generate', metavar='')
    parser.add_argument('-tp', '--top_p', type=float, help='Nucleus sampling threshold', metavar='')
    parser.add_argument('-sd', '--seed', type=int, help='Seed for sampling', metavar='')
    parser.add_argument('-ss', '--stop', type=str, nargs='+', help='Stop sequences for completion', metavar='')

    args = parser.parse_args()
    
    if args.chat:
        Chat().run(args.api_key, args.model,  args.prompt, args.system_prompt, args.stream, args.json, args.temperature, args.max_tokens, args.top_p, args.seed, args.stop)
    elif args.text:
        Text().run(args.api_key, args.model,  args.prompt, args.system_prompt, args.stream, args.json, args.temperature, args.max_tokens, args.top_p, args.seed, args.stop)
    else:
        print("Error: Please specify a mode to use. Use --help for more information.")
        exit()

if __name__ == "__main__":
    main()
