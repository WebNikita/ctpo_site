from django.urls import path
from . import views

app_name = 'ctpo'

urlpatterns = [
    # post views
    path('', views.main_page, name='main_page'),
    path('all_news/', views.all_news, name='all_news'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail, name='post_detail'),
]