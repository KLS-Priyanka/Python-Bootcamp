# multilevel inheritance

class Animal():
    def dog_speaks():
        return "im dog"
class dog(Animal):
    def barks():
        return "bow"
obj1=dog
print(obj1.barks())