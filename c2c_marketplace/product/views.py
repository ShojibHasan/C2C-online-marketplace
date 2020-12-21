from django.shortcuts import render

from index.forms import ProductForm
from .models import *
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404


# Create your views here.

def productlist(request, category_slug=None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query) |
            Q(brand__category_name__icontains=search_query)
        )

    paginator = Paginator(productlist, 2)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {
        'product_list': productlist,
        'category_list': categorylist,
        'category': category,
    }
    return render(request, 'product/product_list.html', context)


def productdetail(request, product_slug):
    productdetail = get_object_or_404(Product,slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)

    context = {
        'product_detail': productdetail,
        'product_images': productimages
    }
    return render(request, 'product/product_details.html', context)

