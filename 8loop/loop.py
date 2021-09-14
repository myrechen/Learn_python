num = 1
sum = 0
i = 0
while i < 64:
    sum = sum + num * 2**i
    i = i + 1
print("麦子总数为:",sum)