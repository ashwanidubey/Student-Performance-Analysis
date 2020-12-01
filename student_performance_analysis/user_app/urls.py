from . import views
from django.conf.urls import url

urlpatterns=[
url('home/',views.home),
#url('^$',views.home),

]
