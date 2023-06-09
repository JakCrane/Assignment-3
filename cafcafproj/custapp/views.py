from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel
import json


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        wraps = MenuItem.objects.filter(
            category__name__contains='Wraps')
        nibbles = MenuItem.objects.filter(category__name__contains='Nibbles')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        soups = MenuItem.objects.filter(category__name__contains='Soup')

        context = {
            'wraps': wraps,
            'nibbles': nibbles,
            'drinks': drinks,
            'soups': soups,
        }

        return render(request, 'custapp/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            postcode=postcode,
            )
        order.items.add(*item_ids)

        body = ("Thankyou for your order."
                "Your food is being made and will be delivered soon!"
                f'Your total: {price}\n'
                'Cheers')

        send_mail(
            "Thankyou for your order",
            body,
            'example@example.com',
            [email],
            fail_silently=False,
        )

        context = {
            'items': order_items['items'],
            'price': price,
        }

        return redirect('order_confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items.all(),
            'price': order.price,
        }

        return render(request, 'custapp/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment_confirmation')


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/order_pay_confirmation.html')


class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
          'menu_items': menu_items,
        }

        return render(request, 'custapp/menu.html', context)


class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query)
        )
        context = {
          'menu_items': menu_items,
        }
        return render(request, 'custapp/menu.html', context)
