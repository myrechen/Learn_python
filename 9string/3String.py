#转义字符串
print("单引号',双引号\",反斜杠\\")

#读取字符串
##使用下标运算符[]
s = "abcdefg"
print(s[1])
##使用[start:end]读取
print(s[1:6])
print(s[2:])
print(s[:5])
##for...in语句遍历,省去计数器的使用
for ch in s:
    print(ch,end="")
##在字符串中查找子串,in操作符
state = ""
if("apple" in "banana,grape,apple,orange"):
    state = "找到"
    print("\n"+state)
##查找子串位置find()方法,未找到返回-1
print("banana,grape,apple,orange".find("apple"))
print("banana,grape,apple,orange".find("pen"))