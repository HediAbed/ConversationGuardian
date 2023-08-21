
import openai
import configparser

def load_file(filename):
    """Load content from a given filename."""
    with open(filename, 'r') as file:
        return file.read()

def replace_symbols(text, chat):
    """Replace placeholder symbols in the text with actual chat content."""
    return text.replace("%%", chat)

def configure_openai(api_key):
    """Configure OpenAI with the given API key."""
    openai.api_key = api_key

def analyze_conversation(prompt, conversation_text):
    """Analyze the conversation using the OpenAI API."""
    # Replace symbols in the prompt
    output_text = replace_symbols(prompt, conversation_text)
    conversation = [
        {"role": "user", "content": output_text}
    ]
    # Send the conversation to the ChatGPT API
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=conversation
    )
    return response.choices[-1].message.content

def main():
    # Load necessary content from files
    conversation_text = load_file('sample_conversation.txt')
    chatgpt_prompt = load_file('analysis_prompt.txt')
    
    # Load and set up OpenAI API configuration
    config = configparser.ConfigParser()
    config.read('api_config.txt')
    api_key = config.get('API', 'api_key')
    configure_openai(api_key)
    
    # Analyze the conversation and print the result
    result = analyze_conversation(chatgpt_prompt, conversation_text)
    print(result)

if __name__ == "__main__":
    main()
