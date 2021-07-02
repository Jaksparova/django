from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makaleniz Başarıyla Kaydedildi")
        return redirect("article:dashboard")
    return render(request, "addarticle.html", {"form": form})


def article(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(request, "article.html", {"article": article, "comments": comments})


@login_required(login_url="user:login")
def editArticle(request, id):
    article = get_object_or_404(Article, id=id, author=request.user)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makaleniz Başarıyla Güncellendi")
        return redirect("article:dashboard")
    return render(request, "edit.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id, author=request.user)
    article.delete()
    messages.success(request, "Makaleniz Başarıyla Silindi")
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        if request.POST.get("comment_author"):
            comment_author = request.POST.get("comment_author")
        else:
            comment_author = request.user
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:article", kwargs={"id": id}))


def likeComment(request, comment_id, article_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user
    
    comment.comment_like += 1
    comment.save()
    return redirect(reverse("article:article", kwargs={"id": article_id}))