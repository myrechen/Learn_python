#创建访问字典元素
##1.使用{}创建字典
d = {"name":"Alan","age":9,"height":100}
print(len(d))
##2.以变量名[键名]的形式访问,键名不存在会报错
print(d["name"])
##3.使用get()方法安全访问字典
print(d.get("weight"))
print(d.get("weight","无"))


#添加或修改元素
##字典名[键名] = 元素值添加新元素,如果键名已存在,则进行修改操作
d["weight"] = 50
print(d)
d["age"] = 10
print(d)
