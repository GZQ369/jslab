# encoding='utf-8'
from django.http import HttpResponse
from jsbiolab import settings
from .models import Article,Pphoto
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

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
    for i,j in enumerate(article):
        article_list.append("No.{}:".format(str(i))+str(j)+"<hr>")
        article_list.append("<small>"+str(j.content)+"</small><br><br>")

        #print(j.content.encode('utf-8'))
    return HttpResponse(article_list)

def detail(request,title):
    template = get_template('detail.html')
    now      = datetime.now()
    try:
        art      = Article.objects.get(title=title)
        if art !=None:
            html     = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect