from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')

def complete(request):
    # request는 요청과 관련된 정보들이 담긴 객체 이다
    # print(request.GET)
    # print(request.method)
    # print(request.path)

    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    return render(request, 'boards/complete.html', context)