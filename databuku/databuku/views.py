from django.views.generic import TemplateView
from django.contrib.auth import authenticate , login, logout
from cerpen.views import CerpenPerKategori
from .forms import FormLogin
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin

    

class BlogHomeView(LoginRequiredMixin,TemplateView, CerpenPerKategori):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_latest_cerpen_each_kategori()
        context = {
            'latest_cerpen_list':queryset
        }

        return context
    


def LoginView(request):
    form = FormLogin(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username_user = request.POST['username']
            password_user = request.POST['password']

            user = authenticate(request, username=username_user, password=password_user)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')

    return render(request, 'login.html', {'form':form})

def Logout(request):
    logout(request)
    request.session.flush()
    return redirect('login')