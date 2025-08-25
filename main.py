class Doniko:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return self.name

D = Doniko('Daniel')
print(D.get_info())

class Umarchik:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return self.name

D = Umarchik('Umar')
print(D.get_info())