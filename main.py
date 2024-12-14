
"""
Jáchym Nácovský
9.12.2024
"""
""" Hlavní program """
if __name__ == "__main__":
    from vector2 import Vector2
    from gameobject import GameObject
    from world import World
    from game import Game

    data = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    symbols = [" ", "#"]
    world = World(data, symbols)
    hero = GameObject(Vector2(1, 1), "@")
    home = GameObject(Vector2(4, 1), "^")

    game = Game(world, hero, home)
    if game.run():
        print("Vítej doma!")
    else:
        print("... a už ho nikdy nikdo neviděl...")