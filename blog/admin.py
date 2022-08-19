from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "created_date",
        "updated_date",
    )


admin.site.register(Article, ArticleAdmin)
