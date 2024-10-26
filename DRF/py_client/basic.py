import requests


endpoint = "https://www.httpbin.org/status/200/"
endpoint = "https://www.httpbin.org"
endpoint = "https://www.httpbin.org/anything" #returns a json format (JavaScript Object Notation)
endpoint = "http://127.0.0.1:8000/api/" # localhost:8000/

# get_responds = requests.get(endpoint) #HTTP Request
# get_responds = requests.get(endpoint, params={"abc":234}, json={"query": "Hello world!"}) #HTTP Request. params are querry parameters
get_responds = requests.post(endpoint, params={"abc":234}, json={"query": "Hello world!"}) #HTTP Request. params are querry parameters
# print(get_responds.text) # Prints the source code
# print(get_responds.json()['message']) # Prints the JSON format
print(get_responds.json()) # Prints the JSON format
# print(get_responds.status_code) # Prints the status code

