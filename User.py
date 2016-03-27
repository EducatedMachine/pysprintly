class User:

    def __init__(self, connection, cache_values=True):
        self.conn = connection
        self.user = ""
        self.cache_values = cache_values

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
        return self.user or self.conn.fetch("USER")

    def get_field(self, field_name):
        if self.cache_values:
            r = self.user or self.conn.get("USER")
        else:
            r = self.conn.get("USER")

        if not r[0]:
            return r[1]

        try:
            value = r[1]
            return value[field_name]
        except KeyError:
            return "Key error could not find {}".format(field_name)
