from django.shortcuts import render
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return{"Hello World"}

