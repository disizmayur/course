from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordcount = fulltext.split()
    worddic = {}
    for word in wordcount:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1
    sortedwords=sorted(worddic.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'bnb.html',{'fulltext':fulltext,'wordcount':len(wordcount),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')