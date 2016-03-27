from utils import cache
from models.product import Product

class Products:
    def __init__(self, connection, is_caching=True):
        self.conn = connection
        self.is_caching = is_caching
        self._cached_values = []

    @property
    @cache
    def all_products(self):
        status, value = self.conn.get("PRODUCTS")
        return value

    def create_product(self, product_name):
        return self.conn.post("PRODUCTS", data={"name": product_name})

    @cache
    def get_product(self, product_id):
        return self.conn.get("PRODUCT", fields=product_id)

    def update_product(self):
        pass

    def delete_product(self, product_id):
        return self.conn.delete("PRODUCT", fields=product_id)

    @property
    def cached_values(self):
        return self._cached_values

    @cached_values.setter
    def cached_values(self, raw_value):
        print("Setting")
        if type(raw_value) == list:
            for value in raw_value:
                self._cached_values.append(Product(value))
        elif type(raw_value) == dict:
            self._cached_values.append(Product(raw_value))


"""
    Fetch the information from the sprint.ly api
        If the information has already been retrieved do nothing
        and operate on the already existing data
        Else get the new information and add it to the cache
"""


