#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Receta, Comentario


class ContactoForm(forms.fomr):
	correo =forms.EmailField(label= 'tu correo electronico')
	mensaje =forms.CharField(widget=forms.Textarea)

class RecetaForm(ModelForm):
	class Meta:
		model = Receta

class ComentarioForm(modelForm):
	class Meta:
		model = Comentario