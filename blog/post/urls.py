from django.conf.urls import url
from views import Lenta, ViewMemeDetail, Register, LogoutView, LoginFormView, AddNewMeme, AddLike



urlpatterns = [
	url(r'^$', Lenta.as_view(), name="home"),
	url(r'^showmem/(?P<pk>\d+)/$', ViewMemeDetail.as_view(), name='showmem'),
	url(r'^addlike/(?P<pk>\d+)/$', AddLike.as_view(), name='addlike'),
	url(r'^register$', Register.as_view(), name="register"),
	url(r'^login$', LoginFormView.as_view(), name="login"),
	url(r'^logout$', LogoutView.as_view(), name="logout"),
	url(r'^addnewmeme$', AddNewMeme.as_view(), name='addnew')
]
