from django.urls import path
from . import views

urlpatterns = [

    # Home page
    path('', views.home, name='home'),

    # Login page
    path('login/', views.login, name='login'),

    # Register page
    path('register/', views.register, name='register'),

    # About page
    path('about/', views.about, name='about'),

    # Logout
    path('logout/', views.logout_view, name='logout'),

    path('explore/', views.explore, name='explore'),

    path('user_home/', views.user_home, name='user_home'),

   path('place_order/', views.place_order, name='place_order'),

   path(  'order_history/',   views.order_history,  name='order_history'),

   path(    'staff_login/',    views.staff_login,    name='staff_login'),

   path(    'staff_home/',    views.staff_home,    name='staff_home'),

path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),

path('update-payment-status/<int:order_id>/', views.update_payment_status, name='update_payment_status'),



]