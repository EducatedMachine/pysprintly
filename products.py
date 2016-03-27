import requests
import json

class Products:

    def __init__(self, sprintly):
        self.sprintly = sprintly

    @property
    def products(self):
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

