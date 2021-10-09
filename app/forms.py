from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets #para importar el modelo ususario 

from app.models import Complement, Genre
from app.models import Profile
from app.models import Word


class CreateForm (forms.Form):
	username= forms.CharField(min_length=4, max_length=50)
	password=forms.CharField(min_length=4, max_length=50, widget=forms.PasswordInput())
	password_confirmation=forms.CharField(max_length=69, widget=forms.PasswordInput())
	first_name=forms.CharField(min_length=3, max_length=90 )
	last_name=forms.CharField(min_length=3, max_length=90 )
	email=forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

	def clean_username(self):
		username=self.cleaned_data['username'] 
		username_taken=User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError ('Username is already in useee')
		return username 

	def clean(self):
		data=super().clean() 
		password=data['password']
		password_confirmation=data['password_confirmation']
		if password!=password_confirmation:
			raise forms.ValidationError('Password do not match.') 

		return data

	def save(self):
		data = self.cleaned_data
		data.pop('password_confirmation')
		user = User.objects.create_user(**data) 
		profile = Profile(user=user)
		profile.save()

class ProfileForm2(forms.Form):

	user_id = forms.IntegerField(required=True, widget = forms.HiddenInput())
	username = forms.CharField(required=False, label=('Username:'),error_messages={forms.ValidationError: 'Please enter your name'})
	first_name = forms.CharField(required=False, label=('First Name:'))
	last_name = forms.CharField(required=False, label=('Last Name:'))
	email = forms.EmailField(required=False, label=('Email:'))
	
	def clean_username(self):
		username=self.cleaned_data['username']
		own_username = User.objects.get(id=self.cleaned_data['user_id']).username
		username_taken=User.objects.filter(username=username).exists()	
		if username_taken:
			print('it is error')
			raise forms.ValidationError ('Username is already in use') 
		return username 

	def clean(self):
		data=super().clean() 
		return data

	def save(self):
		data = self.cleaned_data
		
	

class ProfileForm(forms.ModelForm):

	user_id = forms.IntegerField(required=True, widget = forms.HiddenInput())
	username = forms.CharField(required=False, label=('Username:'))
	first_name = forms.CharField(required=False, label=('First Name:'))
	last_name = forms.CharField(required=False, label=('Last Name:'))
	email = forms.EmailField(required=False, label=('Email:'))
	
	def clean_username(self):
		username=self.cleaned_data['username']
		own_username = User.objects.get(id=self.cleaned_data['user_id']).username
		username_taken=User.objects.filter(username=username).exists()	
		if username_taken and username != own_username:
			print('it is error')
			raise forms.ValidationError ('Username is already in use') 
		return username 

	def clean(self):
		data=super().clean() 
		return data
	
	class Meta():

		model = Profile
		fields = ('user_id','username','first_name','last_name','email','picture',)
		# widgets = {'username': forms.TextInput(),}
		# widgets = {'picture': forms.FileInput(attrs={'style': 'display:none;'}),}
		widgets = {
			'user_id': forms.HiddenInput(),
		}
	

class WordForm (forms.ModelForm):

	class Meta():
		model = Word
		fields = ('user','title','meaning','genre')
		widgets = {
			'user': forms.HiddenInput(), 
			'meaning' : forms.Textarea(),
			'genre': forms.CheckboxSelectMultiple()}

	def __init__(self, *args, **kwargs):
		print('kwargs')
		print(kwargs)
		user = kwargs['initial']['user']
		super(WordForm, self).__init__(*args, **kwargs)
		self.fields['genre'].queryset = Genre.objects.filter(user=user)

			
class ComplementForm (forms.ModelForm):

	class Meta():
		model = Complement
		fields = ('user','parent','title','meaning')
		widgets = {
			'user': forms.HiddenInput(),
			'parent': forms.HiddenInput(),
			'meaning' : forms.Textarea(),
		}


class GenreForm (forms.ModelForm):

	class Meta():
		model = Genre
		fields = ('user','name')
		widgets = {'user': forms.HiddenInput()}

class dELETEGenreForm(forms.ModelForm):
	
	class Meta():
		model = Genre
		fields = ('name',)