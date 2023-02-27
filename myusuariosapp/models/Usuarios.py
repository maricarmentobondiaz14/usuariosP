from django.db import models


class Usuarios(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=12)
    apellidop = models.CharField(db_column='apellidoP', max_length=12)  # Field name made lowercase.
    apellidom = models.CharField(db_column='apellidoM', max_length=12)  # Field name made lowercase.
    edad = models.IntegerField()
    email = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'usuarios'