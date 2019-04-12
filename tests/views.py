# coding: utf-8

from django.http.response import JsonResponse


def fail_view(request):
    9 / 0
    return JsonResponse({'status': True})


def success_view(request):
    return JsonResponse({'status': True})
