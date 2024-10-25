import requests

endpoint = "https://www.httpbin.org/status/200/"
endpoint = "https://www.httpbin.org"
endpoint = "https://www.httpbin.org/anything" #returns a json format (JavaScript Object Notation)
endpoint = "localhost:8000/" # http://127.0.0.1:8000/

get_responde = requests.get(endpoint) #HTTP Request
print(get_responde.text) # Prints the source code
# print(get_responde.json()) # Prints the JSON format
print(get_responde.status_code) # Prints the status code

