from django.shortcuts import render
from employee.models import Company

# Create your views here.
def home(request):
    k = Company.objects.all()
    return render(request,'home.html',{'company':k})

def add(request):
    if(request.method=="POST"):
        n=request.POST['n']
        nu=request.POST['nu']
        d=request.POST['d']
        e=request.POST['e']
        i=request.FILES.get('i')
        c=Company.objects.create(name=n,idnumber=nu,designation=d,experience=e,image=i)
        c.save()
        return home(request)
    return render(request,'add.html')

