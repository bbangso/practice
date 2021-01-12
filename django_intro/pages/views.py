from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'hello.html')

def lotto(request):
    pick = random.sample(range(1,46), 6)
    print(pick)
    context = {
        'pick': pick,
    }
    return render(request, 'lotto.html', context)

def iam(request):
    return render(request, 'iam.html')

def lunch(request):
    menupan = ['햄버거', '더콰트로', '피자', '초밥', '한우', '삼겹살']
    menu = random.choice(menupan)
    context = {
        'menu': menu,
        'menupan': menupan
    }
    return render(request, 'lunch.html', context)

def hi(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hi.html', context)

def add(request, a, b):
    res = a + b
    context = {
        'res' : res
    }
    return render(request, 'add.html', context)

def posts(request, num):
    content = 'Life is short, you need python!'
    replies = ['1111', '2222',' 유익한 글이네요!']
    no_replies = []
    user = 'admin'
    context = {
        'num' : num,
        'content' : content,
        'replies': replies,
        'no_replies' : no_replies,
        'user' : user,
    }
    return render(request, 'posts.html', context)