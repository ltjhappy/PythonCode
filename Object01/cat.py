class Cat:
    def eat(self):
        print("%s 小猫在吃饭." % self.name)

    def drink(self):
        print("%s 小猫在喝茶" % self.name)


# 创建实例
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
# 在类外面给实例添加属性 ， 不推荐

# 输出实例变量 , 16进制
print(tom)

# 输出 实例 在内存中的地址
address = id(tom)
print(address) # 10进制
print("%x"% address) # 16进制