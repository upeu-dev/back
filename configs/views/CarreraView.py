from rest_framework import serializers, viewsets
from configs.models.JerarquiaAcad import JerarquiaAcad
from configs.models.Carrera import Carrera

# Serializers define the API representation.


class CarreraSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Carrera
        fields = ('url', 'nombre', 'abrev', 'codigo', 'jerarquia_acad')

# ViewSets define the view behavior.


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
