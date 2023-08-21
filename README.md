
# ConversationGuardian

**Safeguarding online platforms, one conversation at a time.**

## Introduction
ConversationGuardian is a ChatGpt AI-driven system designed to detect indications of NSFW or illegal content within user interactions. By leveraging state-of-the-art machine learning techniques, this system assists platform administrators and moderators in identifying potential risks and taking timely action.

## Features
- **Advanced Detection**: Utilizes sophisticated models to identify subtle hints or explicit mentions of prohibited content.
- **True/False Output**: Simple yet effective. A 'true' output indicates the presence of undesirable content, while 'false' denotes its absence.
- **Integration Ready**: Designed to be easily integrated into most online platforms, aiding in user management and content moderation.

## How it Works
1. **Input**: Provide the model with a conversation between two users.
2. **Analysis**: The AI model meticulously analyzes the conversation based on various factors.
3. **Output**: The system returns a binary result. "True" indicates the presence of NSFW or illegal content, and "false" indicates its absence.
4. **Action**: Based on the model's output, platform administrators can decide on appropriate actions, such as issuing warnings or blocking users.

## How to Run

1. **Setup**:
   - Ensure you have Python installed (Version 3.6 or higher recommended).
   - Install the required packages using pip:
     ```
     pip install openai configparser
     ```

2. **Configuration**:
   - Open the `api_config.txt` file and update the `api_key` field with your OpenAI API key.

3. **Execution**:
   - Navigate to the project directory in your terminal or command prompt.
   - Run the script using:
     ```
     python conversation_analyzer.py
     ```
   - The script will analyze the conversation provided in `sample_conversation.txt` using the OpenAI model and print the result.

## Potential Applications
- **Social Media Platforms**: Monitor user interactions to ensure community guidelines are maintained.
- **E-commerce Platforms**: Prevent illegal or unauthorized sales by screening user interactions.
- **Forums and Discussion Boards**: Ensure the conversation stays relevant and within the platform's guidelines.
- **Customer Support Platforms**: Detect and manage potentially harmful conversations between users and support agents.

## Disclaimer
While ConversationGuardian is designed to be highly effective, no system is infallible. It's essential for platform administrators to use this tool as part of a broader strategy and not rely solely on it for moderation.

## Contribution
We welcome contributions to enhance ConversationGuardian's capabilities. Please review our contribution guidelines and submit a pull request.

## License
This project is licensed under the MIT License. Please refer to the `LICENSE` file for more details.
