from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view(["GET", "POST"])
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """DRF API view"""
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()# this displays a random data
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # Also done this way
#         # data = model_to_dict(model_data)
#         data = model_to_dict(model_data, fields=['id', 'title']) # You can just add the fields you want in alone
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body) # takes a string of json data and converts it into python dictionary
#     except:
#         pass
    
#     # print(body)
#     print(data)
#     print(data.keys())
#     print(request.GET)
    
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     # return JsonResponse({"message": "Hi Dear, this is your django API Response"})
#     return JsonResponse(data)