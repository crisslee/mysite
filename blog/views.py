from django.shortcuts import render
from django.http import HttpResponse

'''响应客户请求返回html页面'''
# Create your views here.

def index(request):
    return HttpResponse('Hello,world');