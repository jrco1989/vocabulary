from django.urls import path 
from app import views


urlpatterns=[
	path(
        route='',
        view=views.home,
        name='home'
    ),path(
        route='login',
        view=views.login_view,
        name='login',
    ),
    path(
        route='chao',
        view=views.logout_view,
        name='chao',
    ),
    path(
        route='sign',
        view=views.SignupView.as_view(),
        name='sign'
    )
    ]