# from django.views import generic
from django.http import JsonResponse

from .models import Payment
# from apps.categories.models import Categories
# from apps.courses.models import Courses
from django.shortcuts import render, redirect, get_object_or_404


def home_page(request):
    payments = Payment.objects.all()
    # categories = Categories.objects.only('name')
    return render(request, 'status/base.html', locals())


def ajax_add(request, ):
    name_payment = request.GET.get('name_payment')
    sum_payment = request.GET.get('sum_payment')
    status_payment = request.GET.get('status_payment')
    Payment.objects.create(name_payment=name_payment, sum_payment=sum_payment, status_payment=status_payment)
    return JsonResponse({})


def ajax_edit(request):
    number_payment = request.GET.get('number_payment')
    name_payment = request.GET.get('name_payment')
    date_payment = request.GET.get('date_payment')
    sum_payment = request.GET.get('sum_payment')
    status_payment = request.GET.get('status_payment')
    payment = Payment.objects.get(number_payment=number_payment)
    payment.name_payment = name_payment
    payment.date_payment = date_payment
    payment.sum_payment = sum_payment
    payment.status_payment = status_payment
    payment.save()
    return JsonResponse({})


def ajax_delete(request):
    number_payment = request.GET.get('number_payment')
    Payment.objects.filter(number_payment=number_payment).delete()
    return JsonResponse({})
