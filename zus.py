import random

class Piece:
    def __init__(self, file, rank, color):
        self.file = file
        self.rank = rank
        self.color = color

class Bishop(Piece):
    def can_capture(self, other):
        return abs(self.file - other.file) == abs(self.rank - other.rank)

class Rook(Piece):
    def can_capture(self, other):
        return self.file == other.file or self.rank == other.rank

    def move(self, direction, steps):
        if direction == "up":
            self.rank = (self.rank - 1 + steps) % 8 + 1
        elif direction == "right":
            self.file = (self.file - 1 + steps) % 8 + 1

rook = Rook(file=8, rank=1, color="black")
bishop = Bishop(file=3, rank=3, color="white")

for round_num in range(1, 16):
    coin = random.choice(["heads", "tails"])
    direction = "up" if coin == "heads" else "right"
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    steps = dice1 + dice2
    rook.move(direction, steps)
    file_letter = chr(ord("a") + rook.file - 1)
    position = f"{file_letter}{rook.rank}"
    print(
        f"Round {round_num}: "
        f"Coin={coin}, "
        f"Dice={dice1}+{dice2}={steps}, "
        f"Rook moves {direction} to {position}"
    )
    if bishop.can_capture(rook):
        print(f"Bishop captures rook at {position}. White wins.")
        break
else:
    print("Rook survived all 15 rounds. Black wins.")