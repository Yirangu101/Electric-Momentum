rest(16)

basic = [
    0, 4, 4, 4,
    2, 4, 4, 4,
    0, 4, 4, 4,
    2, 4, 0, 4
]

groove = [
    0, 4, 4, 4,
    2, 4, 0, 4,
    0, 4, 0, 4,
    2, 4, 0, 4
]

climax = [
    0, 4, 0, 4,
    2, 4, 0, 4,
    0, 4, 0, 4,
    2, 2, 0, 2
]

for pattern in [basic, basic]:
    for n in pattern:
        playNote(n, beats=0.5)

for pattern in [groove, groove, groove, groove]:
    for n in pattern:
        playNote(n, beats=0.5)

for pattern in [basic, groove]:
    for n in pattern:
        playNote(n, beats=0.5)

for pattern in [climax, climax, climax]:
    for n in pattern:
        playNote(n, beats=0.5)

rest(16)
