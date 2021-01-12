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
        'menu': menu
    }
    return render(request, 'lunch.html', context)