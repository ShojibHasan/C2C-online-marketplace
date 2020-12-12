from django.db.models import Count
from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Category, Product


def index(request,category_slug=None,):
    category = None
    productlist = Product.objects.all()
    category_list = Category.objects.annotate(total_products=Count('product'))
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        productlist = productlist.filter(category=category)
    context = {
        'product_list': productlist,
        'category_list': category_list,
        'category': category,
    }
    return render(request,'product/index.html',context)


def category(request):
    return render(request,'product/category.html')



def post_ads(request):
    return render(request,'product/post_ads.html')