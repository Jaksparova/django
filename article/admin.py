from django.contrib import admin

from .models import Article, Comment
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_date")
    list_display_links = ("title", "author")
    search_fields = ['title']
    list_filter = ('created_date',)

    class Meta:
        model = Article


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_author", "comment_content", "comment_date")
    list_display_links = ("comment_content",)
    search_fields = ['comment_content']
    list_filter = ('comment_date',)

    class Meta:
        model = Comment
