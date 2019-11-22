from rest_framework import serializers

from detektor_suhu.models import stats



class StatsSerializer (serializers.ModelSerializer):
    class Meta:
        model = stats
        fields = ' __all__ '