from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    link = ""
    show = False
    if request.method == "POST":
        
        link = request.POST['link']
        if len(str(link)) !=0:
            show = True
            return render(request,'index.html',{'link': link, 'show':show})
        else:
            show = False



    return render(request,'index.html',{'link': link, 'show':show})

