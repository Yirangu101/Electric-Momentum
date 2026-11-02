rest(16)

C = [48, 55]
G = [47, 55]
Am = [48, 57]
F = [48, 53]

progression = [C, G, Am, F, C, G, Am, F, C, G, Am]

for phrase in progression:
    for n in phrase:
        playNote(n, beats=4)

rest(16)
