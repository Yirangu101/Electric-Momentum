rest(16)

C = [64, 67]
G = [62, 67]
Am = [64, 69]
F = [65, 69]

progression = [
    C, G, Am, F,
    C, G, Am, F,
    C, G, Am, F, C
]

for phrase in progression:
    for n in phrase:
        playNote(n, beats=4)




