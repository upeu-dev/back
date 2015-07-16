from rest_framework import serializers, viewsets
from configs.models.JerarquiaAcad import JerarquiaAcad
from configs.models.Facultad import Facultad

# Serializers define the API representation.


class FacultadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Facultad
        fields = ('url', 'nombre', 'abrev', 'codigo', 'jerarquia_acad')

# ViewSets define the view behavior.


class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer
