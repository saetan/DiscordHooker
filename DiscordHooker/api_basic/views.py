from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):

    return HttpResponse("<h1>Hello World</h1><script>x = 10; x += 10; console.log(x);</script>")