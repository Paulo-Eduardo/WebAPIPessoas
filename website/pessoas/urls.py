from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from pessoas import views

urlpatterns = [
    url(r'^pessoas/$', views.PessoaList.as_view()),
    url(r'^pessoas/(?P<pk>[0-9]+)/$', views.PessoaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)