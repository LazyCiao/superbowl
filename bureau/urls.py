from django.urls import path
from . import views

app_name = 'bureau'

urlpatterns = [
    path('match/', views.match, name='match'),
    path('detail/<int:game_id>/', views.detail, name='detail')

]
