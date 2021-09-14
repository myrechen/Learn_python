#List的使用:素数筛法
n = int(input("输入素数筛上界:"))
#生成2~n的自然数构成的数表,转为List类型存放在列表a中
a = list(range(2,n+1))
i = 0
while(i < len(a)):
    j = i + 1
    while(j < len(a)):
        if(a[j]%a[i] == 0):
            #a[j]是a[i]的整数倍,则删除a[j]
            a.pop(j)
        else:
            j += 1

    i += 1
print("在2~%d之间有%d个质数:\n"%(n,len(a)))
print(a)