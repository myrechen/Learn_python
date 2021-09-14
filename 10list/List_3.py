#用for...in语句遍历列表
a = [1,2,'a',5.90,"牛马?"]
for x in a:
    print(x,end=" ")
print("\n")

#与enumerate()函数结合,同时列出元素下标和值
for i,v in enumerate(a):
    print(i,v,end=" , ")
print("\n")

#与range()函数结合遍历
for i in range(len(a)):
    print(i,a[i])