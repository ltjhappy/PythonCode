# python 推荐使用 纯小写加下划线的方式做变量名
alex_of_age = 19
name = "ucs"
print(name)
x = 100
wu = x
xf = x
del (x)
# print(x)
print(wu)
国家 = "Korea"
print(国家)
# id 反映的是变量值的内存地址，内存地址不同id则不同
print(id(alex_of_age))
# type 不同类型的值用来表示记录不同的状态
print(type(alex_of_age))

x1 = "-9"
y1 = "-9"
print(id(x1))
print(id(y1))
x2 = 'algorithm,898989:,os'
y2 = 'algorithm,898989:,os'
print(id(x2),id(y2))

# is: 比较两个值身份id是否相等
# ==: 比较左右两个值他们的值是否相等

