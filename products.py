import requests
import json

class Products:

    def __init__(self, sprintly):
        self.sprintly = sprintly

    @property
    def all_products(self):
        endpoint = self.sprintly.URLS["BASE"] + "products.json"
        r = requests.get(endpoint, auth=self.sprintly.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def create_product(self, product_name):
        endpoint = self.sprintly.URLS["BASE"] + "products.json"
        r = requests.post(endpoint, data={"name": product_name}, auth=self.sprintly.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def get_product(self, product_id):
        pass

    def update_product(self):
        pass

    def delete_product(self):
        pass

