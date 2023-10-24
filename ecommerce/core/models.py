from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email")
    dni = models.IntegerField(verbose_name="Dni", unique=True)

    def clean_dni(self):
        if not (len(str(self.cleaned_data['dni']))==7 or len(str(self.cleaned_data['dni']))==8):
            raise ValidationError("El Dni debe ser un numero positivo de 8 o 7 digitos")
        return self.cleaned_data['dni']

    class Meta:
        abstract = True

    def mostrar(self):
        return f'''Nombre: {self.nombre} \n
                   Apellido: {self.apellido} \n
                   Email: {self.email} \n
                   DNI: {self.dni} \n'''
    
    def __str__(self):
        return self.mostrar()
    
class Cerveza(models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca")
    tipo = models.CharField(max_length=3, verbose_name="Tipo")
    vencimiento = models.DateField(verbose_name="Fecha vencimiento", null=True)

    def clean_vencimiento(self):
        if self.cleaned_data['vencimiento'] and self.cleaned_data['vencimiento'] < timezone.now().date:
            raise ValidationError("La cerveza no puede estar vencida.")
        return self.cleaned_data['vencimiento']

class Proovedor(Persona):
    empresa = models.CharField(max_length=50, verbose_name="Empresa")
    ciudad = models.CharField(max_length=20, verbose_name="Ciudad")
    telefono = models.CharField(max_length=15, verbose_name="Telefono")
    cerveza = models.ManyToManyField(Cerveza, through="IngresoInsumos")

class IngresoInsumos(models.Model):
    proovedor = models.ForeignKey(Proovedor, on_delete=models.RESTRICT)
    cerveza = models.ForeignKey(Cerveza, on_delete=models.RESTRICT)
    fecha = models.DateField(verbose_name="Fecha de ingreso")

    def clean_fecha(self):
        if self.cleaned_data['fecha'] and self.cleaned_data['fecha'] < timezone.now().date:
            raise ValidationError("La fecha de ingreso no puede ser inferior a la fecha de Hoy.")
        return self.cleaned_data['fecha']
    
class Cliente(Persona):
    nickname = models.CharField(max_length=50, verbose_name="Nickname")
    password = models.CharField(max_length=45, verbose_name="Pass")
    cerveza = models.ForeignKey(Cerveza, on_delete=models.CASCADE)
