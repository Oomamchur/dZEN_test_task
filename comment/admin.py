from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from comment.models import User, MainComment, Comment

admin.site.register(User, UserAdmin)
admin.site.register(MainComment)
admin.site.register(Comment)
