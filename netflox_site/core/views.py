from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index-2.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def pricing(request):
    return render(request, 'pricing.html')


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def movie(request):
    return render(request, 'movie.html')

def tv_show(request):
    return render(request, 'tv-show.html')