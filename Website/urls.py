from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^item_details/(?P<pk>[0-9]+)/$', views.item_details, name='item_details'),
	url(r'^register/$', views.register.as_view(), name='register'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^add_to_cart/(?P<pk>[0-9]+)/$', views.add_to_cart, name='add_to_cart'),
	url(r'^show_cart/$', views.get_cart, name='show_cart'),
	url(r'^remove_from_cart/(?P<pk>[0-9]+)/$', views.remove_from_cart, name='remove_from_cart'),
	url(r'^thanks_buy/(?P<pk>[0-9]+)/$', views.thanks_buy, name='thanks_buy'),
	url(r'^thanks_cart/(?P<cost>[0-9]+)/$', views.thanks_cart, name='thanks_cart'),
	url(r'^clear_cart/$', views.clear_cart, name='clear_cart'),
	url(r'^contact_us', views.contact_us, name='contact_us'),
]
