#自定义函数

#卡普类卡尔常量
#四位不完全相同的整数,最大排列-最小排列=差值,重复多次得到6174

#主程序
def main():
    n = input("请输入各位数字不完全相同的四位整数:")
    if check(n):
        blackhole(n)
    else:
        print("错误的输入!")

#输入检测
def check(n):
    if(not n.isnumeric()):
        return False
    elif(len(n) != 4):
        return False
    elif(n == n[0]*4):
        return False
    else:
        return True

#排列大数
def max_number(a):
    a.sort(reverse = True)
    num = int("".join(a))
    return num

#排列小数
def min_number(a):
    a.sort()
    num = int("".join(a))
    return num

#黑洞变换
def blackhole(n):
    print("变换过程:")
    while(n != "6174"):
        a = list(n)
        b = max_number(a)
        c = min_number(a)
        n = str(b - c)
        print("%s - %s = %s"%(b,c,n))

    print("变换结束")

#程序入口
if __name__ == '__main__':
    main()

##写在最后:
##当运行单个python文件时，如运行a.py，这个时候a的一个属性__name__是__main__n+
##当调用某个python文件时，如b.py调用a.py，这个时候a的属性__name__是模块名a