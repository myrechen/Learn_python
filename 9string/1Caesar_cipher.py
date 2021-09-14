#凯撒密码:加密和解密
#循环运行
go_on = True
while(go_on):
    #选择运行方式,并输入信息
    print("选择程序功能:\n1:加密\n2:解密")
    choose = input("输入1或2:")
    s = ""
    i = 0
    if(choose == '1'):
        text = input("请输入明文:")
        while(i < len(text)):
            c = text[i]
            if('a' <= c <= 'w' or 'A' <= c <= 'W'):
                c = chr(ord(c) + 3)
            elif('x' <= c <= 'z' or 'X' <= c <= 'Z'):
                c = chr(ord(c) - 23)
            else:
                c = str(c)
            s = s + c
            i += 1
        print("输出密文:"+s)

    elif(choose == '2'):
        text = input("请输入密文:")
        while(i < len(text)):
            c = text[i]
            if('d' <= c <= 'z' or 'D' <= c <= 'Z'):
                c = chr(ord(c) - 3)
            elif('a' <= c <= 'c' or 'A' <= c <= 'C'):
                c = chr(ord(c) + 23)
            else:
                c = str(c)
            s = s + c
            i += 1
        print("输出明文:"+s)

    else:
        print("错误的选择!")
    
    choose1 = input("是否继续运行?(Y:继续, N:结束):")
    if(choose1 != 'Y' and choose1 != 'y'):
        print("程序退出...")
        go_on = False