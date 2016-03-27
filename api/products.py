class Products:

    def __init__(self, connection, cache_values=True):
        self.conn = connection
        self.cache_values = cache_values

    @property
    def all_products(self):
        return self.conn.get("PRODUCTS")

    def create_product(self, product_name):
        return self.conn.post("PRODUCTS", data={"name": product_name})

    def get_product(self, product_id):
        return self.conn.get("PRODUCT", fields=product_id)

    def update_product(self):
        pass

    def delete_product(self, product_id):
        return self.conn.delete("PRODUCT", fields=product_id)

