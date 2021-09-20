from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import fields
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView

from app.models import Profile
from django.forms import ModelForm
from app.forms import CreateForm


def home(request):
    return render(request, 'home.html',{'error':'invalid username and password'})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect ('home')      
        else:
            return render(request, 'login.html',{'error':'invalid username and password'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    print("WWWWWWWWWWWWWWWWWWWWWW")
    logout(request)
    return redirect ('home')
    
class CreteModel(ModelForm):
    class Meta():
        model = Profile
        fields = '__all__'
    def __str__(self):
        return self.name

class SignupView(FormView):
	template_name = 'new.html'
	form_class = CreateForm
	models = Profile
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)