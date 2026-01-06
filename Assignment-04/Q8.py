# Concept: Instance & Class Attributes
# Q8. Create a class Player with:
# • a class variable player_count
# • instance variables name and level
# Track how many players were created.

class Player:
    player_count = 0   # class variable

    def __init__(self, name, level):
        self.name = name        # instance variable
        self.level = level      # instance variable
        Player.player_count += 1

    def instance_variable(self):
        print(f"Player name is {self.name} and level is {self.level}")


play1 = Player('Shivam', 6)
play2 = Player('Archit', 4)

play1.instance_variable()
play2.instance_variable()

print(f"Total players created: {Player.player_count}")