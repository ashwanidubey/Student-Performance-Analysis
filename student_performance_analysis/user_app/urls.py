from . import views
from django.conf.urls import url

urlpatterns=[
url('home/',views.home),
url('myform/',views.myform),
url('taketest1/',views.taketest1),
url('predict/',views.predict),
url('history/',views.history),
url('help/',views.help),
url('showquestion/',views.showquestion),
#url('add/',views.addc),
#url('predict/',views.predict),
#url('^$',views.home),

]
