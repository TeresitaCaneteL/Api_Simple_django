from django.urls import path
from . import views
from ApiCompany.views import CatalogoView

app_name="ApiCompany"

urlpatterns=[
  path('catalogo/', CatalogoView.as_view(), name="catalogo"),
  path('catalogo/<int:id>', CatalogoView.as_view(), name="catalogo_process"),



]