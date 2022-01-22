#Using __class__.__name__
class Class_name:
    def name(self, name):
        return name


V = Class_name()
print(V.__class__.__name__)

#Using type() and __name__ attribute
class Class_name:
    def name(self, name):
        return name


V = Class_name()
print(type(V).__name__)

