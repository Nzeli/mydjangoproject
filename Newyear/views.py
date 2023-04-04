from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.



def new(request):
     now = datetime.datetime
     return render (request, "index.html",{
         "now": now. month == 1 and now.day == 1

     })



