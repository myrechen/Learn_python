import matplotlib.pyplot as plt
import numpy as np

def IFSDrawFractal(IFS_code,n):
    # 设置初始点位置
    x = 0
    y = 0

    # 点序列集，初始为空列表
    dots = []

    # 获取IFS_code中每个仿射变换的概率，IFS_code元素的最后一个是概率
    P = [c[-1] for c in IFS_code]

    plt.ion()
    # 清除当前的axes
    plt.cla()
    # 设置x，y轴的单位长度相等
    plt.axis('equal')
    # 隐藏坐标轴
    # plt.axis('off')
    # plt.pause(8)

    # 迭代产生点
    for dot in range(n):
        r = np.random.rand() # 生成（0,1）之间的一个随机浮点数
        # 依据随机数r，选择仿射变换
        p0 = 0
        k = -2
        for i,p in enumerate(P):
            p1 = p0+p
            if r > p0 and r <= p1:
                k = i   # k值用来指定某一个仿射变换
                break
            else:
              p0 = p1
                
        # 获取6个仿射变换系数
        a = IFS_code[k][0]
        b = IFS_code[k][1]
        c = IFS_code[k][2]
        d = IFS_code[k][3]
        e = IFS_code[k][4]
        f = IFS_code[k][5]
        
        # 计算仿射变换后的坐标值
        u = a*x+b*y+e
        y = c*x+d*y+f
        x = u

        dots.append((x,y))

        # 绘制
        if((dot+1)%500 == 0):
            print(dot)
            X = [d[0] for d in dots] # dots中所有点的x坐标值
            Y = [d[1] for d in dots] # dots中所有点的y坐标值
            plt.scatter(X,Y,color="blue",s=3,alpha=1) # 绘制图像
            # 暂停0.1秒
            plt.pause(0.001)
            X.clear()
            Y.clear()
            dots.clear()

    # plt.cla()
    # plt.axis('equal')
    # # # 隐藏坐标轴
    # plt.axis('off')
    # # 绘制点集
    # X = [d[0] for d in dots] # dots中所有点的x坐标值
    # Y = [d[1] for d in dots] # dots中所有点的y坐标值
    # plt.scatter(X,Y,color="blue",s=3,alpha=1) # 绘制图像
    # # 暂停0.1秒
    # plt.pause(0.001)

    plt.show()
