from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        pass