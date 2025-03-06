from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from app1.amphoe import Amphoe
from app1.models import SetProv, SetAump


def index(request):
    return render(request, 'app1/index.html')


def create(request):
    print('create')
    if request.method == "POST":
        provcod = request.POST['provcod']
        provdes = request.POST['provdes']
        # start transaction
        with transaction.atomic():
            province = SetProv(provcod=provcod, provdes=provdes)
            province.save()
            temp_amphoe = Amphoe(request)
            # create
            for item in temp_amphoe.amphoe:
                amphoe = SetAump(provcod=provcod, aumpcod=item['aumpcod'], aumpdes=item['aumpdes'],
                                 postcod=item['postcod'])
                amphoe.save()
            # clear session
            temp_amphoe.clear()
        return redirect('app1:province_index')
    else:
        Amphoe(request).clear()
        return render(request, 'app1/create.html')


def update(request, provcod):
    province = get_object_or_404(SetProv, provcod=provcod)
    if request.method == "POST":
        provcod = request.POST['provcod']
        provdes = request.POST['provdes']
        # start transaction
        with transaction.atomic():
            province.provcod = provcod
            province.provdes = provdes
            province.save()
            temp_amphoe = Amphoe(request)
            # delete
            amphoe = SetAump.objects.filter(provcod=provcod)
            for db_amphoe in amphoe:
                deleted = True
                for item in temp_amphoe.amphoe:
                    if db_amphoe.idno == item['idno']:
                        deleted = False
                if deleted == True:
                    db_amphoe.delete()
            # create and update
            for item in temp_amphoe.amphoe:
                try:
                    amphoe = SetAump.objects.get(idno=item['idno'])
                except SetAump.DoesNotExist:
                    amphoe = None
                if amphoe is not None:
                    amphoe.provcod = provcod
                    amphoe.aumpcod = item['aumpcod']
                    amphoe.aumpdes = item['aumpdes']
                    amphoe.postcod = item['postcod']
                else:
                    amphoe = SetAump(provcod=provcod, aumpcod=item['aumpcod'], aumpdes=item['aumpdes'],
                                     postcod=item['postcod'])
                amphoe.save()
            # clear session
            temp_amphoe.clear()
        return redirect('app1:province_index')
    else:
        # clear session
        Amphoe(request).clear()
        # create from db
        amphoe = SetAump.objects.filter(provcod=provcod)
        temp_amphoe = Amphoe(request)
        for db_amphoe in amphoe:
            item = dict(idno=db_amphoe.idno, aumpcod=db_amphoe.aumpcod, aumpdes=db_amphoe.aumpdes, postcod=db_amphoe.postcod)
            data = temp_amphoe.add(item)
        context = {
            'province': province,
        }
        return render(request, 'app1/update.html', context)


def refresh(request, provcod):
    if provcod == '':
        # clear session
        Amphoe(request).clear()
    else:
        # clear session
        Amphoe(request).clear()
        # create from db
        amphoe = SetAump.objects.filter(provcod=provcod)
        temp_amphoe = Amphoe(request)
        for db_amphoe in amphoe:
            item = dict(idno=db_amphoe.idno, aumpcod=db_amphoe.aumpcod, aumpdes=db_amphoe.aumpdes, postcod=db_amphoe.postcod)
            data = temp_amphoe.add(item)
    return HttpResponse('refresh session')