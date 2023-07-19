from django.contrib import admin

# Register your models here.
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django.db import models

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Post, PostAdmin)