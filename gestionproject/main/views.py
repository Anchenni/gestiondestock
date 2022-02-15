from django.shortcuts import render, redirect
from .models import Categorie,Product
from .forms import ProductForm,CategorieForm
from django.db.models import Count
from django.core.paginator import Paginator
from .filters import ProductFilter

def home(response):
    return render(response, "main/index.html", {})

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request,'main/upload_product.html', {'form': form})


def product_list(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Product.objects.annotate(total_comments=Count('model')).filter(model__icontains=q).order_by('-id')
        lenquest = len(quests)
    else:
        quests=Product.objects.annotate(total_comments=Count('model')).all().order_by('-id')
        print('2',len(quests))
        lenquest = len(quests)
        
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'main/product_list.html',{'quests':quests, 'lenquest':lenquest,})

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    # print('FACTURE:', facture)
    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {'form':form}
    return render(request, 'main/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    context = {'product':product}
    return render(request, 'main/delete.html', context)  

def search_list(request):    
    products = Product.objects.all()
    order_count = products.count()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    lenquest = len(products)
    context = {'products':products,'order_count':order_count,
    'myFilter':myFilter,'lenquest':lenquest,}

    return render(request, 'main/search.html', context)