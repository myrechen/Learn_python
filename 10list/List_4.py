#在列表中查找元素
##in 或者 not in 运算符
a = [1,2,'a',5.90,"牛马?"]
print(3 in a)
print(3 not in a)

##index()方法找出第一个匹配的下标
print(a.index('a'))

##列表存在重复元素,使用循环将其全部找出
fruits = ["apple","banana","grape","orange","banana"]
for i,v in enumerate(fruits):
    if(v == "banana"):
        print(i,v)

##使用max(),min()方法从列表中查找最大最小值
scores = [80,20,50,10,90,30]
print("最大值:",max(scores))
print("最小值:",min(scores))

#使用sum()对列表中各元素求和
print("总和:",sum(scores))