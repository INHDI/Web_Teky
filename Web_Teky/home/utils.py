import json
from .models import *


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0,
        'shipping': False,
    }
    cart_items = order['get_cart_items']

    for i in cart:
        try:
            cart_items += cart[i]["quantity"]

            product = SanPhamModel.objects.get(id=i)
            total = (product.gia * cart[i]["quantity"])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product': {
                    'id': product.id,
                    'name': product.ten,
                    'price': product.gia,
                    'imageURL': product.anh,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total,
            }
            items.append(item)

            if not product.digital:
                order['shipping'] = True

        except:
            pass

    return {'cart_items': cart_items, 'order': order, 'items': items}


def cart_data(request):
    cookie_data = cookie_cart(request)
    cart_items = cookie_data['cart_items']
    order = cookie_data['order']
    items = cookie_data['items']
    return {'cart_items': cart_items, 'order': order, 'items': items}
