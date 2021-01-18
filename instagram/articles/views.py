from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'complete!')
            return redirect('articles:index')
        messages.warinig(request,  'OH shit, please confirm form!')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/forms.html', context)