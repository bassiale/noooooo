from dataclasses import dataclass
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import bmp_data




def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def live_data(request):
    template = loader.get_template('main/live_data.html')
    temperatures = [x.temperature for x in bmp_data.objects.all()]
    pressures = [x.pressure for x in bmp_data.objects.all()]
    altitudes = [x.altitude for x in bmp_data.objects.all()]
    ids = [x.id for x in bmp_data.objects.all()]
    context = {'temperatures': temperatures, 'pressures': pressures, 'altitudes': altitudes, 'ids':ids}
    return HttpResponse(template.render(context, request))

def no(request, temperature, pressure, altitude):
    a = bmp_data(temperature=temperature, pressure=pressure, altitude=altitude)
    a.save()
    return HttpResponse('dati aggiunti al database')

def about_us(request):
    template = loader.get_template('main/about_us.html')
    context = {}
    return HttpResponse(template.render(context, request))
