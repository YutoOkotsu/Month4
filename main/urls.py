from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cloth.views import ClothsListView
from cloth.views import ManListView
from cloth.views import WomanListView
from cloth.views import KidListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('shoe.urls')),
    path('', include('parser_app.urls')),
    path('', include('users.urls')),
    path('all_cloth/', ClothsListView.as_view()),
    path('man_cloth/', ManListView.as_view()),
    path('woman_cloth/', WomanListView.as_view()),
    path('kid_cloth/', KidListView.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
