from django import forms
from django.core.exceptions import ValidationError
from .models import Cerveza


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

class AltaCervezaModelForm(forms.ModelForm):
    class Meta:
        model = Cerveza
        fields = '__all__'
    
    def clean_alcohol(self):
        alcohol = self.alcohol.strip()

        if alcohol > 0 and alcohol%2 != 0:
            raise ValidationError("La dosis de alcohol podria matar a una persona")
        
        self.changed_data['alcohol'] = alcohol
        return self.changed_data['alcohol']