from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *
# Create your views here.

class IndexView(View):
    def get(self,request):
        a = SanPhamModel.objects.all()
        c= LoaiSPModel.objects.all()
        return render(request, 'home/index.html',{'f':a,'danhmuc':c})

def loaisp(request,id):
    c= LoaiSPModel.objects.all()
    chitietsp = SanPhamModel.objects.all().filter(Loai_sp_id=id)
    return render(request, 'home/shop.html',{'f':chitietsp,'danhmuc':c})

def chitiet(request,id):
    c= LoaiSPModel.objects.all()
    chitietsp = SanPhamModel.objects.all().filter(id=id)
    return render(request,'home/product-single.html',{'f':chitietsp,'danhmuc':c})

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = OrderItem.objects.all()
    else:
        item = []
    context={'items':items,
             'order':order
             }
    return render(request,'home/cart.html',context)
