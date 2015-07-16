from rest_framework import serializers, viewsets
from configs.models.JerarquiaAcad import JerarquiaAcad


# Serializers define the API representation.


class JerarquiaAcadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JerarquiaAcad
        fields = ('url', 'tipo', 'institucion', 'parent')

# ViewSets define the view behavior.


class JerarquiaAcadViewSet(viewsets.ModelViewSet):
    queryset = JerarquiaAcad.objects.all()
    serializer_class = JerarquiaAcadSerializer
