#创建列表和访问列表元素
##1.使用[]创建空列表
a = []
print("List:{},length:{}".format(a,len(a)))
##2.创建的同时添加元素
b = [1,2,'a',5.90,"牛马?"]
print("List:{},length:{}".format(b,len(b)))
##3.使用下标访问和[start:end]访问子列表
print(b[4])
print(b[1:])