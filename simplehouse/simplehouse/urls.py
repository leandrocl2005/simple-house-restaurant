from food.views import HomeFood, ListCategories, ListFoods
from django.contrib import admin
from django.urls import path

# handle static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', ListCategories.as_view()),
    path('api/foods/', ListFoods.as_view()),
    path('', HomeFood.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
