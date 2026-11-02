C = [60, 64, 67, 72, 67, 64, 62, 60]
G = [59, 62, 67, 71, 74, 71, 67, 62]
Am = [57, 60, 64, 69, 72, 69, 64, 60]
F = [57, 60, 65, 69, 72, 69, 65, 60]

for phrase in [C, G]:
    for n in phrase:
        playNote(n, beats=1)

for phrase in [C, G, Am, F, C, G, Am, F]:
    for n in phrase:
        playNote(n, beats=1)

for phrase in [C, G, Am]:
    for n in phrase:
        playNote(n, beats=1)

for n in [65, 69, 72, 69, 65, 60, 64]:
    playNote(n, beats=2)

playNote(60, beats=2)
