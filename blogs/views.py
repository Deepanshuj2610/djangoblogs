from django.shortcuts import render
from .models import blog

# Create your views here.
def home(request):
    model={}
    model['blog'] = blog.objects.all()
    return render(request, 'home.html', model)
    