import os
import json
import urllib.request
from dotenv import load_dotenv

# 1.load environment variable from .env file
load_dotenv()

# 2. get the api key from environment variable
api_key = os.getenv("OPENROUTER_API_KEY")

# 3.setup openrouter target url and headers 
url="https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 4.define the json request payload
payload = {
    "model": "openai/gpt-oss-20b:free",
    "messages":[
        {
        "role": "user",
        "content": "Explain the concept of multi-agent autonomous systems"
        }
    ]
}

# 5.compile and excute the http request

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers=headers)
print("sending request to open router")
try:
    with urllib.request.urlopen(req) as response:
        # read the raw byte response
        raw_response = response.read()
        
        #decode the  byte response to string
        result = json.loads(raw_response.decode('utf-8'))

        ai_response = result["choices"][0]["message"]["content"]
        print("AI response: ",ai_response)

except Exception as e:
    print("Error during API request:",e)