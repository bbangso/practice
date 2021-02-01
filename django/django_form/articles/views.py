from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        # POST /articles/new/
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False) # form의 객체를 가져오되 저장하지 않는다
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
        
    else:
        # GET /articles/new/
        form = ArticleForm()

    context = {
        'form' : form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/detail.html', context) 

@require_POST
@login_required
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)

            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
        }
        return render(request, 'articles/form.html', context)
    
    messages.warning(request, '본인글만 수정가능')
    # 403 메시지
    # from django.http import HttpResponseForbidden
    # return HttpResponseForbidden
    return redirect('articles:index')

@require_POST
@login_required
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = article.user
        comment.article = article
        comment.save()
        
        return redirect('articles:detail', article.pk)