from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    return render(request, "result.html")

def process(request):
    if request.method =="POST":
        request.session ['name'] = request.POST['name']
        request.session ['location'] = request.POST['location']
        request.session ['language'] = request.POST['language']
        request.session ['comment'] = request.POST['comment']
        return redirect('/result')
    return redirect('/')

