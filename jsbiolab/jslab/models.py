#_*_ encoding: utf-8 _*_
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题',max_length=50)
    content = models.TextField(u'内容')
    time  = models.DateTimeField(default=timezone.now)

    class order:   #排序方式，按时间排序
        ordering = ('time')
    
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.title

class Pphoto(models.Model):
    pphoto = models.ForeignKey(Article, on_delete = models.CASCADE)   #外键,指向临一表article表
    description = models.CharField(max_length=20 ,null= 'True', default = '添加对图片的描述')
    url = models.URLField(default="http://i.imgur.com/Z230eeq.png")

    def __str__(self):  #让列表中文显示
        return self.description


class userInfor(models.Model):
     
    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
    address = models.CharField(max_length=128)
