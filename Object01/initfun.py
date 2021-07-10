
class Dog():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s 在吃骨头" %self.name)

    print("类语句")

d1 = Dog("小黄狗")
print(d1.name)
d1.eat()
