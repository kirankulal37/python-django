from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        if not name or not price:
            return render(request, "products/create.html", {
                "error": "All fields required"
            })

        Product.objects.create(
            name=name,
            price=float(price)
        )

        return redirect("/")

    return render(request, "products/create.html")
