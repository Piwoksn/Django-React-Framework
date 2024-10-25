from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body) # takes a string of json data and converts it into python dictionary
    except:
        pass
    
    # print(body)
    print(data)
    print(data.keys())
    print(request.GET)
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    # return JsonResponse({"message": "Hi Dear, this is your django API Response"})
    return JsonResponse(data)