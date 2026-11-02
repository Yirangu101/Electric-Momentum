rest(32)

C = [72, 76, 79, 76]
G = [71, 74, 79, 74]
Am = [72, 76, 81, 76]
F = [72, 77, 81, 77]

for phrase in [Am, F, C, G, Am, F]:
    for n in phrase:
        playNote(n, beats=2)
        
for phrase in [C, G, Am]:
    for n in phrase:
        playNote(n, beats=1)
    for n in phrase:
        playNote(n, beats=1)

rest(16)
