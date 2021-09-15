#十进制转2进制
def DecToBin(num):
    if(num == 0):
        return
    else:
        DecToBin(num//2)
        print(num%2,end="")

def main():
    num = int(input("输入十进制整数:"))
    DecToBin(num)

#如果此文件被其他文件调用,下面代码不会执行
if __name__ == '__main__':
    main()