from django.shortcuts import render
from django.http import HttpResponse
from jsbiolab import settings
from .models import Article,Pphoto
from django.template.loader import get_template
from datetime import datetime

# Create your views here.
def index(request):
    template = get_template('index.html')
    art      = Article.objects.all()
    now      = datetime.now()
    html     = template.render(locals())
    return HttpResponse(html)

    # Create your views here.
def index2(request):
    template = get_template('index2.html')
    art      = Article.objects.all()
    now      = datetime.now()
    html     = template.render(locals())
    return HttpResponse(html)

def index3(request):
    template = get_template('index3.html')
    art      = Article.objects.all()
    now      = datetime.now()
    html     = template.render(locals())
    return HttpResponse(html)

def news(request):
    template = get_template('news.html')
    art      = Article.objects.all()
    now      = datetime.now()
    html     = template.render(locals())
    return HttpResponse(html)

def services(request):
    template = get_template('services.html')
    art      = Article.objects.all()
    now      = datetime.now()
    html     = template.render(locals())
    return HttpResponse(html)

def connect(request):
    template = get_template('connect.html')
    art      = Article.objects.all()
    now      = datetime.now()
    html     = template.render(locals())
    return HttpResponse(html)

def homepage(request):
    article = Article.objects.all()
    article_list=list()
    for i,j in enumerate(article,1):
        article_list.append("No.{}:".format(str(i))+str(j)+"<hr>")
        article_list.append("<small>"+str(j.content)+"</small><br><br>")

        #print(j.content.encode('utf-8'))
    return HttpResponse(article_list)
