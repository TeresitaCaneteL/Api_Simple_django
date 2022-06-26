from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ApiCompany.models import Catalogo
import json

# Create your views here.
class CatalogoView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)


  def get(self, request, id=0):
    if(id>0):
      catalogo=list(Catalogo.objects.filter(id=id).values())
      if len(catalogo)>0:
        producto=catalogo[0]
        datos = {'mensaje': "Success",'producto':producto}
      else:
        datos = {'mensaje': "No hay datos"}
      return JsonResponse(datos)
    else:
      catalogo = list(Catalogo.objects.values())
      if len(catalogo)>0:
        datos = {'mensaje': "Success",'catalogo':catalogo}
      else:
        datos = {'mensaje': "No hay datos"}
      return JsonResponse(datos)

  def post(self, request):
    #print(request.body)
    jd=json.loads(request.body)
    #print(jd)
    Catalogo.objects.create(tipo=jd['tipo'],tallas=jd['tallas'],color=jd['color'],stock=jd['stock'])
    datos = {'mensaje': "Success"}
    return JsonResponse(datos)

  def put(self, request, id):
    jd=json.loads(request.body)
    catalogo=list(Catalogo.objects.filter(id=id).values())
    if len(catalogo)>0:
        producto=Catalogo.objects.get(id=id)
        producto.tipo=jd['tipo']
        producto.tallas=jd['tallas']
        producto.color=jd['color']
        producto.stock=jd['stock']
        producto.save()
        datos = {'mensaje': "Success"}
    else:
      datos = {'mensaje': "No hay datos"}
    return JsonResponse(datos)


  def delete(self, request, id):
    catalogo=list(Catalogo.objects.filter(id=id).values())
    if len(catalogo)>0:
      Catalogo.objects.filter(id=id).delete()
      datos = {'mensaje': "Success"}
    else:
      datos = {'mensaje': "No hay datos"}
    return JsonResponse(datos)
