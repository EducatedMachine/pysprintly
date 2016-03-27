def cache(operator):

    def inner_function(*args, **kwargs):
        print("Before")
        value = operator(*args, **kwargs)
        print("After")
        return value

    return inner_function


class Products:
    def __init__(self, connection, cache_values=True):
        self.conn = connection
        self.cache_values = cache_values
        self.products = {}

    @property
    @cache
    def all_products(self):
        if self.products:
            return self.products

        status, value = self.conn.get("PRODUCTS")

        if status and self.cache_values:
            self.products = value

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


"""
    Fetch the information from the sprint.ly api
        If the information has already been retrieved do nothing
        and operate on the already existing data
        Else get the new information and add it to the cache
"""


