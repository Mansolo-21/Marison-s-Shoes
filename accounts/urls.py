from django.urls import path
from . import views

urlpatterns = [

    path( 'signup/',views.signup_view,name='signup'),

    path('login/',views.login_view,name='login'),

    path(
        'logout/',
        views.logout_view,
        name='account_logout'
    ),

    path(
        'redirect/',
        views.redirect_user,
        name='redirect_user'
    ),
    path(
'promote/<int:id>/',
views.promote_user,
name='promote_user'
)

]