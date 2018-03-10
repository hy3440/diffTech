from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import tagpaircompare
from stackapi import StackAPI 

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def tagpair(request,Tag):

    SITE = StackAPI('stackoverflow')
    ori_tag = [Tag]

    TagPairCompares = tagpaircompare.objects.filter(tag = Tag).values('simitag')
    if not TagPairCompares:
        raise Http404("Tag pair does not exist")
    
    tagsFetch = []
    for tag in TagPairCompares:
        tagname = tag['simitag']
        tagsFetch.append(tagname)
    tagswiki = SITE.fetch('tags/{tags}/wikis',tags = tagsFetch)
    tagsWikiDict = {}
    for item in tagswiki['items']:
        excerpt = item['excerpt']
        excerpt = excerpt.strip().split('. ')[0]
        if '.&' in excerpt:
            excerpt = excerpt.split('.&')[0]
        tagsWikiDict[item['tag_name']] = excerpt

    ori_tagwiki = {}
    ori_wiki = SITE.fetch('tags/{tags}/wikis',tags = ori_tag)['items'][0]['excerpt']
    ori_wiki = ori_wiki.strip().split('. ')[0]
    if '.&' in ori_wiki:
        ori_wiki = excerpt.split('.&')[0]
    ori_tagwiki[Tag] = ori_wiki
    
    return render(request, 'tagpair.html',{'tagsWikiDicts':tagsWikiDict,'ori_tagwikis':ori_tagwiki})

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

        SITE = StackAPI('stackoverflow')
        ori_tag = [Tag]

        TagPairCompares = tagpaircompare.objects.filter(tag = Tag).values('simitag')
        if not TagPairCompares:
            raise Http404("Tag pair does not exist")

        tagsFetch = []
        for tag in TagPairCompares:
            tagname = tag['simitag']
            tagsFetch.append(tagname)
        tagswiki = SITE.fetch('tags/{tags}/wikis',tags = tagsFetch)
        tagsWikiDict = {}

        for item in tagswiki['items']:
            excerpt = item['excerpt']
            excerpt = excerpt.strip().split('. ')[0]
            if '.&' in excerpt:
                excerpt = excerpt.split('.&')[0]
            tagsWikiDict[item['tag_name']] = excerpt

        ori_tagwiki = {}
        ori_wiki = SITE.fetch('tags/{tags}/wikis',tags = ori_tag)['items'][0]['excerpt']
        ori_wiki = ori_wiki.strip().split('. ')[0]
        if '.&' in ori_wiki:
            ori_wiki = excerpt.split('.&')[0]
        ori_tagwiki[Tag] = ori_wiki

        return render(request, 'tagpair.html',{'tagsWikiDicts':tagsWikiDict,'ori_tagwikis':ori_tagwiki})