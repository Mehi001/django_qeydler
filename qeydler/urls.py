from django.urls import path
from . import views

urlpatterns = [
    path('', views.qeyd_siyahisi, name='siyahisi'),


    path('yeni/', views.qeyd_yarat, name='yarat'), # << Yeni marşrut
    # << Bura dinamik 'int:pk' (Primary Key) dəyərini gözləyən yeni marşrutu əlavə edin
    path('<int:pk>/', views.qeyd_detali, name='detal'),
]