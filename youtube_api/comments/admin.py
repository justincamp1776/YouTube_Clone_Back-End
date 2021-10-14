from django.contrib import admin
from .models import Comment
from .models import Reply

admin.site.register(Comment)
admin.site.register(Reply)
# Register your models here.
