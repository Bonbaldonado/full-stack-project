from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World! This is a Test')

def my_name(request):
    context = {'name': 'try'}
    return render(request, 'myapp/myapp.html', context)