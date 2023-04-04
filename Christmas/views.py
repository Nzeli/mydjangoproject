
from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.



def yaas(request):
     now = datetime.datetime.now()
     return render (request, "index.html",{
         "now": now. month == 12 and now.day == 25

     })
