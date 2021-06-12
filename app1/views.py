from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Appmodel
from .forms import Appform
from django.contrib import messages
# Create your views here.

def hello(request):
    return HttpResponse('Hello ')

#signup page
def signup(request):
    if request.method == 'POST':
        model = Appmodel()
        model.FirstName = request.POST['FirstName']
        model.MiddleName = request.POST['MiddleName']
        model.LastName = request.POST['LastName']
        model.Phone = request.POST['Phone']
        model.Address = request.POST['Address']
        model.Email = request.POST['Email']
        model.Password = request.POST['Password']
        model.save()
      
    return render(request, 'signup.html')        


# retrieve data
def show(request):
    model=Appmodel.objects.all()
    return render(request,'show.html',{'model':model})    


# delete data
def delete(request,id):
    model = Appmodel.objects.get(id=id)
    model.delete()
    return render(request,'show.html')

#edit data
def edit(request,id):
    model=Appmodel.objects.get(id=id)
    return render(request,'edit.html',{'model':model})


#update data
def update(request,id):
    model=Appmodel.objects.get(id=id)
    form=Appform(request.POST,instance=model)
    if form.is_valid():
        form.save()
    return redirect('show')
    return render(request,'edit.html')

#login page
def login(request):
    if request.POST:
        try:
            email=request.POST.get('Email')
            password=request.POST.get('Password')
            model=Appmodel.objects.get(Email=email)
            if model.Password==password:
                request.session['FirstName']=model.FirstName
                return redirect('show')
            else:
                return HttpResponse("<p><a href="">Wrong Password</p>")
        except:
            return HttpResponse("<p><a href="">No user found</p>")
    return render(request,'login.html')


def logout(request):
    if request.session.has_key('FirstName'):
        del request.session['FirstName']
        return redirect('login')
    return render(request,'login.html')
