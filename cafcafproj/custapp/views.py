from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'custapp/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = MenuItem.objects.filter(
            category__name__contains='Appetizer')
        entrees = MenuItem.objects.filter(category__name__contains='Entree')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')

        context = {
            'appetizers': appetizers,
            'entrees': entrees,
            'drinks': drinks,
            'desserts': desserts,
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

        body = ("Thankyou for your order. Your food is being made and will be delivered soon!"
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
    
    def post(self, request, *args, **kwargs):
        print(request.body)

class OrderPayConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, 'custapp/order_pay_confirmation.html')