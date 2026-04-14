from django.shortcuts import render, redirect
from item.models import Category,Item
from  .forms import SignupForm
def index(request):
    return render(request,"core/base.html")

def index(request):
    items=Item.objects.filter(is_sold=False)[:6]
    categories=Category.objects.all()
    return render(request,"core/index.html",{"items":items, "categories": categories})

def contact(request):
    return redirect(request,"core/contact.html")

def About_us(request):
    return render(request,"core/About_us.html")

def signup(request):

    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")  
    else:
        form=SignupForm
    return render(request,'core/signup.html',{"form":form})







