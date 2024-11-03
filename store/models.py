from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import Q

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone='', password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Ensure 'phone' field is empty for superusers
        extra_fields.setdefault('phone', '')

        return self.create_user(email, username, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)  # Allow blank for non-superusers
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
class Photographer(models.Model):
    photographer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    description = models.TextField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    # Other fields as necessary

class PhotographerImage(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photographer_images/')

class Stylist(models.Model):
    stylist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StylistImage(models.Model):
    stylist = models.ForeignKey(Stylist, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stylist_images/')

    def __str__(self):
        return f"Image for {self.stylist.name}"

class Religion(models.Model):
    id = models.AutoField(primary_key=True)
    religion = models.CharField(max_length=100)

    def __str__(self):
        return self.religion
    

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    
    event_type_name = models.CharField(max_length=100)
    event_description = models.TextField()

    def __str__(self):
        return self.event_type_name

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return f"Image for {self.event.event_type_name}"

class MainCourse(models.Model):
    MAIN_COURSE_CHOICES = [
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non-Vegetarian'),
    ]

    main_course_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='main_courses')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=MAIN_COURSE_CHOICES, default='veg')

    def __str__(self):
        return self.name

class MainCourseImage(models.Model):
    main_course = models.ForeignKey(MainCourse, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main_courses/')

class Dessert(models.Model):
    dessert_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='desserts')
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField('DessertImage', related_name='desserts')

    def __str__(self):
        return self.name

class DessertImage(models.Model):
    image = models.ImageField(upload_to='desserts/')
    
class Starter(models.Model):
    VEG = 'Veg'
    NON_VEG = 'Non-Veg'
    STARTER_TYPE_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]

    starter_id = models.AutoField(primary_key=True)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='starters',null=True, blank=True)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    starter_type = models.CharField(
        max_length=10,
        choices=STARTER_TYPE_CHOICES,
        default=VEG,
    )
    def __str__(self):
        return self.name

class StarterImage(models.Model):
    starter = models.ForeignKey(Starter, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='starters/')

    def __str__(self):
        return f"Image for {self.starter.name}"

class BookedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=50)
    package_name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.package_name}"

class WeddingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    bride_name = models.CharField(max_length=255)
    groom_name = models.CharField(max_length=255)
    guest_count = models.PositiveIntegerField()
    wedding_dates = models.CharField(max_length=255)  # Store as a comma-separated string
    venue_address = models.TextField()
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # New field for total amount
    razorpay_payment_id = models.CharField(max_length=255, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wedding of {self.bride_name} and {self.groom_name}"

class Dress(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class DressImage(models.Model):
    dress = models.ForeignKey(Dress, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dresses/')

    def __str__(self):
        return f"{self.dress.name} - Image"


# class UserImage(models.Model):
#     user_image = models.ImageField(upload_to='user_images/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# class DressImage(models.Model):
#     dress_name = models.CharField(max_length=255, default='Default Dress Name')  # Example of dress_name
#     dress_image = models.ImageField(upload_to='dress_images/', default='path/to/default/image.jpg')  # Set a default image path
#     uploaded_at = models.DateTimeField(auto_now_add=True)


class FoodImage(models.Model):
    image = models.ImageField(upload_to='food_images/')
    predicted_food = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.predicted_food or "Unknown Food"

from django.db import models

class UserPreferences(models.Model):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    VENUE_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('destination', 'Destination')
    ]
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter')
    ]
    
    budget = models.CharField(max_length=10, choices=BUDGET_CHOICES)
    guest_count = models.PositiveIntegerField()
    venue_type = models.CharField(max_length=20, choices=VENUE_CHOICES)
    preferred_colors = models.CharField(max_length=100)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    
    def __str__(self):
        return f"{self.budget} budget wedding in {self.season}"

from django import forms
from .models import UserPreferences

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['budget', 'guest_count', 'venue_type', 'preferred_colors', 'season']
        widgets = {
            'budget': forms.Select(attrs={'class': 'form-control'}),
            'guest_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'venue_type': forms.Select(attrs={'class': 'form-control'}),
            'preferred_colors': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
        }
        
class Feedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User model for customers
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.customer.username}"
    
class Complaint(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User model for customers
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint from {self.customer.username}"