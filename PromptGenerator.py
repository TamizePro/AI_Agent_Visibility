import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

class PromptGenerator:
    def __init__(self) -> None:
        self.client = Groq()
        self.input_prompt = """Give a any prompt that can be passed to llama3-groq-70b-8192-tool-use-preview.
                            Give me a prompt that may or may not require the use of some of the following tools that are available to the model:

                            1. **Search Engine**: Can search the internet for information using a search engine tool.
                            2. **Weather API**: Can can fetch current weather information for a specified location using a weather API tool.
                            3. **News API**: Can fetch the latest news articles for a specified topic or location using a news API tool.
                            4. **Stock Price API**: Can fetch the latest stock prices for a specified company using a stock price API tool.
                            5. **Currency Converter**: Can convert currency from one unit to another using a currency converter tool.
                            6. **Math Calculator**: Can perform mathematical calculations using a math calculator tool.
                            7. **Text Summarizer**: Can summarize long pieces of text into shorter versions using a text summarizer tool.
                            8. **Image Recognizer**: Can recognize and describe images using an image recognition tool.
                            9. **Chatbot**: Can have conversations and answer questions using a chatbot tool.
                            10. **QA Model**: Can answer questions based on an input passage of text using a QA model tool.

                            Just give me the prompt and nothing else."""
        
    def generate_prompt(self):
        completion = self.client.chat.completions.create(
            model="llama-3.2-1b-preview",
            messages=[
                {
                    "role": "user",
                    "content": self.input_prompt
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        return completion.choices[0].message.content

if __name__ == '__main__':
    promptGenerator = PromptGenerator()
    print(promptGenerator.generate_prompt())