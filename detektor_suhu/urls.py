from rest_framework import routers
from detektor_suhu.views import  statsViewSet


router = routers.DefaultRouter()
router.register('stats',statsViewSet)

urlpatterns = []
urlpatterns += router.urls