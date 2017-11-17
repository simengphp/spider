class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_detail(self):
        return self.name, self.age

liuzhu = Foo('liuzhu', '19')
print liuzhu.get_detail()[0]