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
        return f'''{self.dni} - {self.nombre} - {self.apellido}'''
    
    def __str__(self):
        return self.mostrar()

class Cualidad(models.Model):
    cualidad = models.CharField(max_length=50, verbose_name="Tipo")

    def __str__(self) -> str:
        return self.cualidad
    
class Cliente(Persona):
    nickname = models.CharField(max_length=50, verbose_name="Nickname")
    password = models.CharField(max_length=45, verbose_name="Pass")

class Cerveza(models.Model):
    marca = models.CharField(max_length=100, verbose_name="Marca")
    cualidades = models.ManyToManyField(Cualidad, verbose_name="Cualidades")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripcion")
    alcohol = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Alcohol")
    ibu = models.IntegerField(verbose_name="Ibu")
    tapa = models.ImageField(upload_to="assets/tapas/", blank=True, null=True, verbose_name="Tapa")
    botella = models.ImageField(upload_to="assets/botellas/", blank=True, null=True, verbose_name="Botella")
    tipo = models.CharField(max_length=3, verbose_name="Tipo")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    stock = models.IntegerField(verbose_name="Stock", null=True, default=0)

    def __str__(self):
        return f"{self.marca}"

class Proovedor(Persona):
    empresa = models.CharField(max_length=50, verbose_name="Empresa")
    ciudad = models.CharField(max_length=20, verbose_name="Ciudad")
    telefono = models.CharField(max_length=15, verbose_name="Telefono")
    cerveza = models.ManyToManyField(Cerveza, through="IngresoInsumos")

class IngresoInsumos(models.Model):
    proovedor = models.ForeignKey(Proovedor, on_delete=models.RESTRICT)
    cerveza = models.ForeignKey(Cerveza, on_delete=models.RESTRICT)
    fecha = models.DateField(verbose_name="Fecha de ingreso")
    cantidad = models.IntegerField(verbose_name="Cantidad")

    def clean_cantidad(self):
        if self.cleaned_data['cantidad'] <= 0:
            raise ValidationError("La cantidad ingresada debe ser sueprior a 0")
        return self.cleaned_data['cantidad']

    def clean_fecha(self):
        if self.cleaned_data['fecha'] and self.cleaned_data['fecha'] < timezone.now().date:
            raise ValidationError("La fecha de ingreso no puede ser inferior a la fecha de Hoy.")
        return self.cleaned_data['fecha']
    
    def __str__(self) -> str:
        formatted_date = self.fecha.strftime("%d/%m/%Y")
        return f"{formatted_date} - ({self.cantidad}){self.cerveza.marca} - {self.proovedor.empresa}"



