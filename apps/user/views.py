from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, TemplateView

from apps.user.form import UserCreateForm, LoginForm
from apps.user.models import User


# Create your views here.
def home(request):
    return HttpResponse("hello 'mr.Rajat Saini'")



class Sign(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = '/login_view'

    def form_valid(self, form):
        # Hash password using make_password() function
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)


class Login(View):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'home'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        print(email)
        print(password)
        print(user.email)
        if user is not None:
            print("Enter User")
            authenticated_user = authenticate(request, email=user.email, password=password)
            print(authenticated_user)
            if authenticated_user is not None:
                print("Login Successful")
                login(request, authenticated_user)
                context = {
                    'user_email': authenticated_user.email,
                    'user_first_name': authenticated_user.first_name,
                    'user_last_name': authenticated_user.last_name,
                }
                return render(request, 'home.html', context)
            else:
                messages.error(request, 'Authentication failed. Please check your credentials.')
        else:
            print("Invalid Credentials")
            messages.error(request, 'User with this email does not exist.')

        return render(request, self.template_name, {'form': self.form_class})



class HomeView(TemplateView):
    template_name = 'home.html'

def logout_view(request):
    print(11)
    logout(request)
    return redirect('login_view')