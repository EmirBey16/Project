from django.contrib import admin
from .models import FilmNews, Tag, Add

# Register your models here.
admin.site.register(FilmNews)
admin.site.register(Tag)
admin.site.register(Add)