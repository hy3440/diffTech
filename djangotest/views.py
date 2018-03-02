from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import tags, id_postidtypes

# Create your views here.

def home(request):
    #Tags = tags.objects.all()
    Id_postidtypes = id_postidtypes.objects.all()

    #return render(request, 'home.html',{'tags':Tags})
    return render(request, 'home.html',{'id_postidtypes':Id_postidtypes})

"""
def tag_detail(request, id):
    try:
        tag = tags.objects.get(id = id)
    except tags.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'tag_detail.html',{'tag':tag})
    """