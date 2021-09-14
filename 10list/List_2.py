#添加列表元素
##1.使用append()方法在最后面添加元素
a = [1,2,'a',5.90,"牛马?"]
print("List:{},length:{}".format(a,len(a)))
a.append("hello")
print("List:{},length:{}".format(a,len(a)))

##2.insert()在指定位置插入
a.insert(1,"ins_here")
print("List:{},length:{}".format(a,len(a)))

##使用extend()方法将一个外部列表添加到本地列表后面
a.extend([1,"ex1","ex2"])
print("List:{},length:{}".format(a,len(a)))

##对两个列表进行+,会连接成新列表
b = ["b0","b1","b2"]
print(a+b)