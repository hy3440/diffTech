from stackapi import StackAPI 

SITE = StackAPI('stackoverflow')
tags = SITE.fetch('tags/{tags}/wikis',tags = ['python','java'])
tagsDict = tags['items']
print(tagsDict)