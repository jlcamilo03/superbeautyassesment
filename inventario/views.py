from rest_framework.views import APIView
from rest_framework.response import Response
from inventario.models import Equipo
from django.forms.models import model_to_dict
from inventario.serializer import EquipoSerializer

class ListaEquipo(APIView):
     
    
    def get(self, request):
               
        queryset = Equipo.objects.all()
        serializer = EquipoSerializer(queryset, many=True)
        return Response(serializer.data)
