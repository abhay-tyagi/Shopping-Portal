from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^item_details/(?P<pk>[0-9]+)/$', views.item_details, name='item_details'),
	url(r'^register/$', views.register.as_view(), name='register'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^thanks/(?P<pk>[0-9]+)/$', views.thanks, name='thanks'),
	url(r'^contact_us', views.contact_us, name='contact_us'),
	#url(r'^logout/$', views.user_logout, name='user_logout'),
]
