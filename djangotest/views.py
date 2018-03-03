from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import tagPairCompare

# Create your views here.

def home(request):
    #Tags = tags.objects.all()
    TagPairCompares = tagPairCompare.objects.filter(tag = 'python')
    #return render(request, 'home.html',{'tags':Tags})
    return render(request, 'home.html',{'tagPairCompares':TagPairCompares})

"""
def tag_detail(request, id):
    try:
        tag = tags.objects.get(id = id)
    except tags.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'tag_detail.html',{'tag':tag})
    """