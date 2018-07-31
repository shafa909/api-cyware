from django.shortcuts import render
from .models import UserPost
from django.utils.timezone import datetime
from datetime import date


def report_list_view(request):
	today   = Userdate.today()
	year    = UserPost.objects.filter(timestamp__year=today.year).count()
	month   = UserPost.objects.filter(timestamp__month=today.month).count()
	today1  = UserPost.objects.filter(timestamp__day=today.day).count()
	context = {
	'month' : month,
	'year'  : year ,
	'today1' : today1
	}
	return render(request,"report/list.html",context)

