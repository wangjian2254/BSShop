from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Adress(models.Model):
    name = models.CharField(max_length=10,verbose_name=u'名称',help_text=u'地址名称')
    fAdd = models.ForeignKey('Adress',blank=True,null=True,verbose_name=u'父级地址',help_text=u'地址隶属于哪个地址')


class Paper(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'论文题目',help_text=u'论文的题目')
    orderno = models.CharField(max_length=100,verbose_name=u'订单编号',help_text=u'淘宝订单编号')
    user = models.ForeignKey(User,verbose_name=u'用户',help_text=u'发布需求的人')
    content = models.CharField(max_length=2000,verbose_name=u'内容',help_text=u'毕业设计的内容')
    adress = models.ForeignKey(Adress,blank=True,null=True,verbose_name=u'地址',help_text=u'用户所属地址，防止重复')
    status = models.IntegerField(default=0,verbose_name=u'状态',help_text=u'毕设状态')
    orderstatus = models.IntegerField(default=0,verbose_name=u'付费状态',help_text=u'支付宝付费状态')
    isdel = models.BooleanField(default=False,verbose_name=u'是否删除',help_text=u'记录的状态')

class PaperReplay(models.Model):
    paper = models.ForeignKey(Paper,verbose_name=u'毕设',help_text=u'')
    content = models.CharField(max_length=2000,verbose_name=u'内容',help_text=u'沟通内容')
    freplay = models.ForeignKey('PaperReplay',blank=True,null=True,verbose_name=u'父级沟通',help_text=u'针对沟通的回复')
    status = models.IntegerField(default=0,verbose_name=u'状态',help_text=u'是否回复、阅读')
    user = models.ForeignKey(User,verbose_name=u'发布者',help_text=u'')
    ruser = models.ForeignKey(User,related_name=u'replay_user',verbose_name=u'回复者',help_text=u'')
    isdel = models.BooleanField(default=False,verbose_name=u'是否删除',help_text=u'记录的状态')

class File(models.Model):
    file = models.FileField(upload_to='file',verbose_name=u'附件')
    paper = models.ForeignKey(Paper,verbose_name=u'毕设',help_text=u'')
    freplay = models.ForeignKey(PaperReplay,blank=True,null=True,verbose_name=u'父级沟通',help_text=u'针对沟通的回复')
    isdel = models.BooleanField(default=False,verbose_name=u'是否删除',help_text=u'记录的状态')


class ImageFile(models.Model):
    file = models.ImageField(upload_to='image',verbose_name=u'附件')
    paper = models.ForeignKey(Paper,verbose_name=u'毕设',help_text=u'')
    freplay = models.ForeignKey(PaperReplay,blank=True,null=True,verbose_name=u'父级沟通',help_text=u'针对沟通的回复')
    isdel = models.BooleanField(default=False,verbose_name=u'是否删除',help_text=u'记录的状态')
