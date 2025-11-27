from django.shortcuts import render, get_object_or_404
from .models import Package, Category, Destination

def package_list(request):
    packages = Package.objects.all()
    destinations = Destination.objects.all()
    categories = Category.objects.all()
    
    dest_filter = request.GET.get('destination')
    cat_filter = request.GET.get('category')
    
    if dest_filter:
        packages = packages.filter(destination__id=dest_filter)
    if cat_filter:
        packages = packages.filter(category__id=cat_filter)
        
    context = {
        'packages': packages,
        'destinations': destinations,
        'categories': categories,
    }
    return render(request, 'packages/list.html', context)

def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    return render(request, 'packages/detail.html', {'package': package})
