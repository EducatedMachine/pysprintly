import requests
import json
import products
import user
from requests.auth import HTTPBasicAuth

#   =====================================
#
#   API ENDPOINT URLS
#
#   =====================================

URLS = {
    "BASE_API_ENDPOINT": "https://sprint.ly/api/",
    "USER": "user/whoami.json",
    "PRODUCTS": "products/",

    "ITEMS": "products/{product_id}/items.json",
    "ITEM": "products/{product_id}/items/{item_number}.json",
    "ITEM_CHILDREN": "products/{product_id}/items/{item_number}/children.json",

    "TAGS": "products/{product_id}/tags.json",
    "TAG": "products/{product_id}/tags/{tag_name}.json",

    "ATTACHMENTS": "products/{product_id}/items/{item_number}/attachments.json",
    "ATTACHMENT": "products/{product_id}/items/{item_number}/attachments/{attachment_id}.json",

    "BLOCKS": "products/{product_id}/items/{item_number}/blocking.json",
    "BLOCK": "products/{product_id}/items/{item_number}/blocking/{block_id}.json",

    "COMMENTS": "products/{product_id}/items/{item_number}/comments.json",
    "COMMENT": "products/{product_id}/items/{item_number}/comments/{comment_id}.json",

    "DEPLOYS": "products/{product_id}/deploys.json",

    "FAVOURITES": "products/{product_id}/items/{item_number}/favorites.json",
    "FAVOURITE": "products/{product_id}/items/{item_number}/favorites/{favorite_id}.json",

    "PEOPLE": "products/{product_id}/people.json",
    "PERSON": "products/{product_id}/people/{user_id}.json",

    "PULL_REQUESTS": "products/{product_id}/pullrequests.json",
    "PULL_REQUEST": "products/{product_id}/pullrequests/{pull_request_number}.json",
}


class Connection:

    def __init__(self, email, api_key, cache_values=True):
        self.email = email
        self.api_key = api_key
        self.URLS = URLS
        self.cache_values = cache_values
        self.user = ""
        self.products = products.Products(self)
        self.user = user.User(self)

    def get(self, URL):
        endpoint = self.build_url(URL)
        r = requests.get(endpoint, auth=self.auth)
        try:
            value = json.loads(r.text)
            self.user = (True, value)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def post(self, URL, data):
        pass

    def delete(self, URL, data):
        pass

    def build_url(self, URL, fields):
        return self.URLS["BASE_API_ENDPOINT"] + self.URLS[URL]

    @property
    def username(self):
        return self.email

    @property
    def auth(self):
        return HTTPBasicAuth(self.email, self.api_key)

