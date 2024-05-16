from django.shortcuts import render, redirect

from shutterApp.forms import ManufacturersDtlForms,addShutter
from shutterApp.models import ManufacturersDtlClass, ShutterDtls, OrderItems


def displayProfile(request):
    u = request.user.id
    myProfile = ManufacturersDtlClass.objects.get( user_id = u)
    return render(request,'Manufacturer/myProfile.html',{"myProfile":myProfile})


def updateProfile(request,id):
    Muser = ManufacturersDtlClass.objects.get(user_id = id)
    Muserform = ManufacturersDtlForms(instance = Muser )
    if request.method == 'POST':
        Muserform = ManufacturersDtlForms(request.POST,instance = Muser)
        if Muserform.is_valid():
            Muserform.save()
            return redirect('displayProfile')
    return render(request,'Manufacturer/updateProfile.html',{"Muserform":Muserform})


def ManViewProucts(request):
    products = ShutterDtls.objects.all()
    return render(request,"Manufacturer/manViewProduct.html",{"products":products})



def ManupdateProduct(request, product_Id):
    upProduct = ShutterDtls.objects.get(product_Id=product_Id)
    ShutterAddForm = addShutter(instance=upProduct)
    if request.method == 'POST':
        ShutterAddForm = addShutter(request.POST, request.FILES, instance=upProduct)
        if ShutterAddForm.is_valid():
            ShutterAddForm.save()
            return redirect('ManViewProucts')
    return render(request, 'Manufacturer/ManUpdateProduct.html', {'ShutterAddForm': ShutterAddForm})


def Manremove(request, product_Id):
    products = ShutterDtls.objects.get(product_Id=product_Id)
    products.delete()
    return redirect('ManViewProucts')


def Manview_order(request):
    data = OrderItems.objects.all()
    return render(request, 'Manufacturer/Manview_order.html', {'data': data})


def ManupdateStatus(request, product_Id):
    if request.method == 'POST':
        status = request.POST.get('status')
        print(status)
        OrderItems.objects.filter(product_Id=product_Id).update(Booking_status=status)
        return redirect('view_order')



