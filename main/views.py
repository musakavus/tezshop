from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from main.models import Category


def user_not_authenticated(user):
    return not user.is_authenticated


def home(request):
    categories = Category.objects.filter(parent_category=None)  # Ana kategorileri alın
    return render(request, 'index.html', {'categories': categories})


def hakkimizda(request):
    return render(request, 'hakkimizda.html')


def kayit(request):
    return render(request, 'register.html')


def siparis_tamamla(request):
    return render(request, 'siparis-tamamla.html')


def giris(request):
    return render(request, 'login.html')


def kategoriler(request):
    return render(request, 'kategori.html')


def iletisim(request):
    return render(request, 'iletisim.html')


def istek_listesi(request):
    return render(request, 'istek-listesi.html')


def siparis_detayi(request):
    return render(request, 'siparis-detayi.html')


def karsilastir(request):
    return render(request, 'karsilastir.html')


def profilim(request):
    return render(request, 'profilim.html')


def urun_gecmisi(request):
    return render(request, 'urun-gecmisi.html')


def siparis_detayi(request):
    return render(request, 'siparis-detayi.html')


def hediye_ceki(request):
    return render(request, 'hediye-ceki.html')


def urun_detay(request):
    return render(request, 'urun-detay.html')
