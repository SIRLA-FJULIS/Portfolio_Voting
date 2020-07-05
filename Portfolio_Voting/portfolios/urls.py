from django.urls import path
from . import views

app_name = 'portfolios'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.article, name='article')
]