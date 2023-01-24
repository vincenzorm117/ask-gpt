import os
import openai

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt
prompt = 'Give me a rhyme about why the sky is blue'

# Define the parameters for the API call
model = "text-davinci-002"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

# Extract the message from the API response
message = completions.choices[0].text

# Print the message
print(completions)

