from django.shortcuts import render   
from .models import Article     # importing Article model
from django.http import HttpResponse, JsonResponse  # different response for different situations
from rest_framework.parsers import JSONParser   # to parse request data into JSON
from .serializers import ArticleSerializer      # importing serilizer 
from django.views.decorators.csrf import csrf_exempt    # to exempt CSRF protection
# Create your views here.

@csrf_exempt       
def article_list(request):  # lists out all data
    if request.method == 'GET':
        articles = Article.objects.all()    # get all Articles
        serializer = ArticleSerializer(articles, many = True)   # serialize all articles
        return JsonResponse(serializer.data, safe = False)      # return JSON response

    elif request.method == 'POST':
        data = JSONParser().parse(request)      # get article data from request 
        serializer = ArticleSerializer(data = data)     # serialize the data
        if serializer.is_valid():       # if valid then save the article
            serializer.save()
            return JsonResponse(serializer.data, status = 201)      # successfully added new article
        return JsonResponse(serializer.errors, status = 400)        # failed to add new article

@csrf_exempt
def article_detail(request, pk):
    try:        
        article = Article.objects.get(pk = pk)      # try to get article with given id
    
    except Article.DoesNotExist:
        return HttpResponse(status = 404)           # failed to get the article user requested

    if request.method == 'GET':                     # return that particular article
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':                   # update the article
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':                # delete the article
        article.delete()
        return HttpResponse(status = 204)