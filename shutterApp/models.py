from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models her


class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_Customer = models.BooleanField(default=False)
    is_Manufacturers = models.BooleanField(default=False)
    is_Sales = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user")
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()


catagory = (
    ('Wood', 'Wood'),
    ('PVC', 'PVC'),
    ('Steel', 'Steel'),
)


class ShutterDtls(models.Model):
    product_Id = models.AutoField(unique=True, primary_key=True)
    product_Name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100,
                                choices=catagory)  # add catagry(e.g., wooden shutters, vinyl shutters, etc.)
    Material = models.CharField(max_length=100)  # ( wood, PVC, aluminum, etc)
    color = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity_Available = models.CharField(max_length=50)
    Manufacturer_Id = models.CharField(max_length=20)
    supplier_id = models.CharField(max_length=20)
    images = models.ImageField(upload_to='product_images/')


class ManufacturersDtlClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="manufact")
    Manufacturer_ID = models.CharField(max_length=10, validators=[RegexValidator(r'^\d+$', 'Only numbers are allowed')])
    Manufacturer_Name = models.CharField(max_length=50)
    Contact_Person = models.CharField(max_length=50)
    Contact_Email = models.EmailField(max_length=50)
    Contact_Phone = models.CharField(max_length=50)
    Company_Address = models.CharField(max_length=50)
    Company_Website = models.CharField(max_length=50)
    Profile_Description = models.CharField(max_length=50)


class Sales_TeamClass(models.Model):
    Sales_Team_ID = models.CharField(max_length=100)
    Sales_Representative_Name = models.CharField(max_length=100)
    Sales_Representative_Email = models.EmailField(max_length=100)
    Sales_Representative_Phone = models.CharField(max_length=10)
    Sales_Region = models.CharField(max_length=100)
    Sales_Manager = models.CharField(max_length=100)

statusCatagory = (
    ('Processing', 'Processing'),
    ('Shipping', 'Shipping'),
    ('Delivery', 'Delivery'),
)
class OrderItems(models.Model):
    user = models.IntegerField()
    Buyer_Name = models.CharField(max_length=100,null=True)
    Date_of_supply = models.DateField()
    Quantity = models.IntegerField()
    Product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_Id = models.CharField(max_length=100)
    Product_Name = models.CharField(max_length=255)
    Booking_status = models.CharField(max_length=100,choices=statusCatagory,default="Processing")




class Enquiry(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)


class feedBack(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="UserFeedBack")
    Date = models.DateField(auto_now=True)
    feedBack = models.CharField(max_length=20000)

