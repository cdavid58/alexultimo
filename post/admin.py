from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Img_Post)
admin.site.register(Likes_Post)
admin.site.register(Comment)
admin.site.register(Likes_Comment)