from django.contrib import admin
from models import *


# Register your models here.


admin.site.register(BlogUser)
admin.site.register(BlogMessage)
admin.site.register(BlogFriend)
admin.site.register(BlogArticleComment)
admin.site.register(BlogArticleCategory)
admin.site.register(BlogArticleTag)
admin.site.register(BlogArticle)
