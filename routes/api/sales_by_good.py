from flask import Blueprint, render_template, request, redirect, url_for
from models import Order
import json
import operator
from .base import api_bp


@api_bp.route("/sales_by_good", methods=["GET"])
def number_of_usage_by_table():
    orders = Order.select()
    print("data", orders)
    l=[]
    sumprice=[]
    data=[]
    for order in orders:
        if(l.count(order.good.name)<=0):
            l.append(order.good.name)
            sumprice.append(float(order.good.price))
        
        sumprice[l.index(order.good.name)]=sumprice[l.index(order.good.name)]+float(order.good.price)

    for i in range(len(l)):
        data.append({'id':l[i],'sumprice':sumprice[i]})
    
    data2=sorted(data,key=operator.itemgetter('sumprice'),reverse=True)
    return json.dumps(data2,ensure_ascii=False)
