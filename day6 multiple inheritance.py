# multiple inheritance

class father():
    def father_s():
        return "im fit"
class mother():
    def mother_s():
        return "im healthy"
class kid(father,mother):
    def kid_s():
        return "i have inheritance of father and mother"
obj1=kid
print(obj1.kid_s())