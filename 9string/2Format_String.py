#1.使用%占位符格式化
print("1.使用%占位符格式化")
name = "小明"
age = 9
height = 100
print("%s今年%d岁,身高%.2fcm"%("小明",age,height))

#2.使用format方法格式化
print("2.使用format方法格式化")

print("(1).使用空{}作为占位符:")
print("{}今年{}岁,身高{}cm".format("小明",age,height))

print("(2).使用带编号的{}作为占位符:")
print("今年{1}岁的{0},身高{2}cm".format("小明",age,height))

print("(3)使用带名称的{}作为占位符:")
print("{name1}今年{age1}岁,身高{height1}cm".format(name1 = name,age1 = age,height1 = 100.00))
