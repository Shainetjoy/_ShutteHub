from django.shortcuts import render, redirect
from django.contrib import messages
from shutterApp.forms import Order, feedBackForm
from shutterApp.models import ShutterDtls, OrderItems, Customer, User


def ProductCatalog(request):
    products = ShutterDtls.objects.all()
    return render(request, 'User/Product_Catalog.html', {'products': products})


# def BookProduct(request,product_Id ):
#     item = ShutterDtls.objects.get(product_Id=product_Id)
#     Product_Name = item.product_Name
#     product_Id = item.product_Id
#     description = item.description
#     Product_price = item.price
#     BookingItems.objects.create(product_Id = product_Id, Product_Name = Product_Name,Product_price = Product_price,description=description)
#
#     return render(request,'User/Booking.html',
#                   {"item":item})

def orderitems(request, product_Id):
    u = request.user.id
    Pro = ShutterDtls.objects.get(product_Id=product_Id)
    item_name = Pro.product_Name
    item_price = Pro.price
    customer = Customer.objects.filter(user__id= u).values()
    customer_name = customer[0]['Name']
    form = Order()
    if request.method == 'POST':
        item = ShutterDtls.objects.get(product_Id=product_Id)
        Product_Name = item.product_Name
        product_Id = item.product_Id
        Product_price = item.price
        Product_qty = item.quantity_Available
        form = Order(request.POST)
        if form.is_valid():
            qty = request.POST.get('Quantity')
            if qty <= Product_qty:
                print("88888888")
                new_qty = Product_qty - qty
                ShutterDtls.objects.filter(product_Id=product_Id).update(quantity_Available=new_qty)
                data = form.save(commit=False)
                data.user = u
                data.Buyer_Name= customer_name
                data.Product_price = Product_price
                data.product_Id = product_Id
                data.Product_Name = Product_Name
                data.save()
                return redirect('feedback')
            else:
                messages.error(request, 'Out Of Stock')
    return render(request,'User/orderitems.html', {'form': form,'item_name':item_name,'item_price':item_price})



def viewOrders(request):
    orderDtlz = OrderItems.objects.filter(user = request.user.id)

    return render(request,'User/viewOrder.html',{'orderDtlz':orderDtlz})


def feedback(request):
    u = request.user.id
    feedbackF = feedBackForm()
    if request.method == 'POST':
        feedbackF = feedBackForm(request.POST)
        if feedbackF.is_valid():
            user_instance = User.objects.get(id=request.user.id)
            data = feedbackF.save(commit=False)
            data.user = user_instance
            data.save()
            return redirect('shutterUserIndex')
    return render(request,'User/feed.html',{"feedbackF":feedbackF})