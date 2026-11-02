rest(16)

C = [36, 36, 43, 36, 40, 43, 36, 43]
G = [43, 43, 38, 43, 47, 38, 43, 38]
Am = [45, 45, 40, 45, 48, 40, 45, 40]
F = [41, 41, 48, 41, 45, 48, 41, 48]

progression = [C, G, Am, F, C, G, Am, F, C, G, Am]

for phrase in progression:
    for n in phrase:
        playNote(n, beats=1)

rest(16)