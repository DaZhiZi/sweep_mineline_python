import turtle, random
from utils import log
from utils import ensure
from utils import isEquals
from task_01 import marked_square
from words import dict_num
from words import dict_char

t = turtle.Turtle()
t.hideturtle()

turtle.tracer(10000, 0.0001)  # draw speed


def forward(step):
    t.forward(step)


# penup 可以把笔抬起来, 这样往前走就不会画线了
def penup():
    t.penup()


# pendown 后又可以画线了
def pendown():
    t.pendown()


# left 可以往左转, 参数是角度
def left(angle):
    t.left(angle)


def right(angle):
    t.right(angle)


# setHeading(注意大小写) 可以设置箭头的朝向, 0 就是朝右
# 90 和 -90 的朝向, 自行摸索一下
def setHeading(angle):
    t.setheading(angle)


def jump(x, y):  # jump 可以无痕走到某个坐标
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


def fill_color(color):
    t.fillcolor(color)


def edge_color(color):
    t.color(color)


def start():
    t.begin_fill()


def end():
    t.end_fill()


def author_inform():
    t.pensize(2)
    t.color('black', 'pink')
    jump(-200, 200)
    t.write("author：大侄子", move=True, align="left", font=("宋体", 30, "normal"))


def triangle(x=0, y=0, length=101):
    l = length
    jump(x, y)
    i = 0
    while (i < 3):
        forward(l)
        right(120)
        i += 1


def rect(x, y, width, height, fillcolor, edgecolor):
    w = width
    h = height
    jump(x, y)
    setHeading(0)
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    i = 0
    while (i < 2):
        forward(w)
        right(90)
        forward(h)
        right(90)
        i = i + 1
    end()


def polygon(length, num, fillcolor, edgecolor):
    l = length
    n = num
    angle = (n - 2) * 180 / n
    degree = 180 - angle
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < n):
        forward(l)
        right(degree)
        # 特别注意，循环结束前一定要改变 i 的值
        # 否则循环永远不会结束的
        i = i + 1
    end()


def circle(x, y, r, fillcolor, edgecolor):
    jump(x, y)
    num = 36
    import math
    length = (2 * math.pi * r) / num
    jcdu = (90 + (360 / num) / 2)
    start()
    left(jcdu)
    forward(r)
    right(jcdu)
    end()
    polygon(length, num, fillcolor, edgecolor)


def fan(length, num, fillcolor, edgecolor):
    l = length
    n = num
    angle = (n - 2) * 180 / n
    degree = 180 - angle
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < n / 2):
        forward(l)
        right(degree)
        # 特别注意，循环结束前一定要改变 i 的值
        # 否则循环永远不会结束的
        i = i + 1
    end()


def semicircle(x, y, r, fillcolor, edgecolor):  # 半圆
    jump(x, y)
    num = 36
    import math
    length = (2 * math.pi * r) / num
    jcdu = (90 + (360 / num) / 2)
    start()
    left(jcdu)
    forward(r)
    right(jcdu)
    fan(length, num, fillcolor, edgecolor)
    right(180 - jcdu)
    forward(2 * r)
    end()
    pass


def star(x, y, length, fillcolor, edgecolor):
    jump(x, y)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < 5):
        forward(length)
        right(144)
        i = i + 1
    end()


def sin(degree):
    import math
    # 如上课所述, 数学库里面的 sin 函数接受弧度作为参数
    # 我们这个函数接受角度, 下面是弧度转角度的公式
    radians = degree * math.pi / 180
    return math.sin(radians)


def cos(degree):
    import math
    radians = degree * math.pi / 180
    return math.cos(radians)


def center_star(x, y, r, fillcolor, edgecolor):
    du = 18
    x1 = x - cos(du) * r
    y1 = y - sin(du) * r
    length = cos(du) * r * 2
    star(x1, -y1, length, fillcolor, edgecolor)


def draw_square(x, y, width, fillcolor, edgecolor):
    w = width
    jump(x, y)
    setHeading(0)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < 4):
        forward(w)
        right(90)
        i = i + 1
    end()


# 画出 地图 map
# 5
# ===
# 实现函数, 画一排正方形, 有如下参数
# x, y 是第一个正方形左上角坐标
# n 是正方形的个数
# space 是两个正方形之间的间距
# len 是正方形的边长
# square_line(x, y, n, space, len)
#
# 步骤如下:
# 作业 4 中画 5 个正方形, 循环 5 次
# 作业 5 中画 n 个正方形, 循环 n 次
# 同时两个正方形的间距从 10 换成了 space
def square_line(x, y, n, space, len, fillcolor, edgecolor):
    # y 不变   x： 0 30+10  30+10+30+10
    i = 0
    width = len
    while (i < n):
        x1 = x + (width + space) * i
        draw_square(x1, y, width, fillcolor, edgecolor)
        i += 1


# 6
# ===
# 实现函数, 用上题的函数来画一个正方形方阵, 参数如下
# x, y 是第一个正方形左上角坐标
# space 是两个正方形之间的间距
# len 是正方形的边长
# n 是横向正方形的个数
# m 是纵向正方形的个数
# square_square(x, y, space, len, n, m)
#
# 步骤如下
# m 是纵向正方形的个数, 所以需要循环 m 次,
# 每次循环画一排正方形, 这是作业 5 的要求
# 所以每次循环调用作业 5 的 square_line 函数就行
def square_square(x, y, space, len, n, m, fillcolor, edgecolor):
    i = 0
    width = len
    x1 = x
    while (i < m):
        y1 = y - (width + space) * i
        square_line(x1, y1, n, space, width, fillcolor, edgecolor)
        i += 1


def line_x(x, y):
    draw_square(-381, 320, 30, 'pink', 'black')

    draw_square(-381 + 30, 320, 30, 'pink', 'black')

    draw_square(-381, 320 - 30, 30, 'pink', 'black')
    end()


def mine_map():
    # square_line(-381 , 320, 16, 0, 30, 'pink', 'black')
    square_square(-381, 320, 0, 30, 16, 16, 'pink', 'black')
    # line_x(0, 0)
    pass


def draw_pixel(x, y, pixel, size=3, color='pink'):
    jump(x, y)
    pixel_color = ''
    if pixel == '0':
        pixel_color = 'white'
    else:
        # color = '#0997F7'
        # color = 'pink'
        pixel_color = color
        fill_color(pixel_color)
        start()
        for i in range(4):
            forward(size)
            right(90)
        end()


def draw_line(x, y, pixels, size=3, color='pink'):
    for i in pixels:
        jump(x, y)
        draw_pixel(x, y, i, size, color)
        x += size


def draw_block(x, y, block, size=3, color='pink'):
    for i in block:
        draw_line(x, y, i, size, color)
        y -= size


def draw_str(x, y, str, size=3):
    for i in str:
        jump(x, y)
        s = dict_char[i]
        draw_block(x, y, s, size)
        x += len(s[0]) * size


def draw_num(x, y, num, size=3):
    x1 = -200 + x * 30
    y1 = 200 - y * 30
    block = dict_num[num]
    draw_block(x1, y1, block)
    pass


# 用它实现本函数, 返回 0 或 1
def random01():
    import random
    num = random.randint(0, 1)
    r = -1
    if num > 0.5:
        r = 1
    else:
        r = 0
    # log('r', r)
    return r


"""
    返回一个只包含了 0 1 的随机 array, 长度为 n
   假设 n 为 5, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
   [0, 0, 1, 0, 1]
"""


def random_line01(n):
    list = []
    for i in range(n):
        ele = random01()
        list.append(ele)
    # log('list', list)
    return list


"""
    返回一个只包含了 0 9 的随机 array, 长度为 n
    假设 n 为 5, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    [0, 0, 9, 0, 9]
"""


def random_line09(n, limit):
    list = []
    l = limit
    for i in range(n):
        ele = random01() * 9
        if ele == 9 and l > 0:
            l -= 1
            list.append(ele)
        else:
            list.append(0)
    # log('list', list)
    return list


def random_square_09(n, limit_num):
    list = []
    limit = limit_num / n
    for i in range(n):
        line = random_line09(n, limit)
        list.append(line)
    # log('list', list)
    return list
    pass


def search_mine(square):
    list = []
    for i, line in enumerate(square):
        for j, point in enumerate(line):
            if point == 9:
                index = (i, j)  # tuple (x, y) 坐标
                list.append(index)
    return list


def mineline_square():
    arr = random_square_09(10, 10)
    square = marked_square(arr)
    log('sqaure', square)
    return square


square = mineline_square()


def square_index(x, y):  # 返回 坐标 的值
    return square[x][y]


def click_index(x, y, size=3):
    a = 10
    b = 10
    x1 = -200
    y1 = 200
    w = a * size
    h = b * size
    x2 = (x - x1) // w
    y2 = (y1 - y) // h
    log('click_index', (x2, y2))
    return (x2, y2)


log('start square', square)


def draw_mineline(x, y, ele):
    x1 = -200 + x * 30
    y1 = 200 - y * 30
    block = dict_num[ele]
    draw_block(x1, y1, block, size=1, color='pink')


def gua_game_over():
    str = '大侄子 GUA GAME OVER'
    draw_str(100, -250, str, size=3)


click_time = 0  # 点击次数


def click(*args):
    log('click')
    # click_time += 1
    x, y = args
    log('点击 位置 x y', x, y)
    index = click_index(x, y, 3)
    x, y = int(index[0]), int(index[1])
    # log('x', x, 'y', y)
    ele = square_index(x, y)
    log('ele', ele)
    if ele == 9:
        list = search_mine(square)
        for tuple in list:
            (x, y) = tuple
            draw_mineline(x, y, ele)
            gua_game_over()
    else:
        draw_num(x, y, ele, size=3)


def bind_click(func):
    turtle.onscreenclick(func)

def test_word():
    str = '!'
    draw_str(-100, 250, str, size=3)
    h = 'HELP'
    draw_str(-100, 250 - 50, h, size=3)

def main():
    # author_inform()
    mine_map()
    bind_click(click)
    # test_word()
    turtle.done()


if __name__ == '__main__':
    main()
