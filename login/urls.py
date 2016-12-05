from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'/authenticate$', views.auth),
    url(r'upload_file',views.upload_file),
    # url(r'/home',views.login_success)
]
