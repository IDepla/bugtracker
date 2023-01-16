import logging

# pylint: disable=no-member
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import TemplateView, DetailView, View
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import List, Dict, Any
from django.core.paginator import Paginator
from .models import Bug, User
from .forms import PaginatorForm, UserUpdateNameForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from datetime import datetime

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
        bugs = Bug.get_open_bugs_by_date_reverse()
        paginator = Paginator(bugs, 20)
        page_number = 1

        if self.request.GET.get("page"):
            form = PaginatorForm(self.request.GET)
            if form.is_valid():
                page_number = form.cleaned_data["page"]
            else:
                logging.getLogger().warning(
                    "bug-list page non numeric. user %s",
                    self.user,
                )
        context["page_obj"] = paginator.get_page(page_number)

        return context


class CreateBug(LoginRequiredMixin, CreateView):
    """create a bug"""
    model = Bug
    fields = ["title", "description", "assigned_to"]

    def get_success_url(self):
        return reverse('bug-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        # do something with self.object
        return HttpResponseRedirect(self.get_success_url())


class CloseBug(LoginRequiredMixin, View):
    """closes a bug and renders to the open bugs page"""
    model = Bug

    def get(self, request, *args, **kwargs):
        """closes a bug"""
        bug = get_object_or_404(Bug, pk=self.kwargs["pk"])
        bug.status = Bug.BugStatus.CLOSE
        bug.closed_by = self.request.user
        bug.closed_at = datetime.now()
        bug.save()

        #return redirect(reverse("bug-detail", kwargs={"pk": self.kwargs["pk"]}))
        return redirect(reverse("open-bugs"))



class BugDetail(LoginRequiredMixin, DetailView, UpdateView):
    """bug page, with all details."""

    model = Bug
    template_name = "web/bug-detail.html"
    fields = ["title","description","assigned_to"]

    def get_success_url(self):
        return reverse('bug-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if self.object.status == Bug.BugStatus.OPEN:
            self.object = form.save(commit=True)
            
        return HttpResponseRedirect(self.get_success_url())

class AccountPage(LoginRequiredMixin, DetailView, View):
    """user account page"""

    model = User
    template_name = "web/account-page.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        user = User.get_complete(self.kwargs["pk"])

        if user.pk == self.request.user.pk:
            form = UserUpdateNameForm()
            form.fields["first_name"].initial = user.first_name
            form.fields["last_name"].initial = user.last_name
            context["form"] = form
        # Add in a QuerySet of all the books
        context["assigned_bugs_list"] = user.bugs_assigned.all()
        context["created_bugs_list"] = user.bugs_created.all()
        context["user"] = user

        return context

    def post(self, request, *args, **kwargs):
        """patch the user name and surname"""
        user = User.get_complete(self.kwargs["pk"])
        form = UserUpdateNameForm(request.POST)
        if user.pk == self.request.user.pk and form.is_valid():

            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()

        return redirect(reverse("account-detail", kwargs={"pk": self.request.user.pk}))
