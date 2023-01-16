from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import List, Dict, Any


class Landingpage(TemplateView):
    """Landing page, shows login, or redirects to open bugs"""

    template_name = "web/landing.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("open")
        return super().get(request, *args, **kwargs)


class OpenBugs(LoginRequiredMixin, TemplateView):
    """open bugs, show list of open bugs"""

    template_name = "web/bug-list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class BugDetail(LoginRequiredMixin, TemplateView):
    """bug page, with all details."""

    template_name = "web/bug-detail.html"
    


class AccountPage(LoginRequiredMixin, TemplateView):
    """user account page"""

    template_name = "web/account-page.html"
