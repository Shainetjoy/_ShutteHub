from django.contrib.auth.forms import UserCreationForm
from django import forms
from shutterApp.models import User, Customer, ShutterDtls, ManufacturersDtlClass, Sales_TeamClass, OrderItems, Enquiry, \
    feedBack


class DateInput(forms.DateInput):
    input_type = 'date'

class UserRgistration(UserCreationForm):
    username = forms.CharField()
    password1 =forms.CharField(label='password',widget=forms.PasswordInput)
    password2 =forms.CharField(label='password',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username','password1','password2')



class CustomerREgistration(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("user",)


class addShutter(forms.ModelForm):
    class Meta:
        model = ShutterDtls
        fields = '__all__'


class ManufacturersDtlForms(forms.ModelForm):
    class Meta:
        model = ManufacturersDtlClass
        exclude = ('user',)


class Sales_TeamFormClass(forms.ModelForm):
    class Meta:
        model = Sales_TeamClass
        fields = '__all__'


class Order(forms.ModelForm):
    Date_of_supply = forms.DateField(widget=DateInput)
    class Meta:
        model = OrderItems
        exclude = ('user','Product_price','product_Id','Product_Name','Booking_status','Buyer_Name')


class UpdateStatus(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = '__all__'


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'


class feedBackForm(forms.ModelForm):
    class Meta:
        model = feedBack
        exclude = ("user","Date")