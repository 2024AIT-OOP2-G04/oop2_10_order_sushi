from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer
from models import Order
from models import Goods
import json

from .base import api_bp

@api_bp.route("/sales_per_customer", methods=["GET"])
def get_sales_per_customer():

    # データベースから客のidの紐付けリストを取得
    customers = Customer.select()

    # 配列に整理
    customers_array = [{"id": customer.id, "table": customer.table} for customer in customers]

    data = []
    for customer in customers_array:##客の数だけforループ

        customer_id = customer["id"]
        # その客に合致する注文のリストを表示
        orders = Order.select().where(Order.customer == customer_id)
        total_sales = 0

        for order in orders:## 商品の値段をループで取得
            good = Goods.get_or_none(Goods.id == order.good)
            if good:
                total_sales += int(good.price)
        data.append({"id": customer_id, "total_sales": total_sales})

    return json.dumps(data)
