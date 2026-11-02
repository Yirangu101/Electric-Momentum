rest(32)

Am = [57, 60, 64, 69, 64, 60, 64, 60]
F = [53, 57, 60, 65, 60, 57, 60, 57]
C = [60, 64, 67, 72, 67, 64, 67, 64]
G = [55, 59, 62, 67, 62, 59, 62, 59]

progression = [Am, F, C, G, Am, F, C, G, Am]

for phrase in progression:
    for n in phrase:
        playNote(n, beats=1)

rest(16)

