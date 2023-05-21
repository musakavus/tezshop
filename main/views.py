from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from main.forms import RegistrationForm, LoginForm
from main.models import Category, Registration


def user_not_authenticated(user):
    return not user.is_authenticated


def home(request):
    categories = Category.objects.filter(parent_category=None)  # Ana kategorileri alın
    return render(request, 'index.html', {'categories': categories})


def hakkimizda(request):
    return render(request, 'hakkimizda.html')


def kayit(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.password = make_password(registration.password)  # Şifreyi hashle
            registration.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def siparis_tamamla(request):
    return render(request, 'siparis-tamamla.html')


def giris(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Giriş başarılıysa yönlendirilecek sayfa adını belirtin
            else:
                # Giriş başarısız olduğunda yapılacak işlemler
                form.add_error(None, "Geçersiz kullanıcı adı veya şifre.")
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


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
