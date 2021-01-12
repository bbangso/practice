from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')