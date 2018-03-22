from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import tagpaircompare, tagpair as TP, relation
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
    """
    Tag = tag
    SimiTag = simi
    """

    tpair = sorted([tag,simi])
    Tag = tpair[0]
    SimiTag = tpair[1]
    SITE = StackAPI('stackoverflow')

    Relation = relation.objects.filter(tag = Tag, simitag = SimiTag).values('quality','example_id','example')
    if Relation:
        """
        compares = []
        for eachone in Relation:
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
        """
        #make a dictionary containing relation of quality, id, example
        features = {}
        IDS = []
        for eachone in Relation:
            postid = eachone['example_id']
            IDS.append(postid)

            #info = SITE.fetch('posts/{ids}/revisions', ids = IDS)
            """
            title = ''
            for item in info['items']:
                if 'last_title' in item.keys():
                    title = item['last_title']
                    break
                elif 'title' in item.keys():
                    title = item['title']
                    break
            title = title.replace('&quot;','"')

            """
            if ' overall' in eachone['quality']:
                quality = eachone['quality'].replace(' overall','')
                qualityCate = 'Others'
            elif ' in ' in eachone['quality']:
                quality = eachone['quality'].split(' in ')[0]
                qualityCate = eachone['quality'].split(' in ')[1]
            if qualityCate not in features.keys():
                features[qualityCate] = {}
                features[qualityCate][quality] = [[eachone['example'],eachone['example_id']]]
            else:
                if quality in features[qualityCate].keys():
                    features[qualityCate][quality].append([eachone['example'],eachone['example_id']])
                else:
                    features[qualityCate][quality] = [[eachone['example'],eachone['example_id']]]

        #IDS_sorted = sorted(IDS, reverse = True)
        info1 = SITE.fetch('posts/{ids}/revisions', ids = IDS) #the returning list of dictionary will be in descending order of the id
        info2 = SITE.fetch('answers/{ids}/questions', ids = IDS)
        id_title = {} #id of post and title of that post, put into a dictionary
        for item in info1['items']:
            if 'title' in item.keys():
                id_title[str(item['post_id'])] = item['title']
                IDS.remove(str(item['post_id']))
        IDS_sorted = sorted(IDS, reverse = True)                    
        for item in info2['items']: #appears in descending order
            if 'title' in item.keys():
                id_title[IDS_sorted.pop(0)] = item['title']

        #if IDS_sorted != []:
        #    raise Http404("Number of titles not equal to number if IDS")


        # featureswithtitle = features.copy()
        # i = 0
        for post_id, title in id_title.items():
            #i+=1
            found = 0 #find location for title to be attached

            #locate its position in features dictionary
            for qualityCate, qualityDict in features.items():
                #if qualityCate not in featureswithtitle.keys():
                    #featureswithtitle[qualityCate] = qualityDict
                for quality, details in qualityDict.items():
                    for item in details:
                        if post_id == item[1]:
                            item.append(title)
                            #featureswithtitle[qualityCate][quality][index]=['title','title']

                            found = 1
                            break
                    if found:
                        break
                if found:
                    break
            if not found:
                raise Http404("Dictionary pair not found for post_id "+ str(post_id))

        # if iamok:
        #     print('lala')








            #features[eachone['example_id']] = [qualityCate,quality,eachone['example']]
        
        
        
        tagsFetch = [Tag,SimiTag]

        tagswiki = SITE.fetch('tags/{tags}/wikis',tags = tagsFetch)
        tagsWikiDict_tag = {}
        tagsWikiDict_simi = {}
        tagsWikiDict = {}


        for item in tagswiki['items']:
            excerpt = item['excerpt']
            excerpt = excerpt.strip().split('. ')[0]
            if '.&' in excerpt:
                excerpt = excerpt.split('.&')[0]

            tagsWikiDict[item['tag_name']] = excerpt

        tagsWikiDict_tag[Tag] = tagsWikiDict[Tag]
        tagsWikiDict_simi[SimiTag] = tagsWikiDict[SimiTag]



    else:
        raise Http404("Tag pair does not exist")

    return render(request, 'tagcompare.html',{'Features':features,'TagsWikiDict_tag':tagsWikiDict_tag,'TagsWikiDict_simi':tagsWikiDict_simi})

def selecttag(request):

    if request.method == "POST":

        Tag = request.POST.get('tag')

        SITE = StackAPI('stackoverflow')
        ori_tag = [Tag]

        #TagPairCompares = tagpaircompare.objects.filter(tag = Tag).values('simitag')

        #get set of similar tags from tagpair database
        Tagpair = TP.objects.filter(tag__contains = '\t'+Tag+'\t') | TP.objects.filter(tag__startswith = Tag+'\t')
        """
        if not TagPairCompares:
            raise Http404("Tag pair does not exist")
        """

        #make sure tagpair exists
        if not Tagpair:
            raise Http404("Tag pair does not exist")

        """
        tagsFetch = []
        for tag in TagPairCompares:
            tagname = tag['simitag']
            tagsFetch.append(tagname)
        """

        #check the position of the searched tag: 0 or 1 or 2, and locate its similartags
        oritag = Tagpair[0].tag.strip().split('\t')
        pos = 0
        for index, value in enumerate(oritag):
            if value == Tag:
                pos = index
                break
        simitags = Tagpair[0].simitag.split(',')
        simitag = simitags[pos]
        tagsFetch = simitag.strip().split('\t')

        #assign simitags into tagsFetch

        tagswiki = SITE.fetch('tags/{tags}/wikis',tags = tagsFetch)
        tagsWikiDict = {}

        for item in tagswiki['items']:
            excerpt = item['excerpt']
            excerpt = excerpt.strip().split('. ')[0]
            if '.&' in excerpt:
                excerpt = excerpt.split('.&')[0]
            tagp = sorted([Tag, item['tag_name']])
            if relation.objects.filter(tag = tagp[0], simitag = tagp[1]):
                tagsWikiDict[item['tag_name']] = [excerpt,1]
            else:
                tagsWikiDict[item['tag_name']] = [excerpt,0]


        ori_tagwiki = {}
        ori_wiki = SITE.fetch('tags/{tags}/wikis',tags = ori_tag)['items'][0]['excerpt']
        ori_wiki = ori_wiki.strip().split('. ')[0]
        if '.&' in ori_wiki:
            ori_wiki = excerpt.split('.&')[0]
        ori_tagwiki[Tag] = ori_wiki

        return render(request, 'tagpair.html',{'tagsWikiDicts':tagsWikiDict,'ori_tagwikis':ori_tagwiki})