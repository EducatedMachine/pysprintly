import requests
import json
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

    def __init__(self, email, api_key):
        self.email = email
        self.api_key = api_key
        self.URLS = URLS

    @property
    def username(self):
        return self.email

    @property
    def auth(self):
        return HTTPBasicAuth(self.email, self.api_key)

    @property
    def user_id(self):
        endpoint = self.URLS["USER"] + "whoami.json"
        r = requests.get(endpoint, auth=self.auth)
        try:
            value = json.loads(r.text)
            return value["id"]
        except TypeError:
            return "Problem getting the ID, incorrectly formatted json"
        except KeyError:
            return "Key error could not find ID"

    @property
    def user_details(self):
        endpoint = self.URLS["USER"] + "whoami.json"
        r = requests.get(endpoint, auth=self.auth)
        return r.json()




