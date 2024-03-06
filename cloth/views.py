from django.views import generic
from . import models


class ClothsListView(generic.ListView):
    template_name = 'clothes/all_cloth.html'
    context_object_name = 'all_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class ManListView(generic.ListView):
    template_name = 'clothes/man_cloth.html'
    context_object_name = 'man_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='мужская').order_by('-id')


class WomanListView(generic.ListView):
    template_name = 'clothes/woman_cloth.html'
    context_object_name = 'woman_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='женская').order_by('-id')


class KidListView(generic.ListView):
    template_name = 'clothes/kid_cloth.html'
    context_object_name = 'kid_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детская').order_by('-id')

