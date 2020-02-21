import math

with open("xmas.gcode", "r") as myfile:
    data = myfile.readlines()
    z = 2
    pix_array = []
    for line in data:
        if line and line[0:2] == 'G1':
            if line[3] == 'X':
                x = int(float(line[4:9]))
                if line[11] == 'Y':
                    y = int(float(line[12:17]))
                if line[12] == 'Y':
                    y = int(float(line[13:18]))
                if line[13] == 'Y':
                    y = int(float(line[14:19]))
                if "E" in line[18:22]:
                    pix_array.append(x)
                    pix_array.append(y)
                    pix_array.append(z)
                else:
                    pix_array.append(999)
            if line[3] == 'Z':
                z += 1
    with open('output.js', 'w') as file:
        file.write("""let z1 = 0
let z2 = 0
let y1 = 0
let y2 = 0
let x1 = 0
let x2 = 0
let ticker = 0
let draw = 1
let list: number[] = []
player.onChat("run", function () {
    list = """ + str(pix_array) + """
    for (let value of list) {
        if (value < 999) {
            if (ticker % 3 == 0) {
                x2 = x1
                x1 = value
            }
            if (ticker % 3 == 1) {
                y2 = y1
                y1 = value
            }
            if (ticker % 3 == 2) {
                z2 = z1
                z1 = value
                if (draw == 1) {
                    shapes.line(blocks.block(Block.PurpleGlazedTerracotta), positions.createWorld(x1, z1, y1), positions.createWorld(x2, z2, y2))
                } else {
                    x2 = x1
                    y2 = y1
                    z2 = z1
                    draw = 1
                }
            }
            ticker += 1
        } else {
            draw = 0
        }
        if (ticker % 120 == 0) {
            player.say(ticker.toString())
        }
    }
})""")


