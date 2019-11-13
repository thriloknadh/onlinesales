"""onlines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView, CreateView,ListView

from app import views
from app.models import MerchantModel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="login.html")),
    path('login/',views.Save.as_view(),name="login"),
    path('addmerchant/',CreateView.as_view(model=MerchantModel,fields=['Merchant_Name','Merchant_Email','Merchant_Contact'],template_name="addmerchant.html",success_url='/save/'),name="addmerchant"),
    path('save/',TemplateView.as_view(template_name="merchantsaved.html"),name="save"),
    path('viewmerchant/',ListView.as_view(model=MerchantModel,template_name="viewmerchant.html"),name="viewmerchant"),
    path('daywise/',TemplateView.as_view(template_name="daywise.html"),name="daywise"),
    path('weekwise/',TemplateView.as_view(template_name="weekwise.html"),name="weekwise"),
    path('monthwise/',TemplateView.as_view(template_name="monthwise.html"),name="monthwise"),
    path('yearwise/',TemplateView.as_view(template_name="yearwise.html"),name="yearwise")
 ]

