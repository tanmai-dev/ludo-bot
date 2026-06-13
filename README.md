# Ludo Bot Arena

A programmable Ludo engine built for bot-vs-bot competitions.

## Overview

This project implements the complete game logic for Ludo and exposes a simple interface for writing custom bots.

Each player only needs to implement:

```python
def move_piece(self, dice, game_state):
    return piece
```

where `piece` is one of:

```text
"R1" "R2" "R3" "R4"
"G1" "G2" "G3" "G4"
"Y1" "Y2" "Y3" "Y4"
"B1" "B2" "B3" "B4"
```

depending on the player's color.

---

## Rules Implemented

* Standard 4-player Ludo
* Piece deployment on rolling a 6
* Captures
* Safe squares
* Home lane progression
* Exact roll required to finish
* Multiple pieces per player
* Invalid move detection
* Tournament mode

---

## Game State

The bot receives:

```python
game_state
```

Important fields:

### Board Position

```python
game_state.board
```

Dictionary mapping pieces to board positions.

Examples:

```python
{
    'R1': 15,
    'G2': 40
}
```

Special values:

```python
100
```

indicates a piece is inside the home lane.

### Progress

```python
game_state.prog
```

Progress along the piece's journey.

Examples:

```python
0
```

Piece still in base.

```python
57
```

Piece has reached the end.

### Current Turn

```python
game_state.current_player
```

Current player object.

---

## Writing a Bot
The bot must have instances `color` and `in_pieces`. Their values may be used but not modified by your bot. The bot must contain a `move_piece` method which should return a string piece of form `"{color}{integer}"`. An example bot is given below.

Example random bot:

```python
import random

class Player:

    def __init__(self, color):
        self.color = color
        self.in_pieces = 0

    def move_piece(self, dice, game_state):

        legal_moves = []

        for i in range(1, 5):
            piece = self.color + str(i)

            if piece not in game_state.prog:
                continue

            prog = game_state.prog[piece]

            if prog == 0:
                if dice == 6:
                    legal_moves.append(piece)
            else:
                if prog + dice <= 57:
                    legal_moves.append(piece)

        if legal_moves:
            return random.choice(legal_moves)

        for i in range(1, 5):
            piece = self.color + str(i)
            if piece in game_state.prog:
                return piece
```

---

## Invalid Moves

If a bot makes an illegal move while a legal move exists, the game is immediately terminated.

Examples:

* Attempting to move a piece that cannot move
* Attempting to deploy without rolling a 6
* Returning a non-existent piece
* Any move violating engine rules

Bots are expected to validate their own choices.

---

## Tournament Scoring

For a completed game:

```text
1st Place: 3 points
2nd Place: 2 points
3rd Place: 1 point
4th Place: 0 points
```

1000 games would be played to compare performance.

---

## Goal

Build the strongest bot.

May the better bot win.
