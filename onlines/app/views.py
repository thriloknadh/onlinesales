from django.shortcuts import render


from django.views import View

from app.models import AdminModel


class Save(View):
   def post(self,request):
       username=request.POST.get("t1")
       passwd=request.POST.get("t2")
       AdminModel(uname=username,passwd=passwd).save()
       return render(request,"welcome.html")