from django.contrib import admin
from . import models
# Register your models here.
class Articleadmin(admin.ModelAdmin):
    list_display = ('title','time')
    def save_model(self, request, obj, form, change):
        if change:# 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:# 新增的时候
            obj_original = None
 
        obj.user = request.user
        obj.save()

class Pphotoadmin(admin.ModelAdmin):
    list_display = ('description','url')

class userInforadmin(admin.ModelAdmin):
    list_display = ('username','email','sex')    #在详情页展示信息的list列表信息

admin.site.register(models.Article, Articleadmin)
admin.site.register(models.Pphoto,Pphotoadmin)
admin.site.register(models.userInfor,userInforadmin)
