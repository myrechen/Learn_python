#使用for...in遍历字典
##使用keys()方法获取一个字典中的所有键
d = {"name":"小明","age":12,"height":150.1,"weight":50.9}
print("keys()方法:")
for k in d.keys():
    print(k,d[k])

##使用values()方法获取字典中的所有值
print("\nvalues()方法:")
for v in d.values():
    print(v)

##使用items()方法获取字典中的键值对
print("\nitems()方法:")
for k,v in d.items():
    print(k,v)


#删除字典元素del语句
del d["age"]
print("\n删除age:")
for k in d.keys():
    print(k,d[k])

#清空字典元素
d.clear()
print(d)

#从内存中删除整个字典
del d
print(d)