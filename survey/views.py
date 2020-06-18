from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method =="POST":
        return render (request, "result.html")
    return redirect (request, "index.html")