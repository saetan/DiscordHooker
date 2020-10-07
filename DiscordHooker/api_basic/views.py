from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Article
# Create your views here.

def home_page(request):
    return HttpResponse("<h1>Hello World</h1><script>x = 10; x += 10; console.log(x)</script>")

def product_detail_view(request, pk):
    try:
        obj = Article.objects.get(pk = pk)
    except Artcle.DoesNotExist:
        raise Http404
    return HttpResponse(f"Article ID {obj.id}")
