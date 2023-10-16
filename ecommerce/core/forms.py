from django import forms
from django.core.exceptions import ValidationError


class FormStyle(forms.TextInput):
    class Media:
        CSS = {'all': ('core/css/main.css',)}


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombres:')
    apellido =forms.CharField(label='Apellido:')
    telefono =forms.IntegerField(label='Telefono:')
    email = forms.EmailField(label='Email')
    pais = forms.CharField(label="Pais")
    ciudad = forms.CharField(label="Ciudad")
    gustaCerveza = forms.BooleanField(label="¿Te gusta la cerveza?", required=False)
    consulta =  forms.CharField(widget=forms.Textarea)

    def clean_nombre(self):
        if self.cleaned_data["nombre"] == "Ulises":
            raise ValidationError("El usuario no puede tener menos de 18 años")
        
        return self.cleaned_data["nombre"]

    def clean(self):
        pass
        # Este if simula una busqueda en la base de datos
#        if self.cleaned_data["nombre"] == "Carlos" and self.cleaned_data["apellido"] == "Lopez":
 #           raise ValidationError("El usuario Carlos Lopez ya existe")
        
        # Si el usuario no existe lo damos de alta

  #      return self.cleaned_data