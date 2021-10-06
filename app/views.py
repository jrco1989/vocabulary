from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.http import request
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse 
from django.urls.base import reverse_lazy

from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import ComplementForm
from app.forms import CreateForm
from app.forms import dELETEGenreForm
from app.forms import GenreForm
from app.forms import WordForm

from app.models import Complement, Genre, Profile
from app.models import Word

def index(request):
    
    return render(request, 'index.html')


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
    return redirect ('index')


class WordsView(LoginRequiredMixin, ListView):

    template_name = 'home.html'
    model = Word
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'words'
    #   import pdb; pdb.set_trace()

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = self.request.user.profile
        return context
    
    def get_queryset(self):
        return Word.objects.filter(user = self.request.user.profile)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'detail_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #if self.request.user.is_authenticated:
         #   context['profile'] = self.request.user.profile
        print(context)
        return context




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


class CreateWordView(LoginRequiredMixin, CreateView):

    template_name = 'create_word.html'
    form_class = WordForm
    success_url = reverse_lazy('user')
    
    def get_context_data(self, **kwargs):
        """Add profile to context."""

        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = self.request.user.profile
            print("··is authenticated")
        context['title'] = 'New'  
        context['id_word'] = '0'
        #import pdb; pdb.set_trace()      
        return context

    def  get_initial(self):
        profile = get_object_or_404(Profile, id = self.request.user.profile.id)
        return {'user':profile}


class UpdateWordView(UpdateView):
    
    model = Word
    form_class = WordForm
    success_url = '/'
    template_name = 'create_word.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        word_id = int(self.request.path.split('/')[-1])
        context['id_word'] = word_id
        # import pdb; pdb.set_trace()
        return context

    def  get_initial(self):
        profile = get_object_or_404(Profile, id = self.request.user.profile.id)
        return {'user':profile}


class DeleteWordView(DeleteView):
    model = Word
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DetailWordView(DetailView):
    model = Word
    template_name = 'detail_word.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = self.request.user.profile
        print(context)
        return context


class CreateComplementView(CreateView):
    
    template_name = 'create_complement.html'
    form_class = ComplementForm
    
    def get_context_data(self, **kwargs):
        """Add profile to context."""
        context = super().get_context_data(**kwargs)
        id_word = self.kwargs['pk']
        context['id_word'] = id_word
        context['title'] = 'New'        
        
        return context

    def  get_initial(self):
        profile = get_object_or_404(Profile, id = self.request.user.profile.id)
        word_id = int(self.request.path.split('/')[-1])
        word = get_object_or_404(Word, id = word_id)
        return {'user':profile, 'parent':word}
    
    def get_success_url(self):
        return reverse('detail_word', args = [self.kwargs['pk']])
        

class UpdateComplementView(UpdateView):
    
    model = Complement
    form_class = ComplementForm
    # success_url = 'detail_complement'
    template_name = 'create_complement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        word_id = int(self.request.path.split('/')[-1])
        context['id_word'] = word_id
        # import pdb; pdb.set_trace()
        return context

    def get_success_url(self):
        
        return reverse('detail_complement', args = [self.kwargs['pk']])
        
    def  get_initial(self):
        profile = get_object_or_404(Profile, id = self.request.user.profile.id)
        return {'user':profile}


class DeleteComplementView(DeleteView):
    model = Complement

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        id_deleted = self.kwargs['pk']
        print(id_deleted)
        complement = get_object_or_404(Complement, id = self.kwargs['pk'])

        print('id_deletedid_deletedid_deletedid_deletedid_deletedid_deletedid_deletedid_deletedid_deleted')
        return reverse('detail_word', args = [complement.parent.id])


class ComplementDetailView(DetailView):
    model = Complement
    template_name = 'detail_complement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = self.request.user.profile
        print(context)
        return context


class CreateGenreView(CreateView):
    
    template_name = 'create_genre.html'
    form_class = GenreForm

    def  get_initial(self):
        profile = get_object_or_404(Profile, id = self.request.user.profile.id)
        return {'user':profile}

    def get_success_url(self):
        # import pdb; pdb.set_trace()

        if self.kwargs['pk'] == 0:
            return reverse('create_word')
        return reverse('edit_word', args = [self.kwargs['pk']])
        
        # return reverse('createword', args = [self.object.book.id])


class ListGenreView(LoginRequiredMixin, ListView, FormMixin):
    
    models = Genre
    form_class = dELETEGenreForm
    template_name = 'list_genre.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return Genre.objects.filter(user = self.request.user.profile)

    def get(self, request, *args, **kwargs):
        print(' yyyyyyyyyyyyyyyyyyy')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        print('posy yyyyyyyyyyyyyyyyyyy')
        genres_id = request.POST.getlist('genre_check')
        for id in genres_id:
            instance = Genre.objects.get(id=id)
            instance.delete()
            #instance.save()
        
        if self.kwargs['pk'] == 0:
            print('insert pk')
            return redirect('create_word')

        print("don't enteredif ")
        print(self.kwargs['pk'] )
		
        url= reverse('edit_word', kwargs={'pk':self.kwargs['pk'] })
        
        return redirect(url)



