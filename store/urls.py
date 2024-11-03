from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import (
    index, register, login_view, logout_view, profile_view,admin_dashboard_view,
    view_customers, view_packages, add_package, edit_package, delete_package, 
    add_photographer, photographer_list, edit_photographer, delete_photographer, 
    add_stylist, stylist_list, edit_stylist, delete_stylist, 
    view_religions, add_religion, edit_religion, delete_religion, password_reset_form, password_reset_confirm,
    customer_photographer_list,add_event, event_list, edit_event, delete_event,
    add_starter,view_starters,edit_starter,delete_starter,
    add_main_course, view_main_courses, edit_main_course, delete_main_course
)

urlpatterns = [
    path('', index, name='index'),
    
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('profile/', profile_view, name='profile_view'),
    path('admin-dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('view-customers/', view_customers, name='view_customers'),
    
    path('view-packages/', view_packages, name='view_packages'),
    path('add-package/', add_package, name='add_package'),
    path('edit-package/<int:package_id>/', edit_package, name='edit_package'),
    path('delete-package/<int:package_id>/', delete_package, name='delete_package'),
    
    # path('add-occasion/', add_occasion, name='add_occasion'),
    # path('occasions/', view_occasions, name='view_occasions'),
    # path('edit-occasion/<int:occasion_id>/', edit_occasion, name='edit_occasion'),
    # path('delete-occasion/<int:occasion_id>/', delete_occasion, name='delete_occasion'),
    
   
    path('add-photographer/', add_photographer, name='add_photographer'),
    path('photographers/', photographer_list, name='photographer_list'),
    path('photographers/edit/<int:photographer_id>/', edit_photographer, name='edit_photographer'),
    path('photographers/delete/<int:photographer_id>/', delete_photographer, name='delete_photographer'),
    
    path('add-stylist/', add_stylist, name='add_stylist'),
    path('stylists/', stylist_list, name='stylist_list'),
    path('stylists/edit/<int:stylist_id>/', edit_stylist, name='edit_stylist'),
    path('stylists/delete/<int:stylist_id>/', delete_stylist, name='delete_stylist'),
    
    path('religions/', view_religions, name='view_religions'),
    path('religions/add/', add_religion, name='add_religion'),
    path('religions/edit/<int:id>/', edit_religion, name='edit_religion'),
    path('religions/delete/<int:id>/', delete_religion, name='delete_religion'),
    
    path('password-reset/', password_reset_form, name='password_reset_form'),
    path('reset/<uuid:token>/', password_reset_confirm, name='password_reset_confirm'),
    
    path('customer_photographer_list/', customer_photographer_list, name='customer_photographer_list'),
    
    path('add_event/', add_event, name='add_event'),
    path('events/', event_list, name='event_list'),
    path('edit_event/<int:event_id>/', edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    
    path('add/', add_starter, name='add_starter'),
    path('starters', view_starters, name='starter_list'),
    path('edit/<int:starter_id>/', edit_starter, name='edit_starter'),
    path('delete/<int:starter_id>/', delete_starter, name='delete_starter'),

    path('main_course/add/', add_main_course, name='add_main_course'),
    path('main_course/', view_main_courses, name='view_main_courses'),
    path('main_course/edit/<int:pk>/', edit_main_course, name='edit_main_course'),
    path('main_course/delete/<int:pk>/', delete_main_course, name='delete_main_course'),
    
    path('desserts/add/', views.add_dessert, name='add_dessert'),
    path('desserts/', views.view_desserts, name='view_desserts'),
    path('desserts/edit/<int:pk>/', views.edit_dessert, name='edit_dessert'),
    path('desserts/delete/<int:pk>/', views.delete_dessert, name='delete_dessert'),
    
    path('package/', views.package_view, name='package_view'),
    # path('package/<int:package_id>/details/', views.package_details, name='package_details'),
    
    
    path('caters/', views.cater_list, name='cater_list'),
    path('caters/<int:package_id>/', views.caters_customer, name='caters_customer'),


    # path('add-to-order/<str:item_type>/<int:item_id>/', views.add_to_order, name='add_to_order'),
    # path('view-order/', views.view_order, name='view_order'),
    # path('cart/', views.cart_view, name='cart_view'),

    # path('add_to_cart/stylist/<int:stylist_id>/', views.add_to_cart, name='add_stylist_to_cart'),
    # path('add_to_cart/photographer/<int:photographer_id>/', views.add_to_cart, name='add_photographer_to_cart'),
    # path('add_to_cart/package/<int:package_id>/', views.add_to_cart, name='add_package_to_cart'),
    path('package/<int:package_id>/', views.package_details, name='package_details'),

    # path('photographer/<int:item_id>/', views.photographer_details, name='photographer_detail'),
    path('package/<int:package_id>/photographer/', views.photographer_details, name='photographer_details'),
    path('photographer/<int:photographer_id>/', views.photographer_detail, name='photographer_detail'),
    
    path('package/<int:package_id>/stylist/', views.stylist_package, name='stylist_details'),
    path('stylist/<int:stylist_id>/', views.stylist_customer, name='stylist_detail'),
    
    path('package/<int:package_id>/starter/', views.starter_details, name='starter_details'),
    path('starter/<int:item_id>/', views.starter_detail, name='starter_detail'),
    
    path('package/<int:package_id>/main-course/', views.main_course_details, name='main_course_details'),
    path('main-course/<int:item_id>/', views.main_course_detail, name='main_course_detail'),
       
    path('package/<int:package_id>/dessert/', views.dessert_details, name='dessert_details'),
    path('dessert/<int:item_id>/', views.dessert_detail, name='dessert_detail'), 
    
    path('event/<int:item_id>/', views.event_customer, name='event_customer'),
    path('package/<int:package_id>/event/', views.event_package, name='event_details'), 
    
    path('booking/', views.booking_view, name='booking'),
    path('add-to-booking/', views.add_to_booking, name='add_to_booking'),
    path('checkout/', views.checkout_view, name='checkout'), 
    
    # path('wedding-info/',views.wedding_info_view, name='wedding_info'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    
    path('booking/', views.booking_view, name='booking_page'),
    
  
    
    path('upload_dress/', views.upload_dress, name='upload_dress'),
    path('dresses/', views.dress_list, name='dress_list'),
    path('try_on/<int:dress_id>/', views.virtual_try_on, name='virtual_try_on'),
    
    path('photographer/', views.photographer, name='photographers'),
    path('stylist/', views.stylist, name='stylists'),
    path('event/', views.event, name='events'),
    
   
   
    path('export_weddinginfo/', views.export_weddinginfo_csv, name='export_weddinginfo'),  # Add this line
    path('export_packages/', views.export_package_csv, name='export_packages'),  # Add this path
    # path('predict/', views.predict_budget, name='predict_budget'),  # Add this line

    path('order-details/', views.order_details_view, name='order_details'),  # Add this line

    # path('stylist/<int:stylist_id>/', views.stylist_detail_view, name='stylist_detail'),
    path('event/<int:event_id>/', views.event_detail_view, name='event_detail'),
     path('photographer/<int:photographer_id>/', views.photographer_detail_view, name='photographer_detail'),
    # path('preferences/', views.preferences_view, name='preferences_view'),

    path('checkouts/', views.checkout_details_view, name='checkout_details'),
    
    path('customer-page/', views.customer_page, name='customer_page'),
    
    path('feedback/', views.submit_emoji_feedback, name='submit_feedback'),
    path('thank-you/', views.feedback_thankyou_view, name='feedback_thankyou'),
    
    path('complaint/', views.complaint, name='submit_complaint'),
    path('complaints_thankyou/', views.complaint_view, name='complaints'),
    
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('complaint_list/', views.complaint_list, name='complaint_list'),
    
    
    path('stylist/<int:stylist_id>/', views.stylist_index_view, name='stylist_index'),
    
     path('check-existing-name/', views.check_existing_name, name='check_existing_name'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
