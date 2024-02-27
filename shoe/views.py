from django.shortcuts import  get_object_or_404
from . import models, forms
from django.views import generic


class ShoeView(generic.ListView):
    template_name = 'shoe/shoe_list.html'
    context_object_name = 'shoes'
    model = models.Shoe

    def get_queryset(self):
        return self.model.objects.all()


class ShoeDetailView(generic.DetailView):
    template_name = 'shoe/shoe_detail.html'
    context_object_name = 'shoe_id'

    def get_object(self, **kwargs):
        shoe_id = self.kwargs.get('shoe_id')
        return get_object_or_404(models.Shoe, id=id)


class UpdateShoeView(generic.UpdateView):
    template_name = 'shoe/shoe_update.htm'
    form_class = forms.ShoesForm
    success_url = '/shoe_list/'
    def get_object(self, **kwargs):
        shoe_id = self.kwargs.get('shoe_id')
        return get_object_or_404(models.Shoe, id=shoe_id)
    def form_valid(self, form):
        return super(UpdateShoeView, self).form_valid(form=form)


class DeleteShoeView(generic.DeleteView):
    template_name = 'shoe/confirm_delete.html'
    success_url = '/shoe_list/'
    def get_object(self, **kwargs):
        shoe_id = self.kwargs.get('shoe_id')
        return get_object_or_404(models.Shoe, id=shoe_id)


class CreateShoeView(generic.CreateView):
    template_name = 'shoe/creat_shoes.html'
    form_class = forms.ShoesForm
    success_url = '/shoe_list/'
    def form_valid(self, form):
        return super(CreateShoeView, self).form_valid(form=form)


class CommentListView(generic.ListView):
    template_name = 'comment/shoe_list.html'
    model = models.CommentShoe
    context_object_name = 'comments'


class CommentCreateView(generic.CreateView):
    template_name = 'shoe/shoe_detail.html'
    form_class = forms.CommentCreateForm
    success_url = '/comments/'


class CommentUpdateView(generic.UpdateView):
    template_name = 'comment/update.html'
    form_class = forms.CommentCreateForm
    success_url = '/comments/'


class CommentDeleteView(generic.DeleteView):
    template_name = 'comment/delete.html'
    success_url = '/comments/'


# def creat_shoes_view(request):
#     if request.method == 'POST':
#         form = forms.ShoesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Добавлен в список кроссовок</h1 <a href="/shoe_list/">Все кроссовки</a>')
#     else:
#         form = forms.ShoesForm()
#     return render(request, 'shoe/creat_shoes.html', {'form': form})
# def delete_shoe_view(request, id):
#     shoe_id = get_object_or_404(models.Shoe, id=id)
#     shoe_id.delete()
#     return HttpResponse('<h1>Удален из списка кроссовок</h1 <a href="/shoe_list/">Все кроссовки</a>')
# def update_shoe_view(request, id):
#     shoe_id = get_object_or_404(models.Shoe, id=id)
#     if request.method == 'POST':
#         form = forms.ShoesForm(request.POST, instance=shoe_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Успешно поменяли данные</h1><a href="/shoe_list/">Все кроссовки</a>')
#     else:
#         form = forms.ShoesForm(instance=shoe_id)
#     return render(request, 'shoe/shoe_update.html', {'form': form, 'shoe_id': shoe_id})
# def shoe_shop_detail_view(request, id):
#     if request.method == 'GET':
#         shoes_id = get_object_or_404(models.Shoe, id=id)
#         context = {
#             "shoe_id": shoes_id,
#             'form': CommentCreateForm()
#         }
#         return render(request, 'shoe/shoe_detail.html', context)
#     elif request.method == 'POST':
#         form = CommentCreateForm(request.POST)
#         if form.is_valid():
#             models.CommentShoe.objects.create(**form.cleaned_data)
#             return redirect(f'/shoe_detail/{id}/')
#         context = {
#             'form': form,
#         }
#         return render(request, 'shoe/shoe_detail.html', context)
    # страница list
    # def shoe_view(request):
    #     if request.method == 'GET':
    #         shoes = models.Shoe.objects.all()
    #         return render(request, 'shoe/shoe_list.html',
    #                   {'shoes': shoes})
