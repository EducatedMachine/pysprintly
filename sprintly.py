import requests
import json
import products
from requests.auth import HTTPBasicAuth


api_key = "4RZbU9XN7ZFcLdmfdqWA7rJBNELGrc5K"
username = "info@educatedmachine.com"

#   =====================================
#
#   BASE URLS
#
#   =====================================

BASE = "https://sprint.ly/api/"

URLS = {
    "BASE": BASE,
    "USER": BASE + "user/",
    "PRODUCTS": BASE + "products/",
}


class Sprintly:
    def __init__(self, email, api_key, cache_values=True):
        self.email = email
        self.api_key = api_key
        self.URLS = URLS
        self.cache_values = cache_values
        self.user = ""
        self.products = products.Products(self)

    def fetch(self, endpoint):
        pass

    @property
    def username(self):
        return self.email

    @property
    def auth(self):
        return HTTPBasicAuth(self.email, self.api_key)

    @property
    def user_id(self):
        return self.get_field("id")

    @property
    def first_name(self):
        return self.get_field("first_name")

    @property
    def last_name(self):
        return self.get_field("last_name")

    @property
    def created_at(self):
        return self.get_field("created_at")

    @property
    def last_login(self):
        return self.get_field("last_login")

    @property
    def user_details(self):
        endpoint = self.URLS["USER"] + "whoami.json"
        r = requests.get(endpoint, auth=self.auth)
        try:
            value = json.loads(r.text)
            self.user = (True, value)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def get_field(self, field_name):
        if self.cache_values:
            r = self.user or self.user_details
        else:
            r = self.user_details

        if not r[0]:
            return r[1]

        try:
            value = r[1]
            return value[field_name]
        except KeyError:
            return "Key error could not find {}".format(field_name)
