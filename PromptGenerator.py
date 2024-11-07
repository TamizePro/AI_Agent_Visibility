import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

class PromptGenerator:
    def __init__(self) -> None:
        self.client = Groq()
        self.input_prompt = "Give a any prompt that can be passed to another LLM. Just give me the prompt and nothing else."
        
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

        print(completion.choices[0].message.content)

if __name__ == '__main__':
    promptGenerator = PromptGenerator()
    promptGenerator.generate_prompt()