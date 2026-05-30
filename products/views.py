from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Product, Cart, CartItem, Order, OrderItem
from django.db.models import Sum

def index(request):
    return render(request, 'products/index.html')

def is_owner(user):

    return (
        user.is_authenticated and
        user.profile.role in [
            'owner',
            'side_owner'
        ]
    )

@user_passes_test(is_owner)
def owner_dashboard(request):

    products = Product.objects.filter(
        owner=request.user
    )

    orders = Order.objects.all().order_by('-created_at')

    total_orders = orders.count()

    revenue = orders.aggregate(
        total=Sum('total_amount')
    )['total'] or 0

    return render(request, 'products/owner_dashboard.html', {
        'products': products,
        'orders': orders,
        'total_orders': total_orders,
        'revenue': revenue
    })


def shop(request):
    products = Product.objects.all()
    return render(request, 'products/shop.html', {'products': products})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    Cart.objects.create(
        user=request.user,
        product=product,
        quantity=1
    )

    return redirect('shop')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    item = Cart.objects.get(id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))

        item = Cart.objects.get(id=item_id, user=request.user)
        item.quantity = quantity
        item.save()

    return redirect('cart')

@user_passes_test(is_owner)
def add_product(request):

    if request.method == "POST":

        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        category = request.POST['category']

        image = request.FILES['image']

        Product.objects.create(

            owner=request.user,

            name=name,
            description=description,
            price=price,
            quantity=quantity,
            category=category,

            image=image
        )

        return redirect('owner_dashboard')

    return render(
        request,
        'products/add_product.html'
    )
@login_required
def checkout(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        mpesa_code = request.POST.get("mpesa_code")

        # Create order
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            total_amount=total,
            mpesa_code=mpesa_code
        )

        # Save order items
        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear cart
        cart_items.delete()

        return redirect('shop')

    return render(request, 'products/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(request, 'products/orders.html', {
        'orders': orders
    })


@user_passes_test(is_owner)
def owner_orders(request):

    orders = Order.objects.all().order_by('-id')

    return render(
        request,
        'products/owner_orders.html',
        {
            'orders': orders
        }
    )