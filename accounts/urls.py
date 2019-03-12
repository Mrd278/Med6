from django.conf.urls import url
from .import views

app_name='accounts'

urlpatterns=[
    url(r'login/signup/',views.signup,name='signup'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^login/$',views.booking,name='booking')
]