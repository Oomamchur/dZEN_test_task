from django.contrib import admin

from comment.models import MainComment, Comment

admin.site.register(MainComment)
admin.site.register(Comment)
