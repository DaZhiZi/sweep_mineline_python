const initMusic = () => {
    let ms = {
        click_btn: './sound/buttonclick.mp3',
        click_block: './sound/clickblock.mp3',
        click_is_land: './sound/clickisland.mp3',
        flag_block: './sound/flagblock.mp3',
        light_click: './sound/buttonclick.mp3',
        bgm: './sound/panamahatsong.mp3',
        pig_song: './sound/pokepig.mp3',
        sleep_pig: './sound/sleepingpigs.mp3',
    }
    insertMusics(ms)
}

const insertMusics = (ms) => {
    let t = ''
    for (let k in ms) {
        t += templateMusic(k, ms[k])
    }
    appendHtml(e('.lin-music'), t)
}

const templateMusic = (className, url) => {
    let c = className
    let u = url
    let t = `
     <audio class="${c}" src="${u}"></audio>
    `
    return t
}


const elementPlay = (sel) => {
    e(sel).play()
}
const clickBtnMusic = () => {
    e('.click_btn').play()
}

const clickBlockMusic = () => {
    e('.click_block').play()
}

const bgmMusic = () => {
    let b = e('.bgm')
    log('b', b)
    b.play()
    b.loop = true
}

// let ms = {
//     click_btn: './sound/buttonclick.mp3',
//     click_block: './sound/clickblock.mp3',
//     click_is_land: './sound/clickisland.mp3',
//     flag_block: './sound/flagblock.mp3',
//     light_click: './sound/buttonclick.mp3',
//     bgm: './sound/panamahatsong.mp3',
//     pig_song: './sound/pokepig.mp3',
//     sleep_pig: './sound/sleepingpigs.mp3',
// }
const isLandMusic = () => {
    let b = e('.click_is_land')
    b.play()
}

const flagMusic = () => {
    let f = e('.flag_block')
    f.play()
}

const pigMusic = () => {
    elementPlay('.pig_song')
}
