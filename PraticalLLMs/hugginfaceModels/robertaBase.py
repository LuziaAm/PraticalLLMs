import requests
import secretsToken


API_URL = "https://api-inference.huggingface.co/models/roberta-base"
ROBERTA_AUTH = secretsToken.ROBERTA_AUTH


headers = {"Authorization": f"Bearer {ROBERTA_AUTH}"}
print(headers)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({"inputs": "The answer to the universe is <mask>.",})
print(output)
