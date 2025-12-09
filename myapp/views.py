# b_user
from django.shortcuts import render, HttpResponse   


# Create your views here.
def test(request):
    return HttpResponse("This is a_user test")

def aweb(request):
    return HttpResponse("This is a_user aweb.")
def bweb(request):
    return HttpResponse("This is b_user bweb! Done!")
