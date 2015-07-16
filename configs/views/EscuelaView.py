from rest_framework import serializers, viewsets
from configs.models.JerarquiaAcad import JerarquiaAcad
from configs.models.Escuela import Escuela

# Serializers define the API representation.


class EscuelaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Escuela
        fields = ('url', 'nombre', 'abrev', 'codigo', 'jerarquia_acad')

# ViewSets define the view behavior.


class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer
