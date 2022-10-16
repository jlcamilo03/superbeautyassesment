from rest_framework import  serializers
from inventario.models import Equipo

# Serializers define the API representation.
class EquipoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Equipo
        fields = "__all__"