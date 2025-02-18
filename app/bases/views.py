from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
# Create your views here.

class Home(LoginRequiredMixin, generic.TemplateView):
    # template_name = "base/base.html"
    template_name = "bases/home.html"
    login_url = 'bases:login'#'/admin'

class HomeSinPrivilegios(generic.TemplateView):
    template_name = "bases/sin_privilegios.html"
    
class SinPrivilegios(PermissionRequiredMixin):
    raise_exception = False
    redirect_field_name = "redirect_to"
    def handle_no_permission(self): # this can be used to redirect to a 404/403 forbidden page
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = "bases:sin_privilegios"
            
        return HttpResponseRedirect(reverse_lazy(self.login_url))
        
        """
        if self.request.user.is_authenticated:
            return render(self.request, "bases/403.html", status=403)
        else:
            return redirect(self.get_login_url())
        """
    