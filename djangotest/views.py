from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import tagpaircompare

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def tagpair(request,Tag):


    TagPairCompares = tagpaircompare.objects.filter(tag = Tag).values('tag','simitag')
    if not TagPairCompares:
        raise Http404("Tag pair does not exist")
    
    return render(request, 'tagpair.html',{'tagPairCompares':TagPairCompares})

def tagcompare(request,tag,simi):
    #Tags = tags.objects.all()
    Tag = tag
    SimiTag = simi

    TagPairCompares = tagpaircompare.objects.filter(tag = Tag, simitag = SimiTag).values('compare')
    if TagPairCompares:
        compares = []
        for eachone in TagPairCompares:
            compares.append(eachone)
        Compare = compares[0]['compare']
        items = Compare.strip().split()
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
        tagpair = {}
        tagpair[Tag] = SimiTag

    else:
        raise Http404("Tag pair does not exist")

    return render(request, 'tagcompare.html',{'Features':features,'tagpair':tagpair})

def selecttag(request):

    if request.method == "POST":

        Tag = request.POST.get('tag')
        TagPairCompares = tagpaircompare.objects.filter(tag = Tag).values('tag','simitag')

        if not TagPairCompares:
            raise Http404("Tag pair does not exist")

        return render(request, 'tagpair.html',{'tagPairCompares':TagPairCompares})