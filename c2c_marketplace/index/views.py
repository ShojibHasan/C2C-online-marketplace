from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from product.models import Category, Product
from index.forms import ProductForm

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


@login_required
def post_ads(request):
    category_list = Category.objects.all()
    # condition_form = forms.ConditionListForm()
    #condition = Product.CONDITION_TYPE.all()

    coditions = ProductForm()

    context ={
        # 'condition_form':condition_form,
        'category_list':category_list,
        'coditions': coditions
    }

    if request.method == "POST":
        get_method = request.POST.copy()
        category = get_method.get('category') or None
        condition = get_method.get('conditions') or None
        brand = get_method.get('brand') or None
        name = get_method.get('name') or None
        description = get_method.get('description') or None
        image = get_method.get('image') or None
    return render(request,'product/post_ads.html',context)