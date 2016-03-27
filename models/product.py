class Product:

    def __init__(self, product_json):
        self.raw = product_json

    @property
    def admin(self):
        return self.raw["admin"]

    @property
    def archived(self):
        return self.raw["archived"]

    @property
    def created_at(self):
        return self.raw["created_at"]

    @property
    def email(self):
        return self.raw["email"]

    @property
    def id(self):
        return self.raw["id"]

    @property
    def name(self):
        return self.raw["name"]

    @property
    def webhook(self):
        return self.raw["webhook"]

