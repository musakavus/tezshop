from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('kayitol/', views.kayit, name='kayit'),
    path('giris/', views.giris, name='giris'),
    path('kategoriler/', views.kategoriler, name='kategoriler'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('siparis-tamamla/', views.siparis_tamamla, name='siparis_tamamla'),
    path('istek-listesi/', views.istek_listesi, name='istek_listesi'),
    path('karsilastir/', views.karsilastir, name='karsilastir'),
    path('profil/', views.profilim, name='profil'),
    path('urun-gecmisi/', views.urun_gecmisi, name='urun_gecmisi'),
    path('siparis-detayi/', views.siparis_detayi, name='siparis_detayi'),
    path('hediye-ceki/', views.hediye_ceki, name='hediye_ceki'),
    path('urun-detay/', views.urun_detay, name='urun_detay'),

]
