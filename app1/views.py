from django.shortcuts import render

# Create your views here.
def index(requet):
    return render(requet,'index.html')