from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django_filters import rest_framework as filters

from .serializers import ContactSerializer

from .models import Contact


# List API View
class ListContactsApiView(generics.ListAPIView):

  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  filter_backends = (filters.DjangoFilterBackend, )
  filterset_fields = ('name', 'email')


# Create API View
class CreateContactsApiView(generics.CreateAPIView):

  queryset = Contact.objects.all()
  serializer_class = ContactSerializer


# List Template View
class ListContactsTemplateView(ListView):

  template_name = 'dashboard.html'
  paginate_by = 2
  model = Contact
  context_object_name = 'contacts'

  def get_queryset(self):

    query = self.request.GET.get('q')
    if query:
      return Contact.objects.filter(name__icontains=query)
    else:
      return Contact.objects.all()

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)


# Create Template View
class CreateContactsTemplateView(APIView):
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'contacts.html'

  def get(self, request):
    return Response({})

  def post(self, request):
    serializer = ContactSerializer(data=request.data)
    if not serializer.is_valid():
      return render(request, 'contacts.html', {"error": True})
    else:
      serializer.save()
      return render(request, 'contacts.html', {"success": True})
