from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import User, Employees

# Create your views here.

def register(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            return HttpResponse("User Already Exists")

        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(firstName=firstName, lastName=lastName, email=email, password=password)
        user.save()
        request.session['email'] = email
        return redirect('login')
    
    return render(request,'register.html')

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email, password=password).exists():  
            request.session['email'] = email
            return render(request, 'home.html')
        else:
            return HttpResponse("Either email or password is incorrect.")
    
    return render(request, 'index.html')

def home(request):
    # emp = Employees.objects.all()

    # detail = {
    #     'emp':emp
    # }   
    if 'email' in request.session:
        email = request.session['email']
        emp = Employees.objects.all()
        detail = {'emp': emp, 'email': email}
        return render(request, 'home.html', detail)
    else:
        return HttpResponse("Please log in.")
    # return render(request, 'home.html', detail)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        addEmp = Employees(name=name, email=email, address=address, phone=phone)
        addEmp.save()
        return redirect('home')

    return render(request,'index.html')

def edit(request):

    emp = Employees.objects.all()

    detail = {
        'emp':emp
    }

    return render(request,'index.html', detail)

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        updateEmp = Employees(id=id, name=name, email=email, address=address, phone=phone)  
        updateEmp.save()  
        return redirect('home')    

    return render(request,'index.html')

def delete(request, id):
    emp = Employees.objects.filter(id=id)
    emp.delete()

    return redirect('home')    

def logout(request):
    del request.session['email']
    return HttpResponse('Thank you for visiting')

