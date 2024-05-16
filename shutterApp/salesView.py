from django.shortcuts import render

from shutterApp.models import Customer, OrderItems, Enquiry, ShutterDtls


def SalesViewCustomer(request):
    SalesUserView = Customer.objects.all()
    for  i in SalesUserView:
        print(i.user.id)
        orderData = OrderItems.objects.filter(user = i.user.id)
        print(orderData)
    return render(request,'Sales/UserViewsOfSales.html',{"SalesUserView":SalesUserView,"orderData":orderData})




def ViewLeeds(request):
    leeds = Enquiry.objects.all()
    return render(request,'Sales/Leed.html',{"leeds":leeds})


def report(request):
    Report = OrderItems.objects.all
    productReport = ShutterDtls.objects.all()
    return render(request, 'Sales/Report.html',{"Report":Report,"productReport":productReport})