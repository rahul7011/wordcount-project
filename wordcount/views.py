from django.http import HttpResponse
from django.shortcuts import render
import operator

#HOME FUNCTION

def home(request):
    return render(request,'home.html')
#ABOUT FUNCTION

def about(request):
    return render(request,'about.html')

#COUNT FUNCTION

def count(request):
    text=request.GET['textbox']
    words=text.split()
    datadictionary={}
    for word in words:
        if word in datadictionary:
            #increment
            datadictionary[word]+=1
        else:
            #add the new word
            datadictionary[word]=1
    sortedwords=sorted(datadictionary.items(),key=operator.itemgetter(1),reverse=True)
            
    return render(request,'count.html',{'text':text,'words':len(words),'sortedwords':sortedwords})

    