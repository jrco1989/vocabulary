from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets #para importar el modelo ususario 

from app.models import Genre
from app.models import Profile
from app.models import Word


class CreateForm (forms.Form):
	username= forms.CharField(min_length=4, max_length=50)
	password=forms.CharField(min_length=4, max_length=50, widget=forms.PasswordInput())
	password_confirmation=forms.CharField(max_length=69, widget=forms.PasswordInput())
	first_name=forms.CharField(min_length=3, max_length=90 )
	last_name=forms.CharField(min_length=3, max_length=90 )
	email=forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

	# los widgets son una representación de django de elementos de html y pueden iclluir ciertas validaciones 
	
	#se debe crear la funcion de validación para validar los campos del formulario
	def clean_username(self):
		#Username most be unique
		username=self.cleaned_data['username']#debemos traer el valor con este atributo	que se trea de un diccionario
		#usamos filter en vez de get para evitar que no straiga un aexcepción, 
		#el exist se usa para evitar hacer un query de todo el usuario, nos retorna un booleano 
		username_taken=User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError ('Username is already in use') #para lanzar una excepción 
		return username #es necesario retornar el dato para evitar que cuando se llame el metodo clean no suceda error por estar vacío

	def clean(self):
		#verify passwords 
		data=super().clean() #no queremo ssobre escribir todo el método, para esto usamos dla variable data que traerá todos los datos usando super() que un aforma de python de llamar el mpetodo 
		password=data['password']
		password_confirmation=data['password_confirmation']
		if password!=password_confirmation:
			raise forms.ValidationError('Password do not match.') #lanzamos nuevamente la exceocion 

		return data

        #Create user and profile.
	def save(self):
		data = self.cleaned_data
		data.pop('password_confirmation')
		user = User.objects.create_user(**data) #el **data me ayuda para n otener que escribir todos los datos com opor ejemplo "email=data['email']", ed ecir que los dos arteriscos me ayudan par enviar todo el diccinario
		profile = Profile(user=user)
		profile.save()


class WordForm (forms.ModelForm):

	class Meta():
		model = Word
		fields =('user','title','meaning','genre')
		CHOICES = (
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)
		widgets = {'user': forms.HiddenInput(), 'genre': forms.CheckboxSelectMultiple()}

			
		