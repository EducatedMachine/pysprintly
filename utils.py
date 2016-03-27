def cache(operator):

    def inner_function(*args, **kwargs):
        print("Before")
        self = args[0]
        if self.is_caching and self.cached_values:
            print("Using cache")
            return self.cached_values

        value = operator(*args, **kwargs)
        print("Setting cache")
        self.cached_values = value
        print("After")
        return value

    return inner_function

