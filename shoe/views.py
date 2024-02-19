from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


def delete_shoe_view(request, id):
    shoe_id = get_object_or_404(models.Shoe, id=id)
    shoe_id.delete()
    return HttpResponse('<h1>Удален из списка кроссовок</h1 <a href="/">Все кроссовки</a>')


def update_shoe_view(request, id):
    shoe_id = get_object_or_404(models.Shoe, id=id)
    if request.method == 'POST':
        form = forms.ShoesForm(request.POST, instance=shoe_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно поменяли данные</h1><a href="/">Все кроссовки</a>')
    else:
        form = forms.ShoesForm(instance=shoe_id)
    return render(request, 'shoe/update.html', {'form': form, 'shoe_id': shoe_id})


def creat_shoe_view(request):
    if request.method == 'POST':
        form = forms.ShoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Добавлен в список кроссовок</h1 <a href="/">Все кроссовки</a>')
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

