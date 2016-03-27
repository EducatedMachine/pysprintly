import requests
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

BASE_ENDPOINT = "https://sprint.ly/api/"
PRODUCTS_ENDPOINT = BASE_ENDPOINT + "products.json"
PRODUCTS_BASE_ENDPOINT = BASE_ENDPOINT + "products/"
PRODUCT_ENDPOINT = PRODUCTS_BASE_ENDPOINT + "{0}.json"

ITEMS_ENDPOINT = PRODUCTS_BASE_ENDPOINT + "{0}/items.json"


def get_user_ID(username, api_key):
    return requests.get("https://sprint.ly/api/user/whoami.json", auth=HTTPBasicAuth(username, api_key))


def get_all_products(username, api_key):
    return requests.get(PRODUCTS_ENDPOINT, auth=HTTPBasicAuth(username, api_key))

def create_product(product_name, username, api_key):
    return requests.post(PRODUCTS_ENDPOINT, data={"name": product_name}, auth=HTTPBasicAuth(username, api_key))

def update_product():
    pass

def get_product():
    pass

def archive_product(product_id, username, api_key):
    endpoint = PRODUCT_ENDPOINT.format(product_id)
    return requests.delete(endpoint, auth=HTTPBasicAuth(username, api_key))

def get_items(product_id, username, api_key):
    endpoint = ITEMS_ENDPOINT.format(product_id)
    return requests.get(endpoint, auth=HTTPBasicAuth(username, api_key))

# all_products = get_all_products(username, api_key).json()
# print(all_products)
#
# created_product = create_product("Devops", username, api_key)
# print(created_product.json())
# archive_product = archive_product(40472, username, api_key)
# print(archive_product.json())
#
# items = get_items(37771, username, api_key)
# print(items.json())

if __name__ == "__main__":
    pass
    print(URLS["USER"])
    print(URLS["BASE"])
