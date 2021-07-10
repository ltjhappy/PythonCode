class Dog():
    def __init__(self,name):
        self.name = name

    # del 在实例被销毁时，自动被调用
    def __del__(self):
        print("%s 被销毁了" % self.name)

    def __str__(self):
        return "我是小狗 %s" % self.name

    def eat(self):
        print("%s 在吃骨头" %self.name)


# d1 是一个全局变量, 创建类实例
d1 = Dog("小黄狗")

print(d1)