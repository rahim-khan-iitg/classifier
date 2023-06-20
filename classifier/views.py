from django.shortcuts import render
from . import forms
from django.views.decorators.csrf import csrf_protect
from .upload import handle_upload,predict

@csrf_protect
def home(request):
    if request.method=="POST":
        form=forms.Image(request.POST,request.FILES)
        if form.is_valid():
            handle_upload(request.FILES['image'])
            x=predict()
        return render(request,"index.html",{"result":x,"form":forms.Image,"url":"media/a.jpg"})
    return render(request,"index.html",{"form":forms.Image,"result":""})