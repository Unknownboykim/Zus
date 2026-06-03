# Rook vs Bishop Simulation

## Overview

This program simulates a simplified chess game involving only two pieces: a white bishop and a black rook. The bishop remains stationary at c3, while the rook starts at h1 and moves for up to 15 rounds. In each round, a coin toss determines whether the rook moves up or to the right, and the sum of two dice rolls determines how many squares it moves. The board wraps around at the top and right edges, so the rook can reappear on the opposite side of the board. After every move, the program prints the round number, coin result, dice result, direction, and the rook's new position. It then checks whether the bishop can capture the rook. If the bishop can capture the rook, the bishop wins; otherwise, the rook wins if it survives all 15 rounds.

## Approach

I chose to use an object-oriented design because the problem naturally involves different types of chess pieces with different movement and capture rules. I created a base `Piece` class to store the common attributes shared by all pieces, including file, rank, and color. The `Bishop` and `Rook` classes inherit from `Piece` and implement their own capture logic through a `can_capture` method.

For the board representation, I stored positions internally as numeric file and rank values rather than chess notation strings. For example, c3 is represented as file 3, rank 3. This made movement calculations and capture checks simpler because they could be performed directly with arithmetic operations. Chess notation is only used when displaying positions to the user.

The rook movement logic is encapsulated inside the `Rook` class through a dedicated `move` method. To support the wrap-around behavior described in the problem, I used modulo arithmetic to keep positions within the valid range of 1 through 8.

## Pros

One advantage of this approach is that the code is easy to read and understand. The responsibilities of each class are clearly separated, and the capture logic for each piece is contained within its own class. Using numeric coordinates also simplifies movement calculations and avoids repeated string parsing.

Another advantage is that the design can be extended fairly easily. Additional chess pieces could be added by creating new subclasses that implement their own capture behavior.

## Cons and Tradeoffs

For this problem, I chose not to create a dedicated `Board` class. Since there are only two pieces and no obstacles or interactions beyond capture checks, a separate board representation felt unnecessary. The tradeoff is that a full chess implementation would likely benefit from a board class to manage piece placement, movement validation, and more complex game rules.

I also prioritized simplicity over maximum extensibility. The solution is well suited to the requirements of this assignment, but additional refactoring might be useful if the project were expanded into a larger chess simulation.

Since the simulation outcome is random, results vary between runs. A more rigorous analysis could run the simulation thousands of times to estimate the probability of each player winning, rather than relying on a single 15-round game.

## Why Python

I chose Python because it is concise, readable, and well suited for simulation-style problems. It is also my strongest language, which means I can speak confidently to every design decision in a follow-up discussion. Python's syntax allowed me to focus on the problem logic rather than boilerplate code, and its built-in support for random number generation made the coin toss and dice roll mechanics straightforward to implement.
