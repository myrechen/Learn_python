from time import *
from turtle import *

# fd(100)
# left(60)
# bk(200)
# right(90)
# fd(100)
# seth(60)
# fd(100)
# goto(100,100)
# sleep(1)
# clear()
# goto(100,0)
# sleep(1)
# reset()
# goto(100,100)
# sleep(1)
# reset()

#抬笔落笔
fd(50);up()
fd(50);down()
#设置笔迹粗细,颜色
pensize(5)
pencolor("Red")
fd(50)
sleep(1)
#回到画布中心
clear();home()
sleep(1)
#设置填充颜色
fillcolor("Green")
color("blue","yellow")
begin_fill()
goto(-100,100);goto(-100,0);goto(0,0)
end_fill()

input("enter:")