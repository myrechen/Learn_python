#...检测字符串构成
str0 = "hello,world!"
str1 = "HelloWorld"
str2 = "Hello,WoRld"
##isalpha():检测是否全部由字母构成
print(str0.isalpha())
print(str1.isalpha())

##isdigit():检测是否全由数字组成
##ifalnum():检测是否全由字母数字组成
##islower():检测字符串中字母是否全小写
print(str0.islower())
##isupper():
##istitle():判断字符串中各单词首字母是否大写,其它全为小写
print(str2.istitle())
#...

#...大小写转换,并不改变原来的字符串值
##upper(),lower():将字符串中所有字母转换
str0.upper()
print(str0.upper())
##capitalize():将字符串第一个字母变成大写,其余变成小写
print(str1.capitalize())

##title():将每个单词首字母大写,其余小写
str3 = "hELlo,WoRld"
print(str3.title())
#...

#...字符串替换replace()方法,本身并不改变字符串值
str1 = str1.replace("World","牛马?")
print(str1)
#...