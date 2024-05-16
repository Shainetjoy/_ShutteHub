from django.shortcuts import render, redirect
from .forms import addShutter
from .models import ShutterDtls, OrderItems, Customer


def Shutter_Add(request):
    ShutterAddForm = addShutter()
    if request.method == 'POST':
        ShutterAddForm = addShutter(request.POST, request.FILES)
        if ShutterAddForm.is_valid():
            ShutterAddForm.save()
            return redirect('viewProduct')
    return render(request, 'admin/addShutter.html', {'ShutterAddForm': ShutterAddForm})


def viewProduct(request):
    products = ShutterDtls.objects.all()
    return render(request, 'admin/viewProduct.html', {'products': products})


def updateProduct(request, product_Id):
    upProduct = ShutterDtls.objects.get(product_Id=product_Id)
    ShutterAddForm = addShutter(instance=upProduct)
    if request.method == 'POST':
        ShutterAddForm = addShutter(request.POST, request.FILES, instance=upProduct)
        if ShutterAddForm.is_valid():
            ShutterAddForm.save()
            return redirect('viewProduct')
    return render(request, 'admin/ManUpdateProduct.html', {'ShutterAddForm': ShutterAddForm})


def remove(request, product_Id):
    products = ShutterDtls.objects.get(product_Id=product_Id)
    products.delete()
    return redirect('viewProduct')


def view_order(request):
    data = OrderItems.objects.all()
    return render(request, 'admin/view_order.html', {'data': data})


def updateStatus(request, product_Id):
    if request.method == 'POST':
        status = request.POST.get('status')
        print(status)
        OrderItems.objects.filter(product_Id=product_Id).update(Booking_status=status)
        return redirect('view_order')


