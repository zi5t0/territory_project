# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.core import validators

class Hermano(models.Model):
    idhermano = models.IntegerField()
    nombre_completo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hermano'
# Unable to inspect table 'prestamo'
# The error was: list index out of range


class Territorio(models.Model):
    numero = models.IntegerField()
    estado = models.IntegerField(null=True, blank=True, default=0)
    campania = models.IntegerField()
    lluvia = models.IntegerField()
    zona = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'territorio'


class Usuario(models.Model):
    idusuario = models.IntegerField()
    nombre_completo = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'usuario'
