import openai, json

with open('config.json') as config_file:
    data = json.load(config_file)

key = data['openai_key']

openai.api_key = key

