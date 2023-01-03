from django.urls import path
from . import views

#填写 login,update,delete 路由
urlpatterns = [
    path('pc/', views.pc),
    path('qx/', views.qx),
    path('fx/', views.fx),
    path('xx/', views.xx),
]