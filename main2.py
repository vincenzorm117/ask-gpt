import http.client
import json
import os

authHeader = "Bearer " + os.getenv("OPENAI_API_KEY")

prompt = input()

# Define the target website
website = "api.openai.com"

# Define the data to be sent in the request body
data = {"model": "text-davinci-003", "prompt": prompt, "temperature": 0, "max_tokens": 512}
headers = {"Content-type": "application/json", "Authorization": authHeader}

# Connect to the website
conn = http.client.HTTPSConnection(website)

# Send the POST request
conn.request("POST", "/v1/completions", json.dumps(data), headers)

# Get the response
res = conn.getresponse()

# Print the response status and data
# print(res.status, res.reason)
data = res.read()
# print(data.decode("utf-8"))
data = data.decode("utf-8")

# Parse the response data as JSON
json_data = json.loads(data)

# Access the JSON data
print(json_data["choices"][0]["text"])

# Close the connection
conn.close()

