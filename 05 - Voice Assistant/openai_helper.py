import openai
from api_secrets import OPEN_AI_KEY

openai.api_key = OPEN_AI_KEY


def ask_computer(prompt):
    response = openai.Completion.create(
		engine="text-davinci-002",
		prompt = prompt,
  		temperature=0,
  		max_tokens=100,
	)
    return response["choices"][0]["text"]
