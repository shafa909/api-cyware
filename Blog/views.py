from django.shortcuts import render
from .models import BlogPost
from django.utils.timezone import datetime
from datetime import date


def report_list_view(request):
	today   = date.today()
	year    = BlogPost.objects.filter(timestamp__year=today.year).count()
	month   = BlogPost.objects.filter(timestamp__month=today.month).count()
	today1  = BlogPost.objects.filter(timestamp__day=today.day).count()
	context = {
	'month' : month,
	'year'  : year ,
	'today1' : today1
	}
	return render(request,"report/list.html",context)

