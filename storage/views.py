from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Asset, Employee
from .forms import AssetForm
from .filters import AssetFilter


@login_required(login_url='login')
def asset_list(request):
    assets = Asset.objects.all().exclude(status='deleted').order_by('-added_date')
    form = AssetForm(request.POST or None, request.FILES or None)
    asset_filter = AssetFilter(request.GET, queryset=assets)
    assets = asset_filter.qs

    if form.is_valid():
        asset = form.save()
        return redirect('asset_list')

    context = {
        'assets': assets,
        'form': form,
        'asset_filter': asset_filter
    }
    # context['form'] = form
    # context['asset_filter'] = asset_filter
    return render(request, 'storage/asset_list.html', context)


def asset_detail(request, pk):
    asset = Asset.objects.get(pk=pk)
    return render(request, 'storage/asset_detail.html', {'asset': asset})


@login_required(login_url='login')
def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    form = AssetForm(request.POST or None, instance=asset)
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES, instance=asset)

    if form.is_valid():
        asset = form.save()
        return redirect('asset_detail', pk=asset.pk)

    context = {
        'form': form
    }

    return render(request, 'storage/asset_list.html', context)


@login_required(login_url='login')
def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'storage/asset_delete.html', {'asset': asset})


# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, 'myapp/employee_list.html', {'employees': employees})


# def employee_detail(request, pk):
#     employee = Employee.objects.get(pk=pk)
#     return render(request, 'myapp/employee_detail.html', {'employee': employee})
