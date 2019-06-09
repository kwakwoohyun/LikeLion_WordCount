from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dict = {}

    for word in words :
        if word in word_dict :
            #Increase
            word_dict[word] += 1
        else :
            #add to dict
            word_dict[word] = 1
                                            #마지막 인자 = 사전 {'키':값} / 키 = html에서 사용
    return render(request, 'result.html',{'full' : text, 'total' : len(words), 'dict' : word_dict.items()}) 