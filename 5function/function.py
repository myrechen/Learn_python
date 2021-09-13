#数据类型转换函数
#int(),float(),str(),bool()


#常用数学函数
##舍入round()
print("round(3.14) = ",round(3.14))
###保留两位小数
print("round(2.675,2) = ",round(2.675,2))
print("round(2.675+1e-9,2) = ",round(2.675+1e-9,2))

##绝对值abs()
print("abs(-3) = ",abs(-3))

##数学函数import math
import math
##向上取整ceil(),向下取整floor()
##平方根sqrt()
##角度转弧度radians()
##弧度转角度degrees()
##三角函数sin(),cos(),tan(),参数为弧度
##三角函数反函数asin(),acos(),atan(),返回值为弧度
print("sin 30° = ",math.sin(math.radians(30)))
print("arcsin 1 = ",math.degrees(math.asin(1)),"°")


#随机数random模块
import random
##随机生成指定范围整数randint(x,y),x <= y,[x,y]
print("random int(-4~3) = ",random.randint(-4,3))
##随机生成浮点数random(),[0~1)之间
##在指定范围生成浮点数uniform(x,y),[x,y)
print("random float[0~1) = ",random.random())
print("random float[-4~3) = ",random.uniform(-4,3))


#时间函数time模块
import time
##获取当前时间time(),返回一个浮点数
print("当前时间:",time.time())
###转换为时间元组
loctime = time.localtime(time.time())
print("本地时间:",loctime)
###格式化时间
localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)
###格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y年%m月%d日 %H:%M:%S 星期%w %A %B %Z", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2020"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

##程序暂停,以秒为单位
time.sleep(3)
print("sleep 3s")