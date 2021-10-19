from django.urls import path 
from app import views


urlpatterns=[
	path(
        route='',
        view=views.index,
        name='index'
    ),
    #user
    path(
        route='login',
        view=views.login_view,
        name='login',
    ),
    path(
        route='logout',
        view=views.logout_view,
        name='logout',
    ),
    path(
        route='signup',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='user/<dict>',
        view=views.WordsView.as_view(),
        name='home'
    ),
    path(
        route='user/details/<int:pk>',
        view=views.ProfileUpdateView.as_view(),
        name='detail_user'
    ),
    #words
    path(
        route='createword',
        view=views.CreateWordView.as_view(),
        name='create_word'
    ),
    path(
        route='edit/word/<pk>',
        view=views.UpdateWordView.as_view(),
        name='edit_word'
    ),
    path(
        route='delete/word/<int:pk>',
        view=views.DeleteWordView.as_view(),
        name='delete_word'
    ),
    path(
        route='detail/word/<int:pk>',
        view=views.DetailWordView.as_view(),
        name='detail_word'
    ),
    #complements
    path(
        route='complement/create/<int:pk>',
        view=views.CreateComplementView.as_view(),
        name='create_complement'
    ),
    path(
        route='detail/complement/<int:pk>',
        view=views.ComplementDetailView.as_view(),
        name='detail_complement'
    ),
    path(
        route='edit/complement/<pk>',
        view=views.UpdateComplementView.as_view(),
        name='edit_complement'
    ),
    path(
        route='delete/complement/<int:pk>',
        view=views.DeleteComplementView.as_view(),
        name='delete_complement'
    ),
    #genres
    path(
        route='genre/create/<int:pk>',
        view=views.CreateGenreView.as_view(),
        name='create_genre'
    ),
    path(
        route='genre/list/<int:pk>',
        view=views.ListGenreView.as_view(),
        name='list_genre'
    )
    ]