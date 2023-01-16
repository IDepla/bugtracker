"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.urls import urlpatterns as api_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    Landingpage,
    OpenBugs,
    BugDetail,
    AccountPage,
    CreateBug,
    CloseBug,
)

urlpatterns = api_urlpatterns + [
    path("admin/", admin.site.urls),
    path("open/", OpenBugs.as_view(), name="open-bugs"),
    path("bug/create/", CreateBug.as_view(), name="bug-create"),
    path("bug/<int:pk>/", BugDetail.as_view(), name="bug-detail"),
    path("bug/<int:pk>/close/", CloseBug.as_view(), name="bug-close"),
    path("account/<int:pk>/", AccountPage.as_view(), name="account-detail"),
    path(
        "account/login/",
        LoginView.as_view(template_name="web/landing.html"),
        name="login",
    ),
    path(
        "account/logout/",
        LogoutView.as_view(template_name="web/landing.html"),
        name="logout",
    ),
    path("", Landingpage.as_view(), name="home"),
]
