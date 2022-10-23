let hands: Image[] = []
let dir2 = 0
let idir = 0
function showCompass () {
    hands = [
    images.createImage(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . . . .
        `),
    images.createImage(`
        . # . . .
        . # . . .
        . . # . .
        . . . . .
        . . . . .
        `),
    images.createImage(`
        . . . . .
        # # . . .
        . . # . .
        . . . . .
        . . . . .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        . . # . .
        # # . . .
        . . . . .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        . . # . .
        . # . . .
        . # . . .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        . . # . .
        . . . # .
        . . . # .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        . . # . .
        . . . # #
        . . . . .
        `),
    images.createImage(`
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        `),
    images.createImage(`
        . . . . .
        . . . # #
        . . # . .
        . . . . .
        . . . . .
        `),
    images.createImage(`
        . . . # .
        . . . # .
        . . # . .
        . . . . .
        . . . . .
        `)
    ]
    while (true) {
        dir2 = input.compassHeading() / 30
        idir = Math.floor(dir2)
        hands[idir].showImage(0)
        if (input.buttonIsPressed(Button.B)) {
            break;
        }
    }
    basic.showNumber(input.compassHeading())
}
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # . # . #
        . # # # .
        # # . # #
        . # # # .
        # . # . #
        `)
    basic.clearScreen()
    basic.pause(1000)
    basic.showNumber(input.temperature())
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
    basic.clearScreen()
    basic.pause(1000)
    showCompass()
})
