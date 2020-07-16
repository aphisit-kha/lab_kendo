from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from api.models import AccMst
from app1.models import SetProv


class AccMstSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccMst
        fields = '__all__'


class SetProvSerializer(serializers.ModelSerializer):
    update_url = HyperlinkedIdentityField(view_name='app1:province_update', lookup_field='provcod')

    class Meta:
        model = SetProv
        fields = '__all__'
