from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
        
    def make_move(self):
        new_position = random.choice(self.moves)
        new_x = self.position[0] + new_position[0]
        new_y = self.position[1] + new_position[1]
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0), (-1,0), (0,1), (0,-1)]

    def level_up(self):
        self.moves.append((1,1))
        self.moves.append((1,-1))
        self.moves.append((-1,1))
        self.moves.append((-1,-1))
        
player1 = Pawn()

print(f"Initial position: {player1.position}")

print("\n--- Moving (Level 1) ---")
for i in range(3):
    pos = player1.make_move()
    print(f"Movement {i+1}: the player moved to {pos}")

print("\n--- LEVEL UP! ---")
player1.level_up()
print("Now the pawn can move diagonally.")
print(f"Current possible moves: {player1.moves}")

print("\n--- Moving (Level 2) ---")
for i in range(3):
    pos = player1.make_move()
    print(f"Movement {i+1}: the player moved to {pos}")

print("\n--- Complete history (Path) ---")
print(player1.path)