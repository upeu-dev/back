from rest_framework import serializers, viewsets
from configs.models.Institucion import Institucion

# Serializers define the API representation.


class InstitucionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Institucion
        fields = ('url', 'nombre', 'abrev', 'codigo',
                  'estructura_validada', 'jerarquia_acad')

# ViewSets define the view behavior.


class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
