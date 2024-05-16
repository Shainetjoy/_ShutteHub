from django.contrib import auth, messages
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from .forms import UserRgistration, CustomerREgistration, ManufacturersDtlForms, Sales_TeamFormClass,EnquiryForm
from .models import ManufacturersDtlClass


# Create your views here.
def shutterIndex(request):
    EnquiryF = EnquiryForm()
    if request.method == 'POST':
        EnquiryF = EnquiryForm(request.POST)
        if EnquiryF.is_valid():
            EnquiryF.save()
            return redirect('shutterIndex')
    return render(request, 'shutterIndex.html',{"EnquiryF":EnquiryF})


def shutterSignin(request):
    if request.method == 'POST':
        username = request.POST.get('Uname')
        password = request.POST.get('pword')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('shutterAdminIndex')
        elif user is not None and user.is_Manufacturers:
            login(request,user)
            return redirect('ManufacturersIndex')
        elif user is not None and user.is_Customer:
            login(request,user)
            return redirect('shutterUserIndex')
        elif user is not None and user.is_Sales:
            print("4")

            login(request,user)
            return redirect('SalesIndex')
        else:
            messages.info(request, "Invalid credentials ")
    return render(request, 'shutterSignin.html')


def CustomerRegistrationFun(request):
    UserRegistration = UserRgistration()
    CustomerRegister = CustomerREgistration()
    if request.method == 'POST':
        UserRegistration = UserRgistration(request.POST)
        CustomerRegister = CustomerREgistration(request.POST)
        if UserRegistration.is_valid() and CustomerRegister.is_valid():
            user = UserRegistration.save(commit=False)
            user.is_Customer = True
            user.save()
            Customer = CustomerRegister.save(commit=False)
            Customer.user = user
            Customer.save()
            print("customenr registration sucessfull")
            messages.info(request, "Customer Registration Successfully")
            return redirect('shutterSignin')
    return render(request, 'Registration/CustomerREgistration.html',
                  {'UserRegistration': UserRegistration, 'CustomerRegister': CustomerRegister})


def ManufacturersDtlFun(request):
    userRegistration = UserRgistration()
    manufacturerForm = ManufacturersDtlForms()
    if request.method == 'POST':
        userRegistration = UserRgistration(request.POST)
        manufacturerForm = ManufacturersDtlForms(request.POST, request.FILES)
        if userRegistration.is_valid() and manufacturerForm.is_valid():
            user = userRegistration.save(commit=False)
            user.is_Manufacturers = True
            user.save()
            manufact = manufacturerForm.save(commit=False)
            manufact.user = user
            manufact.save()
            messages.info(request, "Manufacturer Registration Successfully Completed")
            return redirect('shutterSignin')
    return render(request, 'Registration/Manufacturers.html',
                  {'userRegistration': userRegistration, 'manufacturerForm': manufacturerForm})


def Sales_TeamModelClass(request):
    userRegistration = UserRgistration()
    salesTEam = Sales_TeamFormClass()
    if request.method == 'POST':
        userRegistration = UserRgistration(request.POST)
        salesTEam = Sales_TeamFormClass(request.POST)
        if userRegistration.is_valid() and salesTEam.is_valid():
            user = userRegistration.save(commit=False)
            user.is_Sales = True
            user.save()
            sale = salesTEam.save(commit=True)
            sale.user = user
            messages.info(request, 'salesTEam team registred successfully completed')
            return redirect('shutterSignin')
    return render(request, 'Registration/Sales.html', {'userRegistration': userRegistration, 'salesTEam': salesTEam})


def shutterAdminIndex(request):
    return render(request, 'shutterAdminIndex.html')


def shutterUserIndex(request):
    return render(request, 'shutterUserIndex.html')


def ManufacturersIndex(request):
    u = request.user.id
    myProfile = ManufacturersDtlClass.objects.get(user_id=u)
    return render(request, 'ManufacturersIndex.html',{"myProfile":myProfile})


def SalesIndex(request):
    return render(request, 'SalesIndex.html')


def log_out(request):
    logout(request)
    return redirect('shutterIndex')


