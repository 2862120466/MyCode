"""
字符画是一系列字符的组合，可以将单个字符看成一个像素，表示一种颜色，字符
的种类越多，可以表现的颜色也就越多，图像就越有层次感

灰度值：指黑白图像中点的颜色深度。范围从0-255，白色为255，黑色为0
RGB：三原色，对应红绿蓝，通过三原色的叠加得到各种颜色

可以用灰度值公式将RGB值映射到灰度值
灰度值公式 gray = 0.2126 * r + 0.7152 * g +0.0722 * b
接着创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）
的用列表末尾的符号。
"""

from PIL import Image
import argparse

# 字符集有93个不重复字符
ascii_char = list("$@%&#QWERTYUIOPASDFGHJKLZXCVBNM*qwertyuiopasdfghjklzxcvbnm123456789/\|()""{}[]?-_+~<>!;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):

    length = len(ascii_char)
    gray = int(0.21 * r + 0.71 * g + 0.07 * b)

    if alpha == 0:  #当alpha为0时，表示图片中该位置为空白
        return ' '

    unit = (alpha + 1) / length
    where = int(gray / unit)  # 像素在字符集中的对应位置 / 字符集长度 = 灰度值 / 256

    return ascii_char[where]

if __name__ == "__main__":

    width = 55
    height = 30

    im = Image.open('E:\wcc\图片\dlam.png')  #使用 PIL 的 Image.open 打开图片文件，获得对象 im
    im = im.resize((width,height))  #使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度
                                    #第二个参数Image.NEAREST表示输出低质量图片

    txt = ''
    for i in range(height): # 遍历提取图片中每行的像素的RGB值，调用get_char转成对应的字符
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))  # 调用 get_char 时候的参数是通过 PIL 库的 getpixel 获取的
        txt += '\n'  # 将所有的像素对应的字符拼接在一起成为一个字符串txt


    print(txt)

    confirm = input('你需要存储这个字符画吗？ Y/N：')
    if confirm == 'y' or confirm == 'Y':

        name = input('请输入这个字符画的名字：')
        path = "E:\wcc\图片\字符画"
        path_name = path + r'\\' + name + '.txt'

        with open(path_name,'w') as f:
            f.write(txt)

    else:print('NO SAVE')