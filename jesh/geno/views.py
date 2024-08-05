from django.shortcuts import render
def index(request):
    return render(request,'apps/index.html')
def home(request):
    return render(request,'apps/home.html')
def flavours(request):
    return render(request,'apps/flavours.html')
def shop(request):
    return render(request,'apps/shop.html')
def contact(request):
    return render(request,'apps/contact us.html')

