#输出100以内的素数

i = 2
count = 0
while i <= 100:
    j = 2
    flag = 1
    while j <= i/2:
        if i % j == 0:
            #不是素数
            flag = 0
            break
        else:
            j = j + 1
    if flag:
        if(count == 5):
            print(i)
            count = 0
        else:
            print("%2d"%i,end=" ")
            count += 1
    i = i + 1