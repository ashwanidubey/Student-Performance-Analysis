from . import views
from django.conf.urls import url

urlpatterns=[
url('home/',views.home),
url('myform/',views.myform),
url('taketest/',views.taketest),
url('predict/',views.predict),
url('history/',views.history),
url('help/',views.help),
#url('predict/',views.predict),
#url('^$',views.home),

]
