from django.shortcuts import render, get_object_or_404
from . import models


def shoe_view(request):
    if request.method == 'GET':
        shoes = models.Shoe.objects.all()
        return render(request, 'shoe/shoe_list.html', {'shoes': shoes})
# Create your views here.


def shoe_shop_detail_view(request, id):
    shoes_id = get_object_or_404(models.Shoe, id=id)
    return render(request, 'shoe/shoe_detail.html',
                  context={'shoe_id': shoes_id})

