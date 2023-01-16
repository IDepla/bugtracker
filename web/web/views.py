from django.views.generic import TemplateView


class Landingpage(TemplateView):
    template_name = "web/landing.html"


class OpenBugs(TemplateView):
    template_name = "web/bug-list.html"


class BugDetail(TemplateView):
    template_name = "web/bug-detail.html"


class AccountPage(TemplateView):
    template_name = "web/account-page.html"
