import requests

endpoint = "https://www.httpbin.org/status/200/"
endpoint = "https://www.httpbin.org"
endpoint = "https://www.httpbin.org/anything" #returns a json format (JavaScript Object Notation)

get_responde = requests.get(endpoint) #HTTP Request
print(get_responde.text) # Prints the source code

