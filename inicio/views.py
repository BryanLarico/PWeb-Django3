from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def myHomeview(request, *args, **kwargs):
    return render(request, 'index.html', {})
  
def anotherView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h1>Otra vista desde DJango</h1>')
