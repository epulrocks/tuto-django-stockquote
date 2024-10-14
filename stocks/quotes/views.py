from django.shortcuts import render
import requests, json

# Create your views here.
def home(request):

    # response = requests.get(url, headers=headers, params=querystring)
    # if response.status_code==200:
    #     response_content = {"success": True,
    #                         "data": response.json}
    # else:
    #     response_content = {"success": False}
    return render(request, "home.html", {"resp": "test"})

def aboutme(request):
    return render(request, "aboutme.html", {})