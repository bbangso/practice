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