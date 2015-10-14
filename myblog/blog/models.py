# -*- coding: utf-8 -*-
from django.contrib.auth.models import *
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class User(AbstractUser):
    pass


# Create your models here.
# 博客用户表
class BlogUser(models.Model):
    user = models.CharField(verbose_name="登陆账号", max_length=30, blank=False, null=True, unique=True)
    password = models.CharField(verbose_name="登陆密码", max_length=20, blank=False, null=True)

    name = models.CharField(verbose_name="博主名称", max_length=100, blank=False, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to="avatar/%Y/%m", blank=True)
    introduce = models.TextField(verbose_name="介绍", blank=True, null=True)

    qq = models.CharField(verbose_name="QQ", max_length=20, blank=True, null=True)
    wechat = models.CharField(verbose_name="微信", max_length=20, blank=True, null=True)
    weibo = models.CharField(verbose_name="微博", max_length=20, blank=True, null=True)
    github = models.CharField(verbose_name="github", max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.user


# 博客留言表
class BlogMessage(models.Model):
    name = models.CharField(verbose_name="留言者名称", max_length=100, blank=False, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to="avatar/%Y/%m", blank=True)

    body = models.TextField(verbose_name="留言内容", blank=False, null=True)
    email = models.EmailField(verbose_name="电子邮箱", blank=False, null=True)
    time = models.DateTimeField(verbose_name="留言时间", blank=False, null=True)
    web = models.CharField(verbose_name="网站", max_length=20, blank=True, null=True)
    message = models.ForeignKey('self', blank=True, null=True, verbose_name="留言")

    def __unicode__(self):
        return self.body


# 博客友情链接表
class BlogFriend(models.Model):
    name = models.CharField(verbose_name="邻居", max_length=100, blank=False, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to="avatar/%Y/%m", blank=True)
    link = models.CharField(verbose_name="网站", max_length=20, blank=False, null=True)

    def __unicode__(self):
        return self.name


# 文章留言表
class BlogArticleComment(models.Model):
    name = models.CharField(verbose_name="留言者名称", max_length=100, blank=False, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to="avatar/%Y/%m", blank=True)
    time = models.DateTimeField(verbose_name="留言时间", blank=False, null=True)
    body = models.TextField(verbose_name="留言内容", blank=False, null=True)
    email = models.EmailField(verbose_name="电子邮箱", blank=False, null=True)
    web = models.CharField(verbose_name="网站", max_length=20, blank=True, null=True)
    comment = models.ForeignKey('self', blank=True, null=True, verbose_name="留言")

    def __unicode__(self):
        return self.body


# 文章分类表
class BlogArticleCategory(models.Model):
    name = models.CharField(verbose_name="分类名称", max_length=50, blank=False, null=True)

    def __unicode__(self):
        return self.name


# 文章标签表
class BlogArticleTag(models.Model):
    name = models.CharField(verbose_name="标签名称", max_length=50, blank=False, null=True)

    def __unicode__(self):
        return self.name


# 文章表
class BlogArticle(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=50, blank=False, null=True)
    body = models.TextField(verbose_name="文章内容", blank=False, null=True)
    author = models.ForeignKey(BlogUser, verbose_name="文章作者", blank=False, null=True)
    time = models.DateTimeField(verbose_name="更新时间", blank=False, null=True)

    like = models.IntegerField(verbose_name="喜欢", default=0, blank=False, null=True)
    pv = models.IntegerField(verbose_name="浏览量", default=0, blank=False, null=True)
    category = models.ForeignKey(BlogArticleCategory, verbose_name="文章分类", blank=False, null=True)
    tag = models.ManyToManyField(BlogArticleTag, verbose_name="文章标签", blank=False, null=True)
    comment = models.ForeignKey(BlogArticleComment, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.title
