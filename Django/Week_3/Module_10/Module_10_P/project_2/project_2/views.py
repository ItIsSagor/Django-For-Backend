from django.shortcuts import render

def html(request):
    return render(request, "home.html")