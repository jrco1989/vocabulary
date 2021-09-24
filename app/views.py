from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.http import request
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import CreateForm
from app.forms import WordForm

from app.models import Profile
from app.models import Word


class WordsView(ListView):

    template_name = 'home.html'
    model = Word
    ordering = ('-created',)
    paginate_by = 3
    context_object_name = 'words'
    #   import pdb; pdb.set_trace()

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        #context['user'] = self.request.user
        if self.request.user.is_authenticated:
            context['profile'] = self.request.user.profile
        
        return context

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

class CreateWordView(CreateView):
    """Create a new post."""

    template_name = 'create_word.html'
    form_class = WordForm
    success_url = reverse_lazy('home')
    initial = {'user':1,'title':'new'}
    
    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        #context['user'] = self.request.user
        context['user'] = self.request.user.profile
        
        return context

    def  get_initial(self):
        profile = get_object_or_404(Profile, id = self.request.user.profile.id)
        return {'user':profile}

class UpdateWordView(UpdateView):
    model = Word
    fields = ['title','meaning']
    success_url = '/'
    template_name = 'create_word.html'


class DeleteWordView(DeleteView):
    model = Word
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
