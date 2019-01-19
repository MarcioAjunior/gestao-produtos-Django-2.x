from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdForm


@login_required
def prod_list(request):
    prod = Produto.objects.all()
    return render(request, 'index_produto.html', {'prod': prod})

@login_required
def prod_new(request):
    form = ProdForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'prod_form.html', {'form': form})

@login_required
def update_pro(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'prod_form.html', {'form': form})

@login_required
def delete_p(request, id):
    prod = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        prod.delete()
        return redirect('product_list')

    return render(request, 'prod_delete.html', {'prod': prod})