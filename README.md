# Ludo Bot Arena

A programmable Ludo engine where players are controlled by Python bots.

The engine handles:

* Dice rolls
* Turn order
* Captures
* Safe squares
* Home lane logic
* Finishing pieces
* Winner detection
* Invalid move detection
* Tournament rankings

Your bot only needs to decide:

```python
def move_piece(self, dice, game_state):
    return piece
```

---

# Goal

Get all four of your pieces to the end before everyone else.

Tournament scoring:

```text
1st Place = 3 points
2nd Place = 2 points
3rd Place = 1 point
4th Place = 0 points
```

---

# Piece Names

Each player controls four pieces.

```text
Red:
R1 R2 R3 R4

Green:
G1 G2 G3 G4

Yellow:
Y1 Y2 Y3 Y4

Blue:
B1 B2 B3 B4
```

---

# How The Board Works

The outer track contains 52 numbered squares.

```text
1 → 2 → 3 → ... → 52 → 1 → 2 → ...
```

The numbering wraps around.

Example:

```python
board["R1"] = 50
```

Rolling:

```text
4
```

moves the piece to:

```python
board["R1"] = 2
```

because:

```text
50 → 51 → 52 → 1 → 2
```

---

# Two Important Dictionaries

The engine tracks every piece using two systems:

```python
game_state.board
```

and

```python
game_state.prog
```

---

## Board Position (`board`)

Stores where a piece is physically standing.

Example:

```python
board["R1"] = 17
```

means:

```text
R1 is standing on outer square 17.
```

Special values:

```python
board[piece] = 0
```

means:

```text
Piece is still inside base.
```

```python
board[piece] = 100
```

means:

```text
Piece is inside the home lane.
```

---

## Progress (`prog`)

Stores how far a piece has travelled since entering the board.

Example:

```python
prog["R1"] = 1
```

means:

```text
R1 has just entered the board.
```

Example:

```python
prog["R1"] = 30
```

means:

```text
R1 has travelled 30 steps since entering.
```

Progress never wraps around.

It always increases:

```text
1 → 2 → 3 → ... → 57
```

The engine uses progress to determine:

* Home lane entry
* Finishing
* Move legality

---

# Why Both Exist

Example:

```python
board["R1"] = 3
prog["R1"] = 55
```

and

```python
board["G1"] = 3
prog["G1"] = 3
```

Both pieces occupy square 3.

However:

```text
R1 is almost finished.
G1 has barely started.
```

Board position alone cannot distinguish this.

---

# Entering The Board

All pieces begin inside base.

```python
prog[piece] = 0
```

A piece can only leave base by rolling:

```text
6
```

Starting squares:

```text
Red    → 1
Green  → 14
Yellow → 27
Blue   → 40
```

Example:

```python
dice = 6
piece = "R1"
```

Result:

```python
board["R1"] = 1
prog["R1"] = 1
```

---

# Home Lane

When:

```python
prog[piece] > 51
```

the piece enters the home lane.

At that point:

```python
board[piece] = 100
```

The value:

```text
100
```

does not represent a real board square.

It simply means:

```text
The piece is somewhere inside its home lane.
```

Example:

```python
prog["R1"] = 53
board["R1"] = 100
```

and

```python
prog["R1"] = 56
board["R1"] = 100
```

are both valid.

The exact lane position is determined by progress.

---

# Finishing A Piece

A piece finishes when:

```python
prog[piece] == 57
```

The engine removes it completely:

```python
del board[piece]
del prog[piece]
```

The piece can never move again.

---

# Exact Finish Rule

A move is legal only if:

```python
prog[piece] + dice <= 57
```

Example:

```python
prog = 55
dice = 2
```

Legal.

Example:

```python
prog = 55
dice = 3
```

Illegal.

---

# Safe Squares

The following squares are safe:

```text
1
9
14
22
27
35
40
48
```

Pieces cannot be captured on safe squares.

---

# Capturing

If a piece lands on an opponent and the square is not safe:

```text
The opponent is captured.
```

The opponent is sent back to base:

```python
board[opponent] = 0
prog[opponent] = 0
```

The opponent must roll another 6 to re-enter.

---

# Same-Color Collision Rule

This engine uses a custom rule.

If a piece lands on another piece of the same color:

```text
The move is cancelled.
```

The piece returns to its previous position.

The player immediately receives another turn.

Internally this is called:

```text
reroll
```

Example:

```text
R1 lands on R2
```

Result:

```text
R1 returns to where it came from
Red gets another turn
```

---

# Extra Turns

A player receives another turn if:

### Rolling a 6/ Capturing a piece

Standard Ludo rule.

### Triggering a reroll

Landing on a friendly piece.

### Finishing a piece

A piece reaches:

```python
prog == 57
```

and the player still has unfinished pieces remaining.

---

# Winning

A player wins when:

```python
in_pieces == 4
```

meaning all four pieces have finished.

The player is added to:

```python
game_state.winners
```

and removed from future play.

---

# Turn Order

Players move in this order:

```text
Red
Green
Yellow
Blue
```

The turn advances normally unless:

* A 6 is rolled
* A reroll occurs
* A piece finishes

In those cases the player immediately plays again.

---

# Legal Moves

A move is legal if:

### Piece is in base

```python
prog[piece] == 0
```

and

```python
dice == 6
```

---

### Piece is already active

```python
prog[piece] + dice <= 57
```

---

# Illegal Moves

Examples:

### Moving a piece out of base without rolling 6

```text
Illegal
```

---

### Overshooting the finish

Example:

```python
prog = 55
dice = 4
```

Illegal because:

```python
55 + 4 > 57
```

---

### Selecting a finished piece

Finished pieces no longer exist inside:

```python
game_state.board
game_state.prog
```

Attempting to move one is illegal.

---

# Invalid Move Detection

The engine checks:

```text
Did the bot attempt an invalid move?
```

and

```text
Was another legal move available?
```

Example:

```text
Dice = 6

R1 can legally enter the board.

Bot chooses R2.

R2 cannot move.
```

The engine detects that:

```text
A legal move existed.
```

and immediately terminates the game.

---

# Consequences Of Invalid Moves

If a bot makes an invalid move while another legal move exists:

```text
Game Terminated
```

The match ends immediately.

This prevents bots from:

* Making impossible moves
* Ignoring valid moves
* Exploiting undefined behaviour

---

# Bot Interface

Every bot must implement:

```python
def move_piece(self, dice, game_state):
    return piece
```

Inputs:

```python
dice
```

Current die roll.

```python
game_state
```

Full game state.

Output:

```python
piece
```

A string such as:

```text
R1
G3
Y2
B4
```

---

# Useful Game State Fields

### Board Positions

```python
game_state.board
```

Example:

```python
{
    "R1": 17,
    "G3": 40
}
```

---

### Progress Values

```python
game_state.prog
```

Example:

```python
{
    "R1": 35,
    "R2": 0
}
```

---

### Current Player

```python
game_state.current_player
```

---

### Winners

```python
game_state.winners
```

Contains players who have already finished.

---

# Example Random Bot

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

# Competition Rule

Use any strategy you want.

Examples:

* Capture-focused bots
* Defensive bots
* Racing bots
* Monte Carlo bots
* Search-based bots
* Machine-learning bots

The only requirement:

```text
Return a valid piece name.
```

May the better bot win.
