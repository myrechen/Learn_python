#元组Tuple,只读列表
#使用()创建元组
a = (1,2,'a',5.90,"牛马?")
print(a[4])

#tuple()函数将列表转成元组
b = [9,8,7]
c = tuple(b)
#未改变b的列表属性
print(b)
print(c)