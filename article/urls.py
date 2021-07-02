from django.contrib import admin
from django.urls import path
from . import views


app_name = "article"


urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('article/<int:id>', views.article, name="article"),
    path('edit/<int:id>', views.editArticle, name="editarticle"),
    path('delete/<int:id>', views.deleteArticle, name="deletearticle"), 
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="addcomment"), 
    path('like/<int:comment_id>/<int:article_id>', views.likeComment, name="likecomment"), 
]