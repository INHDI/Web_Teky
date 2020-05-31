from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from .models import *
from .utils import cookie_cart
import json


# Create your views here.

class IndexView(View):
    def get(self, request):
        a = SanPhamModel.objects.all()
        c = LoaiSPModel.objects.all()
        return render(request, 'home/index.html', {'f': a, 'danhmuc': c})


def loaisp(request, id):
    c = LoaiSPModel.objects.all()
    chitietsp = SanPhamModel.objects.all().filter(Loai_sp_id=id)
    return render(request, 'home/shop.html', {'f': chitietsp, 'danhmuc': c})


def chitiet(request, id):
    c = LoaiSPModel.objects.all()
    chitietsp = SanPhamModel.objects.all().filter(id=id)
    return render(request, 'home/product-single.html', {'f': chitietsp, 'danhmuc': c})


def cart(request):
    data = cookie_cart(request)
    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }
    return render(request, 'home/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)
    return JsonResponse('Item was added', safe=False)
