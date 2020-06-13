const debug = true
const log = debug ? console.log.bind(console) : function () { }

const int = number => parseInt(number, 10)

const len = arr_or_str => arr_or_str.length

const copy = arr_or_obj => {
    let a = JSON.parse(JSON.stringify(arr_or_obj))
    return a
}
const bindEvent = (element, eventName, callback) => {
    element.addEventListener(eventName, callback)
}
const bindAll = (elements, eventName, callback) => {
    for (let e of elements) {
        bindEvent(e, eventName, callback)
    }
}
const appendHtml = (element, html) => {
    element.insertAdjacentHTML('beforeend', html)
}

const e = selector => document.querySelector(selector)
const es = selector => document.querySelectorAll(selector)

const find = (ele, sel) => {
    return ele.querySelector(sel)
}

const shuffle = (arr) => {
    if (!Array.isArray(arr) && arr.length) {
        return []
    }
    for (let i = arr.length; i > 0; i--) {
        const idx = Math.floor(Math.random() * i)
        if (idx !== (i - 1)) {
            const tmp = arr[idx];
            arr[idx] = arr[i - 1]
            arr[i - 1] = tmp
        }
    }
    return arr
}

const imageFormPath = (path) => {
    let img = new Image()
    img.src = path
    return img
}

const markedSquare = function(array) {
    /*
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

    提示：
        这道题比较麻烦, 你要是不会, 就直接写「这道题目我不会」
        这道题目循环调用作业 14 的 markedLine，这道题目不要求写测试

    分步提示：
        1. 先定义一个 clonedSquare 函数，把 array 的内容复制到一个新数组中
        2. 调用 clonedSquare 函数，得到 square
        3. 遍历 square，每次遍历的元素为 line
        4. 遍历 line，调用一个 markAround 函数，传入 square, i, j
        5. 实现 markAround 函数，对于每一个 square[i][j] 这样的元素都按照规则 +1
            分 4 个顶角、4 条边和剩下的元素这几种情形
        6. 两重遍历结束后，square 就是需要的结果，return square 即可。
    */
    let square = copy(array)
    for (let i = 0; i < len(square); i++) {
        let line = square[i]
        for (let j = 0; j < len(line); j++) {
            if (square[i][j] === 9) {
                markedAround(square, i, j)
            }
        }
    }
    // log('square', square)
    return square
}

const markedAround = function(square, i, j) {
    // left
    jxyi(square, i, j - 1)
    // right
    jxyi(square, i, j + 1)
    // up
    jxyi(square, i - 1, j)
    // down
    jxyi(square, i + 1, j)

    // 四个顶点
    jxyi(square, i - 1, j - 1)
    // right
    jxyi(square, i + 1, j + 1)
    // up
    jxyi(square, i - 1, j + 1)
    // down
    jxyi(square, i + 1, j - 1)
}

const isSquare = function(square, i, j) {
    let rule_row = i >= 0 && i < len(square)
    let rule_col = j >= 0 && j < len(square[0])
    return rule_col && rule_row
}

const jxyi = function(square, i, j) {
    if (isSquare(square, i, j) && square[i][j] != 9) {
        square[i][j] += 1
    }
}

