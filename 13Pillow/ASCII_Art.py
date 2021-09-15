from PIL import Image
def main():
    img_name = "D:\VSC_code\PY_CODE\\13Pillow\hellokitty.jpg"
    img = Image.open(img_name)

    ##调整图像色彩尺寸,让一个像素对应一个字符,这里设置为宽80字符,高40字符
    width,height = 120,180
    img = img.resize((width,height))

    ##转为灰度图像
    img = img.convert('L')
    
    ##上述代码可采用链式写法
    ##img = Image.open(img_name).resize(width,height).convert('L')

    ##根据灰度值生成字符画
    text = ''
    for y in range(height):
        for x in range(width):
            text += getchar(img.getpixel((x,y)))
        text += "\n"
    
    #写入文件
    fo = open("D:\VSC_code\PY_CODE\\13Pillow\hellokitty.txt",'w')
    fo.write(text)
    fo.close()

#getchar方法
ascii_chars = list('MNHQ$OC?7>!:-;. ')
def getchar(gray):
    unit = 256 / len(ascii_chars)
    return ascii_chars[int(gray // unit)]
    #return '@' if gray < 128 else ' '

if __name__ == '__main__':
    main()