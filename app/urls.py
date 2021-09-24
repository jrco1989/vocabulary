from django.urls import path 
from app import views


urlpatterns=[
	path(
        route='',
        view=views.WordsView.as_view(),
        name='home'
    ),path(
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
        route='delete/word/<pk>',
        view=views.DeleteWordView.as_view(),
        name='delete_word'
    )
    ]