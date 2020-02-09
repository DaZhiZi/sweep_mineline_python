from utils import log
from utils import ensure
from utils import isEquals

""" 
    n 是 int
    返回这样规律的字符串, 特殊情况不考虑
    n       返回值
    1       '1'
    2       '121'
    3       '12321'

  方法一：两部分 left  1-n   right  (n-1)-1
  方法二： 对称 三部分  left   n   right
"""


def str1(n):
    r = '{}'.format(n)
    i = n - 1
    while (i > 0):
        r = str(i) + r + str(i)
        i -= 1
    log('r', r)
    return r


def test_str1():
    msg = 'str1'
    isEquals(str1(3), '12321', msg)


# 判断回文数
def hvwfuu(num):
    return str(num) == str(num)[::-1]
    pass


def test_hvwfuu():
    msg = 'hvwfuu'
    isEquals(hvwfuu(12321), True, msg)
    isEquals(hvwfuu(-12321), False, msg)


"""
    n 是 int
   返回这样规律的字符串, 特殊情况不考虑
   n       返回值
   1       'A'
   2       'ABA'
   3       'ABCBA'
"""


def str2(n):
    upper = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = '{}'.format(upper[n])
    i = n - 1
    while (i > 0):
        r = upper[i] + r + upper[i]
        i -= 1
    log('r', r)
    return r


def test_str2():
    msg = 'str2'
    isEquals(str2(1), 'A', msg)
    isEquals(str2(2), 'ABA', msg)
    isEquals(str2(3), 'ABCBA', msg)


def add(num1, num2):
    sum = num1 + num2
    r = '{} + {} = {}'.format(num1, num2, sum)
    return r


def add_line(n):
    list = []
    for i in range(1, n + 1):
        ele = add(i, n)
        list.append(ele)
    log('list', list)
    return list


# 实现加法口诀表
def add_table():
    list = []
    for i in range(1, 10):
        line = add_line(i)
        list.append(line)
    log('list', list)
    return list
    pass


# 2020/02/05 16:28:40 list [['1 + 1 = 2'], ['1 + 2 = 3', '2 + 2 = 4'], ['1 + 3 = 4', '2 + 3 = 5', '3 + 3 = 6'], ['1 + 4 = 5', '2 + 4 = 6', '3 + 4 = 7', '4 + 4 = 8'], ['1 + 5 = 6', '2 + 5 = 7', '3 + 5 = 8', '4 + 5 = 9', '5 + 5 = 10'], ['1 + 6 = 7', '2 + 6 = 8', '3 + 6 = 9', '4 + 6 = 10', '5 + 6 = 11', '6 + 6 = 12'], ['1 + 7 = 8', '2 + 7 = 9', '3 + 7 = 10', '4 + 7 = 11', '5 + 7 = 12', '6 + 7 = 13', '7 + 7 = 14'], ['1 + 8 = 9', '2 + 8 = 10', '3 + 8 = 11', '4 + 8 = 12', '5 + 8 = 13', '6 + 8 = 14', '7 + 8 = 15', '8 + 8 = 16'], ['1 + 9 = 10', '2 + 9 = 11', '3 + 9 = 12', '4 + 9 = 13', '5 + 9 = 14', '6 + 9 = 15', '7 + 9 = 16', '8 + 9 = 17', '9 + 9 = 18']]

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
    pass


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
   返回以下格式的数据
    假设 n 为 3, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    注意, 这只是一个 array, 并不是它显示的样子
    注意, 这是一个 array 不是 string
    [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0],
    ]
    返回, 包含了 n 个『只包含 n 个「随机 0 1」的 array』的 array
"""


def random_square01(n):
    list = []
    for i in range(n):
        ele = random_line01(n)
        list.append(ele)
    # log('list', list)
    return list


"""
    返回一个只包含了 0 9 的随机 array, 长度为 n
    假设 n 为 5, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    [0, 0, 9, 0, 9]
"""


def random_line09(n):
    list = []
    for i in range(n):
        ele = random01() * 9
        list.append(ele)
    # log('list', list)
    return list


"""
    array 是一个只包含了 0 9 的 array
   返回一个标记过的 array
   标记规则如下
   对于下面这样的 array
   [0, 0, 9, 0, 9]
   标记后是这样
   [0, 1, 9, 2, 9]

   规则是, 0 会被设置为左右两边 9 的数量
"""


def copy_arr(arr):
    list = []
    for i in range(len(arr)):
        ele = arr[i]
        list.append(ele)
    # log('list', list)
    return list


def abs(num):
    r = num
    if num < 0:
        r = -num
    return r


def marked_line(arr):
    list = copy_arr(arr)
    for i in range(len(list)):
        ele = list[i]
        log('ele', ele)
        if ele != 9:
            tmp = abs(i - 1)
            if list[tmp] == 9:
                # log('list[i-1]', list[i-1])
                ele += 1
            if list[i + 1] == 9:
                ele += 1
        list[i] = ele
    # log('list', list)
    return list


def test_marked_line():
    msg = 'marked_line'
    isEquals(marked_line([0, 0, 9, 0, 9]), [0, 1, 9, 2, 9], msg)


# 复制一个 square
def copy_square(arr):
    list = []
    for i in range(len(arr)):
        line = []
        for j in range(len(arr[i])):
            ele = arr[i][j]
            line.append(ele)
        list.append(line)
    # log('list', list)
    return list


def test_copy_square():
    msg = 'copy_square'
    arr = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0],
    ]
    copy_arr = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0],
    ]
    isEquals(copy_square(arr), copy_arr, msg)


# 辅助函数, 给数字 + 1
# 这里会判断下标是否合法  最后判断 越界
def plus1(arr, x, y):
    n = len(arr)
    if (x >= 0 and x < n and y >= 0 and y < n):
        if (arr[x][y] != 9):
            arr[x][y] += 1


"""
###
#+#
###
"""


def marked_around(arr, x, y):
    if (arr[x][y] == 9):
        # 左边 3 个
        plus1(arr, x - 1, y - 1)
        plus1(arr, x - 1, y)
        plus1(arr, x - 1, y + 1)
        # 上下 2 个
        plus1(arr, x, y - 1)
        plus1(arr, x, y + 1)
        # 右边 3 个
        plus1(arr, x + 1, y - 1)
        plus1(arr, x + 1, y)
        plus1(arr, x + 1, y + 1)

    pass


"""
  array 是一个「包含了『只包含了 0 9 的 array』的 array」
  返回一个标记过的 array
  ** 注意, 使用一个新数组来存储结果, 不要直接修改老数组

  范例如下, 这是 array
  [
      [0, 9, 0, 0],
      [0, 0, 9, 0],
      [9, 0, 9, 0],
      [0, 9, 0, 0],
  ]

  这是标记后的结果
  [
      [1, 9, 2, 1],
      [2, 4, 9, 2],
      [9, 4, 9, 2],
      [2, 9, 2, 1],
  ]

  规则是, 0 会被设置为四周 8 个元素中 9 的数量
"""


def marked_square(arr):
    list = copy_square(arr)
    for i in range(len(list)):
        line = []
        for j in range(len(list[i])):
            marked_around(list, i, j)
    log('list', list)
    return list
    pass


def test_marked_square():
    msg = 'marked_square'
    arr = [
        [0, 9, 0, 0],
        [0, 0, 9, 0],
        [9, 0, 9, 0],
        [0, 9, 0, 0],
    ]
    copy_arr = [
        [1, 9, 2, 1],
        [2, 4, 9, 2],
        [9, 4, 9, 2],
        [2, 9, 2, 1],
    ]
    isEquals(marked_square(arr), copy_arr, msg)


def main():
    # test_str1()
    # test_hvwfuu()
    # test_str2()
    # add_table()
    # random01()
    # random_line01(4)
    # random_square01(4)
    # test_marked_line()
    # test_copy_square()
    test_marked_square()
    pass


if __name__ == '__main__':
    main()
