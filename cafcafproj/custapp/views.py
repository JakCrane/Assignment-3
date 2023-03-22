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
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
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

            order_items['item'].append(item_data)

            price = 0
            item_ids = []

            for item in order_items['item']:
                price += item['price']
                item_ids.append(item['id'])

            order = OrderModel.objects.create(price=price)
            order.items.add(*item_id)

            context = {
                'items': order_items['items'],
                'price': price,
            }

            return render(request, 'custapp/order_confirmation.html', context)