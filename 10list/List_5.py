#移除列表元素
a = [1,2,'a',5.90,"牛马?"]
##使用pop()方法,默认移除最后一个,指定pop(i)
print(a.pop())
print(a)

##使用remove()方法移除与目标值相匹配的第一个元素
b = [1,2,1,"a",'b','a']
b.remove(1)
b.remove('a')
print(b)

##clear(),清除列表中所有元素
a.clear()
print(a)