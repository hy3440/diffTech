from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import tagPairCompare

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def tagpair(request,Tag):
    
    TagPairCompares = tagPairCompare.objects.filter(tag = Tag).values('tag','simiTag')
    return render(request, 'tagpair.html',{'tagPairCompares':TagPairCompares})

def tagcompare(request,tag,simi):
    #Tags = tags.objects.all()
    Tag = tag
    SimiTag = simi
    TagPairCompares = tagPairCompare.objects.filter(tag = Tag, simiTag = SimiTag).values('compare')
    compares = []
    for eachone in TagPairCompares:
        compares.append(eachone)
    Compare = compares[0]['compare']
    items = Compare.strip().split(',')
    features = {}
    
    i = 0 #loop current index
    k = '' #last feature 
    for item in items:
        if i % 3 == 0:
            features[item] = [] #add in new comparable feature
            k = item
        else:
            features[k].append(item)
        i+=1
    #return render(request, 'home.html',{'tags':Tags})
    return render(request, 'tagcompare.html',{'Features':features})

def inputtag(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        Tag = request.POST.get('tag')
        TagPairCompares = tagPairCompare.objects.filter(tag = 'python').values('tag','simiTag')
        #return render(request, 'tagpair.html',{'tagPairCompares':TagPairCompares})
        return render(request, 'tagcompare.html',{'Features':{'visability':[1,2]}})

"""
def tag_detail(request, id):
    try:
        tag = tags.objects.get(id = id)
    except tags.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'tag_detail.html',{'tag':tag})
    """