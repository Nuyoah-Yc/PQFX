from django.urls import path
from . import views

#填写 login,update,delete 路由
urlpatterns = [
    path('file_up/', views.file_up),
    path('pc/', views.pc),
    path('pc_Ajax/', views.pc_Ajax),
    path('qx/', views.qx),
    path('qx_Ajax/', views.qx_Ajax),
    path('fx/', views.fx),
    path('fx_Ajax/', views.fx_Ajax),
    path('xx/', views.xx),
    path('xx_Ajax/', views.xx_Ajax),
    path('text/', views.text),
    path('text_Ajax/', views.text_Ajax),
]