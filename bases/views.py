from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, permission_required
from .models import Usuario
from .forms import Userform

# Create your views here.


class Home(LoginRequiredMixin, TemplateView):

    template_name = 'bases/home.html'
    login_url = 'config:login'


class UserLis(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "bases/users_list.html"
    login_url = 'config:login'
    model = Usuario
    permission_required = 'bases:view_usuario'
    context_object_name = 'obj'


@login_required(login_url='config:login')
@permission_required('bases.change_usarios', login_url='config:home')
def user_admin(request, pk=None):
    template_name = "bases/user_add.html"
    context = {}
    form = None
    obj = None
    if request.method == "GET":
        if not pk:
            form = Userform(instance=None)
        else:
            obj = Usuario.objects.filter(id=pk).first()
            form = Userform(instance=obj)
        context["form"] = form
        context["obj"] = obj
    if request.method == "POST":
        data = request.POST
        e = data.get("email")
        fn = data.get("first_name")
        ln = data.get("last_name")
        pw = data.get("password")
        if pk:
            obj = Usuario.objects.filter(id=pk).first()
            if not obj:
                print("Error Usuario No Existe")
            else:
                obj.email = e
                obj.first_name = fn
                obj.last_name = ln
                obj.password = make_password(pw)
                obj.save()
        else:
            obj = Usuario.objects.create_user(
                email=e,
                password=pw,
                first_name=fn,
                last_name=ln
            )
            print(obj.email, obj.password)
        return redirect('config:users_list')

    return render(request, template_name, context)
