import json
import requests
from requests.auth import HTTPBasicAuth

from api import user
from api import products

#   =====================================
#
#   API ENDPOINT URLS
#
#   List of URL Endpoints, the items are arranged alphabetically
#   =====================================

URLS = {
    # Fields: product_id, item_number
    "ATTACHMENTS": "products/{}/items/{}/attachments.json",
    # Fields: product_id, item_number, attachment_id
    "ATTACHMENT": "products/{}/items/{}/attachments/{}.json",

    "BASE_API_ENDPOINT": "https://sprint.ly/api/",

    # Fields: product_id, item_number
    "BLOCKS": "products/{}/items/{}/blocking.json",
    # Fields: product_id, item_number, block_id
    "BLOCK": "products/{}/items/{}/blocking/{}.json",

    # Fields: product_id, item_number
    "COMMENTS": "products/{}/items/{}/comments.json",
    # Fields: product_id, item_number, comment_id
    "COMMENT": "products/{}/items/{}/comments/{}.json",

    # Fields: product_id
    "DEPLOYS": "products/{}/deploys.json",

    # Fields: product_id, item_number
    "FAVOURITES": "products/{}/items/{}/favorites.json",
    # Fields: product_id, item_number, favorite_id
    "FAVOURITE": "products/{}/items/{item_number}/favorites/{}.json",

    # Fields: product_id
    "ITEMS": "products/{}/items.json",
    # Fields: product_id, item_number
    "ITEM": "products/{}/items/{}.json",
    # Fields: product_id, item_number
    "ITEM_CHILDREN": "products/{}/items/{}/children.json",

    # Fields: product_id
    "PEOPLE": "products/{}/people.json",
    # Fields: product_id, user_id
    "PERSON": "products/{}/people/{}.json",

    "PRODUCTS": "products.json",
    # Fields: product_id
    "PRODUCT": "products/{}.json",

    # Fields: product_id
    "PULL_REQUESTS": "products/{}/pullrequests.json",
    # Fields: product_id, pull_request_number
    "PULL_REQUEST": "products/{}/pullrequests/{}.json",

    # Fields: product_id
    "TAGS": "products/{}/tags.json",
    # Fields: product_id, tag_name
    "TAG": "products/{}/tags/{tag_name}.json",

    "USER": "user/whoami.json",
}


class Connection:

    def __init__(self, username, api_key, cache_values=True):
        self.username = username
        self.api_key = api_key
        self.URLS = URLS
        self.cache_values = cache_values
        self.user = ""
        self.products = products.Products(self, cache_values)
        self.user = user.User(self, cache_values)

    def get(self, URL, fields=""):
        endpoint = self.build_url(URL, fields)
        r = requests.get(endpoint, auth=self.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def post(self, URL, data="", fields=""):
        endpoint = self.build_url(URL, fields)
        r = requests.post(endpoint, data=data, auth=self.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def delete(self, URL, data="", fields=""):
        endpoint = self.build_url(URL, fields)
        r = requests.delete(endpoint, data=data, auth=self.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def build_url(self, URL, fields=""):
        url = self.URLS["BASE_API_ENDPOINT"] + self.URLS[URL].format(*fields)
        print(url)
        return url

    @property
    def auth(self):
        return HTTPBasicAuth(self.username, self.api_key)

if __name__ == "__main__":
    import config as c
    conn = Connection(c.username, c.api_key, cache_values=True)
    print(conn.products.delete_product(["40054",]))

