# method overwriting
class animal():
    def speaks():
        return "barking"
class dog(animal):
    def speaks():
        return "im barking"
class puppy(dog):
    def speaks():
        return "it is barking"
obj1=puppy
print(obj1.speaks())