# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect 

from .models import *
import unicodedata
import json
  

def index(request):
	if request.method == 'POST':
		contadores = {
			"AIO" : 0.0,
			"SIF" : 0.0,
			"NTC" : 0.0,
			"PRO" : 0.0,
			"TRD" : 0.0,
			"GER" : 0.0,
		}	
		AIO_set  	= set()
		SIF_set  	= set()
		NTC_set  	= set()
		PRO_set  	= set()
		TRD_set  	= set()
		GER_set 	= set()
			
		
		palabras = request.POST.get('tplanteamiento') + request.POST.get('dplanteamiento')
		removes = set(['.',',',';','-',':','...','1','2','3','4','5','6','7','8','9','0','!','?','/','_','¡','¿'])
		for i in palabras.split():	
			i = ''.join([c for c in i if c not in removes])
			i = i.lower()
			if AIO.objects.filter(area = i):
				contadores["AIO"] = contadores["AIO"] + 1
				AIO_set.add(i)
			if SIF.objects.filter(area = i):
				contadores["SIF"] = contadores["SIF"] + 1
				SIF_set.add(i)
			if NTC.objects.filter(area = i):
				contadores["NTC"] = contadores["NTC"] + 1
				NTC_set.add(i)
			if PRO.objects.filter(area = i):
				contadores["PRO"] = contadores["PRO"] + 1
				PRO_set.add(i)				
			if TRD.objects.filter(area = i):
				contadores["TRD"] = contadores["TRD"] + 1
				TRD_set.add(i)
			if GER.objects.filter(area = i):
				contadores["GER"] = contadores["GER"] + 1
				GER_set.add(i)
		
		total = contadores["AIO"] + contadores["SIF"] + contadores["NTC"] + contadores["PRO"] + contadores["TRD"] + contadores["GER"]
		
		#Comparacion con AIO 
		if contadores["AIO"] > contadores["SIF"]:
			SIF_set = SIF_set - AIO_set
		if contadores["AIO"] > contadores["NTC"]:
			NTC_set = NTC_set - AIO_set
		if contadores["AIO"] > contadores["PRO"]:
			PRO_set = PRO_set - AIO_set
		if contadores["AIO"] > contadores["TRD"]:
			TRD_set = TRD_set - AIO_set
		if contadores["AIO"] > contadores["GER"]:
			GER_set = GER_set - AIO_set

		#Comparacion con SIF 
		if contadores["SIF"] > contadores["AIO"]:
			AIO_set = AIO_set - SIF_set
		if contadores["SIF"] > contadores["NTC"]:
			NTC_set = NTC_set - SIF_set
		if contadores["SIF"] > contadores["PRO"]:
			PRO_set = SIF_set - SIF_set
		if contadores["SIF"] > contadores["TRD"]:
			TRD_set = SIF_set - SIF_set
		if contadores["SIF"] > contadores["GER"]:
			GER_set = SIF_set - SIF_set

		#Comparacion con NTC 
		if contadores["NTC"] > contadores["AIO"]:
			NTC_set = NTC_set - AIO_set
		if contadores["NTC"] > contadores["SIF"]:
			NTC_set = NTC_set - SIF_set
		if contadores["NTC"] > contadores["PRO"]:
			NTC_set = NTC_set - PRO_set
		if contadores["NTC"] > contadores["TRD"]:
			NTC_set = NTC_set - TRD_set
		if contadores["NTC"] > contadores["GER"]:
			NTC_set = NTC_set - GER_set

		#Comparacion con PRO 
		if contadores["PRO"] > contadores["AIO"]:
			PRO_set = PRO_set - AIO_set
		if contadores["PRO"] > contadores["SIF"]:
			PRO_set = PRO_set - SIF_set
		if contadores["PRO"] > contadores["NTC"]:
			PRO_set = PRO_set - NTC_set
		if contadores["PRO"] > contadores["TRD"]:
			PRO_set = PRO_set - TRD_set
		if contadores["PRO"] > contadores["GER"]:
			PRO_set = PRO_set - GER_set

		#Comparacion con TRD
		if contadores["TRD"] > contadores["AIO"]:
			TRD_set = TRD_set - AIO_set
		if contadores["TRD"] > contadores["SIF"]:
			TRD_set = TRD_set - SIF_set
		if contadores["TRD"] > contadores["NTC"]:
			TRD_set = TRD_set - NTC_set
		if contadores["TRD"] > contadores["PRO"]:
			TRD_set = TRD_set - PRO_set
		if contadores["TRD"] > contadores["GER"]:
			TRD_set = TRD_set - GER_set

		#Comparacion con GER
		if contadores["GER"] > contadores["AIO"]:
			GER_set = GER_set - AIO_set
		if contadores["GER"] > contadores["SIF"]:
			GER_set = GER_set - SIF_set
		if contadores["GER"] > contadores["NTC"]:
			GER_set = GER_set - NTC_set
		if contadores["GER"] > contadores["PRO"]:
			GER_set = GER_set - PRO_set
		if contadores["GER"] > contadores["TRD"]:
			GER_set = GER_set - TRD_set

		if total == 0:
			return HttpResponseRedirect('/tomador/nocongruencia')
		else:
			contadores["AIO"] = contadores["AIO"] / total
			contadores["SIF"] = contadores["SIF"] / total
			contadores["NTC"] = contadores["NTC"] / total
			contadores["PRO"] = contadores["PRO"] / total
			contadores["TRD"] = contadores["TRD"] / total
			contadores["GER"] = contadores["GER"] / total
			print "AIO palabras concurrentes /n %s " % AIO_set
			print "SIF palabras concurrentes /n %s " % SIF_set
			print "NTC palabras concurrentes /n %s " % NTC_set
			print "PRO palabras concurrentes /n %s " % PRO_set
			print "TRD palabras concurrentes /n %s " % TRD_set
			print "GER palabras concurrentes /n %s " % GER_set
			
			
			
			return render(request,'respuesta.html', {'contar': contadores, 'AIO': AIO_set,'SIF':SIF_set,'NTC':NTC_set,'PRO':PRO_set,'TRD':TRD_set,'GER':GER_set})
	else:
		return render(request, 'index.html')

def nocongruencia(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/tomador')
	else:
		return render(request, 'nocongruencia.html')

