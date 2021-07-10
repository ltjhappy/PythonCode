
stu_info = [{'name':'陈心怡','age':18,'sex':'女'},
            {'name':'艾春伶','age':22,'sex':'女'},
            {'name':'陈佩文','age':21,'sex':'女'}]

# 列表【】，字典【key】
print(stu_info[2]['name'])

if 10:
    print("yes")

# not
13 > 10
print(not 13>10)

# and  逻辑与

if 13>10 and 0 > -5 :
    print("条件满足yes")
else:
    print("no")

# 优先级  not > and > or

condition = (3>4 and not 4>3 or 1==3 and 'x'=='x' or 3>3)
print("Condition结果是: ",condition)