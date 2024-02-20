from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse

from .forms import CommentCreateForm


def delete_shoe_view(request, id):
    shoe_id = get_object_or_404(models.Shoe, id=id)
    shoe_id.delete()
    return HttpResponse('<h1>Удален из списка кроссовок</h1 <a href="/shoe_list/">Все кроссовки</a>')




def update_shoe_view(request, id):
    shoe_id = get_object_or_404(models.Shoe, id=id)
    if request.method == 'POST':
        form = forms.ShoesForm(request.POST, instance=shoe_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно поменяли данные</h1><a href="/shoe_list/">Все кроссовки</a>')
    else:
        form = forms.ShoesForm(instance=shoe_id)
    return render(request, 'shoe/shoe_update.html', {'form': form, 'shoe_id': shoe_id})


def creat_shoe_view(request):
    if request.method == 'POST':
        form = forms.ShoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Добавлен в список кроссовок</h1 <a href="/shoe_list/">Все кроссовки</a>')
    else:
        form = forms.ShoesForm()
    return render(request, 'shoe/shoe_form.html', {'form': form})


def shoe_view(request):
    if request.method == 'GET':
        shoes = models.Shoe.objects.all()
        return render(request, 'shoe/shoe_list.html', {'shoes': shoes})
# Create your views here.


def shoe_shop_detail_view(request, id):
    shoes_id = get_object_or_404(models.Shoe, id=id)
    return render(request, 'shoe/shoe_detail.html',
                  context={'shoe_id': shoes_id})


def shoe_shop_detail_view(request, id):
    if request.method == 'GET':
        shoes_id = get_object_or_404(models.Shoe, id=id)
        context = {
            "shoe_id": shoes_id,
            'form': CommentCreateForm()
        }
        return render(request, 'shoe/shoe_detail.html', context)
    elif request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            models.CommentShoe.objects.create(id=id, **form.cleaned_data)
            return redirect(f'/shoe_detail/{id}/')
        context = {
            'form': form,
        }
        return render(request, 'shoe/shoe_detail.html', context)
