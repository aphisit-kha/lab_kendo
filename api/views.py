import json

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.models import AccMst
from api.serializers import AccMstSerializer, SetProvSerializer
from app1.amphoe import Amphoe
from app1.models import SetProv


def ConvertStrToList(data):
    data_list = json.loads(data)
    return data_list


class AccMstListView(ListAPIView):
    serializer_class = AccMstSerializer
    pagination_class = None

    def get_queryset(self, *args, **kwargs):
        provinces = AccMst.objects.all()
        return provinces


class SetProvListView(ListAPIView):
    serializer_class = SetProvSerializer
    pagination_class = None

    def get_queryset(self, *args, **kwargs):
        provinces = SetProv.objects.all()
        return provinces


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AmphoeTemp(request):
    amphoe = Amphoe(request)
    if request.data:
        data_list = ConvertStrToList(request.data['models'])
    else:
        data_list = list()

    if request.method == 'GET':
        return Response(amphoe.amphoe)

    if request.method == 'POST':
        result = list()
        for item in data_list:
            data = amphoe.add(item)
            result.append(data)
        return Response(result)

    if request.method == 'PUT':
        result = list()
        for item in data_list:
            data = amphoe.update(item)
            result.append(data)
        return Response(result)

    if request.method == 'DELETE':
        for item in data_list:
            amphoe.remove(item['idno'])
        return Response(amphoe.amphoe)


@api_view(['GET'])
def AmphoeClear(request):
    if request.method == 'GET':
        amphoe = Amphoe(request)
        amphoe.clear()
        return Response([{}])
