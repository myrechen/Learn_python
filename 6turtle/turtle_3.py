from turtle import *
#调整绘画速度取值为slowest,slow,normal,fast,fastest
speed("fast")

#背景
bgcolor("SkyBlue")

#地面
pensize(235);pencolor("Lightgreen")
up();goto(-400,-200)
down();goto(400,-200)

#栅栏
pensize(20); pencolor("GoldEnrod")
up();goto(-400,-150)
down();goto(400,-150)
up();goto(-250,-200)
down();goto(-250,-100)
up();goto(-100,-200)
down();goto(-100,-100)
up();goto(30,-200)
down();goto(30,-100)
up();goto(300,-200)
down();goto(300,-100)

#树
pensize(30); pencolor("Olive")
up();goto(-150,-200); down();goto(-150,-120)

pensize(1); color("ForestGreen")
up();goto(-80,-120);down()
begin_fill()
seth(60);circle(80,steps=3)
end_fill()
up();goto(-98,-50);down()
begin_fill()
seth(60);circle(60,steps=3)
end_fill()
up();goto(-115,0);down()
begin_fill()
seth(60);circle(40,steps=3)
end_fill()

#房子
pensize(1);color("#D2D264")
up();home();fd(70);right(90);down()
begin_fill()
fd(200);left(90);fd(200);left(90);fd(200)
end_fill()
color("Pink")
up();home();down()
begin_fill()
left(30);fd(200);right(60);fd(200);home()
end_fill()

pensize(30);color("dimgray")
up();goto(230,30);down();goto(230,100)

color("cyan")
up();goto(150,-90);down()
begin_fill()
seth(45);circle(40,steps=4)
end_fill()

color("chocolate")
up();goto(250,-190);down();seth(90)
begin_fill()
fd(120);left(90);fd(60);left(90);fd(120);left(90);fd(60)
end_fill()
up();goto(195,-130);down()
dot(15,"gray")

#太阳
up();goto(-260,250)
dot(80,"gold")

ht()

input()