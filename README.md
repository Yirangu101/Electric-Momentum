Electric Momentum — Creative Music Coding Project

1. Project Overview

Electric Momentum is a creative coding music project developed using TunePad and Python-based programming.

The aim of this project is to create an energetic, game-style soundtrack by combining different instruments through code.

Instead of using traditional music production software, I used programming commands to control musical notes, rhythms, timing and instrument arrangements.

The final composition is approximately 60 seconds long and includes seven instrument tracks.

Project Information

- Project Name: Electric Momentum
- Platform: TunePad
- Programming Language: Python 
- Music Style:Energetic, game-style instrumental music
- Tempo:120 BPM
- Key: C Major
- Duration: Approximately 60 seconds
- Number of Tracks: 7

## 2. Project Features

The final composition includes seven instrument tracks:

| Instrument | Role in the Composition |
|---|---|
| Keyboard 1 | Main melody |
| Keyboard 2 | Additional energetic melody |
| Keyboard 3 | Supporting harmony |
| Electric Bass | Low-frequency rhythm and support |
| 808 Drum Kit | Beat and rhythm |
| Acoustic Guitar | Additional rhythmic and harmonic layers |
| Synth Strings | Background atmosphere and harmony |

The composition starts with a simple keyboard melody. More instruments gradually enter to build energy and create a fuller sound.

Towards the end, the arrangement becomes simpler again, allowing the main melody to finish the composition.

 3. Programming Concepts Used

This project uses several basic programming concepts introduced during the Creative Coding subject.

Variables

Variables help store musical information, such as notes and patterns.

Lists

Lists are used to organise sequences of musical notes.

For example:

```python
melody = [60, 64, 67, 72]
```

Each number represents a musical pitch.

Loops

Loops help repeat musical patterns without writing the same commands multiple times.

For example:

```python
for note in melody:
    playNote(note, beats=1)
```

Functions and Commands

TunePad provides commands to control the music:

- `setTempo()` — controls the tempo.
- `playNote()` — plays musical notes.
- `rest()` — creates silence or delays an instrument's entrance.

These programming concepts helped me organise the composition and make changes more efficiently.

4. Music Structure

The composition follows a gradual build-up structure.

| Time | Musical Arrangement |
|---|---|
| 0–8 seconds | Keyboard 1 introduction |
| 8–16 seconds | Bass, drums, supporting keyboard and strings enter |
| 16–40 seconds | Guitar and additional keyboard join |
| 40–52 seconds | Main energetic section |
| 52–60 seconds | Keyboard 1 and synth strings ending |

The different instrument entrances were controlled through timing commands in TunePad.

5. Development Process

The project was developed over six weeks.

Week 1 — Initial Experiment

I experimented with basic keyboard notes and drum patterns to understand how TunePad worked.

Week 2 — Adding a Second Keyboard

I added another keyboard track and started exploring how different instruments could work together.

Week 3 — Starting Again

I decided to restart my original composition because I wanted a clearer musical direction.

Week 4 — Developing the Main Melody

I created the main melody, which became the foundation of the final soundtrack.

Week 5 — Building the Instrumental Arrangement

I developed the drum, bass, guitar and keyboard arrangements to create a fuller composition.

Week 6 — Refining the Final Composition

I added more keyboard layers and synth strings. I also adjusted the existing instruments to improve their timing and overall arrangement.

6. Challenges and Solutions

One of the main challenges was synchronising multiple instrument tracks.

Some instruments needed to begin later than others, and their musical patterns had to fit within the same composition.

To address this problem, I used `rest()` commands, adjusted note durations and checked the number of beats in each section.

Another challenge was balancing the different instruments. Adding more tracks did not always improve the music, so I needed to make creative decisions about which instruments should play at different times.

These experiences helped me improve my understanding of debugging, musical structure and creative programming.

7. How to Run the Project

This project was created using TunePad, an online platform for coding music.

1. Visit [TunePad](https://tunepad.com/).
2. Open the Electric Momentum project using the project link below, or open a compatible TunePad project and load the instrument code from this repository.
3. Select an instrument track to view its Python code.
4. Run the track to hear the musical output.
5. Play the complete composition to hear all seven tracks together.

TunePad Project Link:(https://tunepad.com/project/130155)

Note:TunePad-specific commands require the TunePad environment and may not work directly in a standard Python interpreter.

8. Learning Outcomes

Through this project, I learned how programming can be used as a creative tool.

I developed a better understanding of variables, lists, loops and musical timing. I also learned that creating music through code requires both technical problem-solving and creative judgement.

The project helped me become more confident in using code to organise musical ideas and develop an original digital composition.

9. Author and Acknowledgements

Created as part of the 52685 Creative Coding subject at the University of Technology Sydney (UTS).

Author: Yiran Gu

Platform: TunePad

Generative AI Disclosure: ChatGPT was used to assist with generating, reviewing and modifying parts of the TunePad code and project documentation. The project was developed through an iterative process of experimentation and revision. Full details of GenAI use are provided in the assessment documentation.
