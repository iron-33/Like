from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class LoginView(TemplateView):
    template_name = "app/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

def index(request):
    return render(request, 'app/index.html')

def forgotPass(request):
    return render(request, 'app/forgot-pass.html')

def order(request):
    return render(request, 'app/order.html')

def cabinet(request):
    return render(request, 'app/cabinet.html')

def services(request):
    return render(request, 'app/services.html')

def news(request):
        news=News.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(news, 3)
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)
        return render(request, 'app/news.html', {'blog_list': blog_list})

def balance(request):
    return render(request, 'app/balance.html')