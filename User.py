class User:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name

    def get_age(self, current_year: int):
        return current_year - self.birth_year

