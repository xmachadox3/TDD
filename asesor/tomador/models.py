# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.


#AIO Área de Investigación y Operaciones
class AIO(models.Model):
	area = models.CharField(max_length=50,primary_key=True)

	def __unicode__(self):
		return u"%s" %self.area

#Sistema de Información
class SIF(models.Model):
	area = models.CharField(max_length=50,primary_key=True)

	def __unicode__(self):
		return u"%s" %self.area

#Nuevas Tecnologias
class NTC(models.Model):
	area = models.CharField(max_length=50,primary_key=True)

	def __unicode__(self):
		return u"%s" %self.area
#Programación
class PRO(models.Model):
	area = models.CharField(max_length=50,primary_key=True)

	def __unicode__(self):
		return u"%s" %self.area

#Telecomunicaciones y Redes
class TRD(models.Model):
	area = models.CharField(max_length=50,primary_key=True)

	def __unicode__(self):
		return u"%s" %self.area

class GER(models.Model):
	area = models.CharField(max_length=50,primary_key=True)

	def __unicode__(self):
		return u"%s" %self.area