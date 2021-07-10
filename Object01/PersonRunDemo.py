class Person:
    def __init__(self,name,weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重 %.2f斤" %(self.name,self.weight)

    def run(self):
        print("%s爱跑步,跑步锻炼身体"% self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s在吃大餐，吃了再减肥." % self.name)
        self.weight += 3

xiao_ming = Person("王小明",130)

xiao_ming.run()
xiao_ming.eat()
print(xiao_ming)