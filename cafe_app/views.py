from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import Order, Staff , Product
from django.views.decorators.http import require_POST


# Home page
def home(request):
    return render(request, 'home.html')


# About page
def about(request):
    return render(request, 'about.html')


# Explore Menu page
def explore(request):
    return render(request, 'explore.html')


def user_home(request):

    coffees = Product.objects.filter(category="Coffee")
    cakes = Product.objects.filter(category="Cake")
    donuts = Product.objects.filter(category="Donut")
    drinks = Product.objects.filter(category="Drinks")
    snacks = Product.objects.filter(category="Snack")

    return render(
        request,
        'user_home.html',
        {
            'coffees': coffees,
            'cakes': cakes,
            'donuts': donuts,
            'drinks': drinks,
            'snacks': snacks,
        }
    )

# Register page
def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully. Now Login!")
        return redirect('login')

    return render(request, 'register.html')


# Login page
def login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('home')


# =========================
# PLACE ORDER (UPDATED LOGIC)
# =========================
def place_order(request):

    item = request.GET.get('item')

    if request.method == "POST":

        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        delivery_option = request.POST['delivery_option']
        payment_method = request.POST['payment_method']

        pickup_time = request.POST.get('pickup_time') or None
        pickup_period = request.POST.get('pickup_period') or None
        address = request.POST.get('address') or None


        if payment_method in ["UPI", "Google Pay"] and delivery_option == "Pickup":
            payment_status = "Paid"
        else:
            payment_status = "Pending"

        Order.objects.create(
            user=request.user,
            item_name=item_name,
            quantity=quantity,
            delivery_option=delivery_option,
            address=address,
            pickup_time=pickup_time,
            pickup_period=pickup_period,
            payment_method=payment_method,
            payment_status=payment_status
        )

        messages.success(request, "🎉 Your order has been placed successfully!")

        return redirect('user_home')



    return render(request, 'order.html', {'item': item})


# Order History
def order_history(request):

    orders = Order.objects.filter(user=request.user).order_by('-id')

    return render(request, 'order_history.html', {'orders': orders})


# Staff Login
def staff_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        try:
            staff = Staff.objects.get(username=username, password=password)
            request.session['staff_id'] = staff.id
            return redirect('staff_home')

        except Staff.DoesNotExist:
            messages.error(request, "Invalid Staff Username or Password")
            return redirect('staff_login')

    return render(request, 'staff_login.html')


# Staff Home
def staff_home(request):

    orders = Order.objects.all().order_by('-id')

    return render(request, 'staff_home.html', {'orders': orders})

@require_POST
def update_order_status(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    new_status = request.POST.get("status")

    order.status = new_status
    order.save()

    return redirect('staff_home')

@require_POST
def update_payment_status(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    new_payment_status = request.POST.get('payment_status')

    order.payment_status = new_payment_status
    order.save()

    return redirect('staff_home')


