from . import views
from django.conf.urls import url

urlpatterns=[
url('home/',views.home),
url('myform/',views.myform),
url('taketest/',views.taketest),
#url('^$',views.home),

]
