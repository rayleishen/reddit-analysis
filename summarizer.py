import openai
import json
import pandas as pd


with open('config.json') as config_file:
    data = json.load(config_file)

key = data['openai_key']

openai.api_key = key

# List available models
pd.json_normalize(openai.Model.list(), "data")


# Converse with GPT with openai.ChatCompletion.create()
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # or "gpt-4"
    messages=[{
            "role": "system", 
            "content": 'You are a stand-up comic performing to an audience of data scientists. Your specialist genre is dad jokes.'
        }, {
            "role": "user", 
            "content": 'Tell a joke about statistics.'
        }, {
            "role": "assistant", 
            "content": 'My last was gig at a statistics conference. I told 100 jokes to try and make people laugh. No pun in ten did.'
        }

    ]
)

# Check the response status
response["choices"][0]["finish_reason"]

# Extract the AI output content
ai_output = response["choices"][0]["message"]["content"]

# Render the AI output content
#display(Markdown(ai_output))
