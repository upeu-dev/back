from django.conf.urls import include, url


# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from configs.views.UserView import UserViewSet
from configs.views.JerarquiaAcadView import JerarquiaAcadViewSet
from configs.views.InstitucionView import InstitucionViewSet
from configs.views.FacultadView import FacultadViewSet
from configs.views.CarreraView import CarreraViewSet
from configs.views.EscuelaView import EscuelaViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'jerarquiaacads', JerarquiaAcadViewSet)
router.register(r'institucions', InstitucionViewSet)
router.register(r'facultads', FacultadViewSet)
router.register(r'carreras', CarreraViewSet)
router.register(r'escuelas', EscuelaViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
