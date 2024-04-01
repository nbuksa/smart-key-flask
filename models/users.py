


class User:
    def __init__(self, first_name: str, last_name: str, pin_code: str, is_active: bool, id = None):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.pin_code = pin_code
        self.is_active = is_active

