from vector2 import Vector2
from gui import Gui
from gameobject import GameObject
from world import World

"""
Jáchym Nácovský
9.12.2024
"""

class Game:
    """Spuštění herní smyčky"""
    def __init__(self, world: World, hero: GameObject, home: GameObject):
        self.world = world
        self.hero = hero
        self.home = home
        self.gui = Gui(world.width, world.height)

    def run(self) -> bool:
        while True:
            self.gui.clear()
            self.world.draw(self.gui)
            self.hero.draw(self.gui)
            self.home.draw(self.gui)
            self.gui.show()

            if self.hero.position == self.home.position:
                return True

            move = self.gui.input_direction()
            new_position = self.hero.position + move
            if not self.world.is_empty(new_position):
                return False

            self.hero.move(move)
