from .api.number_of_usage_by_table import api_bp
from .api.sales_by_day import api_bp
from .api.sales_by_good import api_bp
from .api.sales_per_customer import api_bp

from .customer import customer_bp
from .goods import goods_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [customer_bp, goods_bp, order_bp, api_bp]
