class Dog():
    def __init__(self,name):
        self.name = name

    # del 在实例被销毁时，自动被调用
    def __del__(self):
        print("%s 被销毁了" % self.name)

    def eat(self):
        print("%s 在吃骨头" %self.name)

    print("类语句")
# d1 是一个全局变量
d1 = Dog("小黄狗")
print(d1.name)
d1.eat()

del d1 # 对象销毁时会调用 __del__ 方法
print("-"*50)