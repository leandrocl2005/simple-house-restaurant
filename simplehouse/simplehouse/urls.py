from contacts.views import CreateContactsApiView, CreateContactsTemplateView, ListContactsApiView, ListContactsTemplateView
from food.views import HomeFood, ListCategories, ListFoods
from django.contrib import admin
from django.urls import path, include

# handle static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # api endpoints
    path('api/categories/', ListCategories.as_view()),
    path('api/foods/', ListFoods.as_view()),
    path('api/contacts/', ListContactsApiView.as_view()),
    path('api/contacts/create/', CreateContactsApiView.as_view()),
    # templates endpoints
    path('', HomeFood.as_view()),
    path('dashboard/', ListContactsTemplateView.as_view()),
    path('contatos/', CreateContactsTemplateView.as_view()),
    # accounts
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
