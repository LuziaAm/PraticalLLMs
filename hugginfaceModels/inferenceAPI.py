import json
import requests
import unittest

import secretsToken


# Color results
RED = "\033[0;31m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
RESET = "\033[0;0m"
GREEN = "\033[0;32m"

# gpt2
API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_URL2 = "https://api-inference.huggingface.co/models/bert-base-uncased"
API_URL3 = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_URL4 = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2" 


API_TOKEN = secretsToken.API_TOKEN
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query("Can you please let us know more details about your ")
print(YELLOW + 'gpt2' + RESET, data)


# bart-large-cnn
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL2, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query({"inputs": "The answer to the universe is [MASK]."})
print(YELLOW + 'bart-large-cnn' + RESET, data)


# roberta-base-squad2
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL4, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query(
    {
        "inputs": {
            "question": "What's my name?",
            "context": "My name is Clara and I live in Berkeley.",
        }
    }
)
print(YELLOW + 'roberta-base-squad2' + RESET, data)


# bert-base-uncased
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL3, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query(
    {
        "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
        "parameters": {"do_sample": False},
    }
)
print(YELLOW + 'bert-base-uncased' + RESET, data)


# Test response bert-base-uncased
class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        # assertEqual() to check equality of data return
        self.assertEqual(data, [{"summary_text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world.", },],)


# Response
if __name__ == '__main__':
    unittest.main()

