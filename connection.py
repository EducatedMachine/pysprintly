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
    "ATTACHMENTS": "products/{product_id}/items/{item_number}/attachments.json",
    "ATTACHMENT": "products/{product_id}/items/{item_number}/attachments/{attachment_id}.json",

    "BASE_API_ENDPOINT": "https://sprint.ly/api/",

    "BLOCKS": "products/{product_id}/items/{item_number}/blocking.json",
    "BLOCK": "products/{product_id}/items/{item_number}/blocking/{block_id}.json",

    "COMMENTS": "products/{product_id}/items/{item_number}/comments.json",
    "COMMENT": "products/{product_id}/items/{item_number}/comments/{comment_id}.json",

    "DEPLOYS": "products/{product_id}/deploys.json",

    "FAVOURITES": "products/{product_id}/items/{item_number}/favorites.json",
    "FAVOURITE": "products/{product_id}/items/{item_number}/favorites/{favorite_id}.json",

    "ITEMS": "products/{product_id}/items.json",
    "ITEM": "products/{product_id}/items/{item_number}.json",
    "ITEM_CHILDREN": "products/{product_id}/items/{item_number}/children.json",

    "PEOPLE": "products/{product_id}/people.json",
    "PERSON": "products/{product_id}/people/{user_id}.json",

    "PRODUCTS": "products/",
    "PRODUCT": "products/{product_id}.json",

    "PULL_REQUESTS": "products/{product_id}/pullrequests.json",
    "PULL_REQUEST": "products/{product_id}/pullrequests/{pull_request_number}.json",

    "TAGS": "products/{product_id}/tags.json",
    "TAG": "products/{product_id}/tags/{tag_name}.json",

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

    def get(self, URL):
        endpoint = self.build_url(URL)
        r = requests.get(endpoint, auth=self.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def post(self, URL, data):
        endpoint = self.build_url(URL)
        r = requests.post(endpoint, data=data, auth=self.auth)
        try:
            value = json.loads(r.text)
            return True, value
        except TypeError:
            return False, "Error returning value, incorrect JSON format"

    def delete(self, URL, data):
        pass

    def build_url(self, URL):
        return self.URLS["BASE_API_ENDPOINT"] + self.URLS[URL]

    @property
    def auth(self):
        return HTTPBasicAuth(self.username, self.api_key)

if __name__ == "__main__":
    import config as c
    conn = Connection(c.username, c.api_key, cache_values=True)
    print(conn.user.last_name)
    print(conn.user.first_name)
    print(conn.user.created_at)

