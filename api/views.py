from django.shortcuts import render

# Create your views here.
def editimage(request):
    if request.method == "POST":
        image = request.data.get()