/*
- 第一步选择关卡
    - 安装难度划分 done
        - 点击关卡显示不同的 地图
            - 开始 目前只支持 easy medium hard
                - 先解决 easy 模式 6 * 6
                    - 第一步生成地图 done
 */
const toggleClass = (ele, className) => {
    if (ele.classList.contains(className)) {
        ele.classList.remove(className)
    } else {
        ele.classList.add(className)
    }
}

const toggleStartMenu = () => {
    // lin-hide
    let menu = e('#startMenu')
    toggleClass(menu, 'lin-hide')
}

const toggleloadingMessage = () => {
    let msg = e('#loadingMessage')
    toggleClass(msg, 'lin-show')
}

// gameSquare island11 island number clicked
// unclicked gameSquare pig
// gameSquare zero island island26 clicked
// unclicked gameSquare number
// unclicked gameSquare zero island island11
const templateCell = (line, x) => {
    let t = ``
    for (let i = 0; i < line.length; i++) {
        let y = i
        let n = line[i]

        let v = 'number'
        if (n == 9) {
            v = 'pig'
        }
        if (n == 0) {
            v = 'zero'
        }

        let island = ''
        let island11 = ''
        if (v === 'zero') {
            island = 'island'
            island11 = 'island11'
        }
        t += `<div 
             id="row${x}column${y}" 
             class="cell ${island} ${island11} unclicked gameSquare ${v} cell-${x}-${y}"
             data-number="${n}" 
             data-x="${x}" 
             data-y="${y}"
            ></div>`
    }
    let html = `<div class="lin-row clearfix">${t}</div>`
    return html
}

const templateRows = (square) => {
    let t = ''
    for (let i = 0; i < len(square); i++) {
        t += templateCell(square[i], i)
    }
    return t
}

const matirxShuffle = (list, n) => {
    list = shuffle(list)
    let l = []
    for (let i = 0; i < n; i++) {
        let line = []
        for (let j = 0; j < n; j++) {
            let index = i * n + j
            let v = list[index]
            line.push(v)
        }
        l.push(line)
    }
    return markedSquare(l)
}

const getSquare = (n, number) => {
    let l = []
    for (let i = 0; i < number; i++) {
        l.push(9)
    }
    let m = n * n - number
    for (let i = 0; i < m; i++) {
        l.push(0)
    }
    return matirxShuffle(l, n)
}

const actionNewGame = () => {
    window.time = 0
    e('#playArea').innerHTML = ''
    window.data = getSquare(8, 10)
    let t = templateRows(data)
    // log('t', t)
    appendHtml(e('#playArea'), t)
}

const renderSquare = () => {
    let pig_number = 10
    e('#counterNumber').innerHTML = pig_number
    toggleClass(e('#playArea'), 'lin-show')
    window.data = getSquare(8, pig_number)
    let t = templateRows(data)
    // log('t', t)
    appendHtml(e('#playArea'), t)
}

const renderControl = () => {
    e('#playInfoControls').style.display = 'block'
}
//  toggleStartMenu()
// toggleClass(e('#playArea'), 'lin-show')
const startEasyScene = () => {
    toggleStartMenu()
    toggleloadingMessage()
    setTimeout(() => {
        toggleloadingMessage()
        renderSquare()
        renderControl()
    }, 1000)
}

const actionStart = event => {
    let id = event.target.id
    if (id == 'easy') {
        startEasyScene()
    }
}

const bindEventsClickLevel = () => {
    // startButton
    bindEvent(e('#startMenu'), 'click', event => {
        let btn = event.target
        // log('btn', btn)
        let has = btn.classList.contains.bind(btn.classList)
        if (has('startButton')) {
            // log('start')
            actionStart(event)
        }
    })
}

const clickPosition = (x, y) => {
    // log('before square', window.data)
    actionNewGame()
    window.time += 1
    // log('after window.square', window.data)
    let square = copy(window.data)
    let sel = `.cell-${x}-${y}`
    let cell = e(sel)
    vjkl(cell, square)
}

const showCellClassName = (cell) => {
    cell.classList.remove('unclicked')
    cell.classList.add('clicked')
    // lin-number-color
    cell.classList.add('lin-number-color')
}

const showCell = (square, x, y) => {
    let sel = `.cell-${x}-${y}`
    let cell = e(sel)
    showCellClassName(cell)
    window.time += 1
    // show value
    let n = int(square[x][y])
    if (n == 0) {
        n = ''
    }
    if (n == 9) {
        return
    }

    cell.innerHTML = n
}

const showCellAll = (square) => {
    let cells = es('.cell')
    for (let c of cells) {
        if (!c.classList.contains('clicked')) {
            c.classList.remove('unclicked')
            c.classList.add('clicked')
            c.classList.add('lin-number-color')
            let n = int(c.dataset.number)
            if (n == 0) {
                c.innerHTML = ''
            }
            if (n == 9) {
                let x = c.dataset.x
                let y = c.dataset.y
                addPig(x, y)
            }
        }
    }
}

const addPig = (x, y) => {
    let sel = `.cell-${x}-${y}`
    let cell = e(sel)
    cell.classList.remove('unclicked')
    cell.classList.add('lin-number-color')
    cell.classList.add('clicked')
    let t = `
      <div class="sleepZ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Z<br>&nbsp;&nbsp;&nbsp;&nbsp;Z<br>Z</div><div class="pigContainer" style="opacity: 1; display: inline;"><div class="pigBody pigLookUp"><br>°(oo)°<br>~</div><div class="pigEar"></div><div class="pigSpacer"></div><div class="pigEar"></div><div class="pigFeet"></div><div class="pigSpacer"></div><div class="pigFeet"></div></div> 
    `
    appendHtml(cell, t)
}

const vjkl = (cell, s) => {
    flagMusic()
    let x = int(cell.dataset.x)
    let y = int(cell.dataset.y)
    let n = window.data[x][y]
    if (n === 9 && window.time > 1) {
        log('game over 添加 pig')
        pigMusic()
        addPig(x, y)
        showCellAll(window.data)
        return
    }
    if ('123456789'.includes(String(n)) && window.time == 1) {
        clickPosition(x, y)
    }
    showCellClassName(cell)

    if (n == 9) {
        return
    }
    cell.innerHTML = n
    if (n == 0) {
        cell.innerHTML = ''
    }
    if (n === 0) {
        log('click around')
        isLandMusic()
        let square = copy(window.data)
        vjklAround(square, x, y)
    }
}

const vjklAround = function(square, x, y) {
    // left right
    vjkl1(square, x, y - 1)
    vjkl1(square, x, y + 1)
    // up down
    vjkl1(square, x - 1, y)
    vjkl1(square, x + 1, y)

    vjkl1(square, x - 1, y - 1)
    vjkl1(square, x - 1, y + 1)

    vjkl1(square, x + 1, y + 1)
    vjkl1(square, x + 1, y - 1)
}

const isInSquare = (square, x, y) => {
    let row = square.length
    let col = square[0].length
    let rule_row = x >= 0 && x < row
    let rule_col = y >= 0 && y < col
    return rule_row && rule_col
}

const hasClicked = (x, y) => {
    let sel = `.cell-${x}-${y}`
    return e(sel).classList.contains('clicked')
}

const vjkl1 = function(square, x, y) {
    if (isInSquare(square, x, y) && !hasClicked(x, y)) {
        log('debug x y', x, y)
        let n = square[x][y]
        if (n === 9) {
            return
        }
        if (n === 0) {
            // log('vjkl 01 debug  n == 0', x, y)
            showCell(square, x, y)
            vjklAround(square, x, y)
        }
        // log('vjkl 01 debug n == 1-8', x, y, n)
        showCell(square, x, y)
    }
}

const bindEventClickGameSquare = () => {
    bindEvent(e('#playArea'), 'click', event => {
        let area = event.target
        let has = area.classList.contains.bind(area.classList)
        if (has('gameSquare')) {
            let s = copy(window.data)
            window.time += 1
            vjkl(area, s)
        }
    })
}

const actionBack = () => {
    toggleStartMenu()
    toggleClass(e('#playArea'), 'lin-show')
    e('#playInfoControls').style.display = 'none'
}

const actionAbout = () => {
     e('#questionBoardContainer').style.display = 'inline'
}

const bindEventplayInfoControls = () => {
    bindEvent(e('#playInfoControls'), 'click', event => {
        let a = event.target
        log('a', a)
        let has = a.classList.contains.bind(a.classList)
        if (has('lin-new-game')) {
            actionNewGame()
        } else if (has('lin-back')){
            actionBack()
        } else if (has('lin-about')) {
            log('about')
            actionAbout()
            return
        } else if(has('lin-play-bgm')) {
            bgmMusic()
        }
    })
}

const bindEventCancelAlert = () => {
    bindEvent(e('body'), 'click', event => {
        let self = event.target
        // log('self', self)
        // TODO 完成 tab 切换功能
        if (self.classList.contains('lin-about') || self.classList.contains('tab')) {
            let sel = self.data.id
            e(sel).style.display = 'inline'
            return
        } else if (self.classList.contains('counterPigBody')) {
            pigMusic()
        }
        e('#questionBoardContainer').style.display = 'none'
    })
}

const bindEvents = () => {
    bindEventsClickLevel()
    bindEventClickGameSquare()
    bindEventplayInfoControls()
    bindEventCancelAlert()
}

const init = () => {
    initMusic()
}

const __main = () => {
    init()
    window.time = 0
    bindEvents()
}

__main()