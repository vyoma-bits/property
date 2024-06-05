from django.shortcuts import render,redirect
from input.models import Location
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    print(context)
    return render(request,"user/index.html",context)
def loginc(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)

        if user is not None:

            login(request,user)

            # Pass the username to the redirected view using a context variable

            return redirect("display")





        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'user/loginc.html')


