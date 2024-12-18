from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer
import json

from .base import api_bp

@api_bp.route("/number_of_usage_by_table", methods=["GET"])
def number_of_usage_by_table():
    customers = Customer.select()
    print("data", customers)
    data = [{"id": customer.id, "table": customer.table} for customer in customers]
    return json.dumps(data)
