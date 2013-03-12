from blitzcraft import BlitzBot
import blitzcraft.logic as logic

class MyBot(BlitzBot):
    def make_move(self):
        if not logic.basic_detect_five(self.board, self.gem_keys, self.swap):
            if not logic.basic_detect_four(self.board, self.gem_keys, self.swap):
                logic.basic_detect_three(self.board, self.gem_keys, self.swap)
        self.random_move()

b = MyBot()
b.delay = 0.08
#boosts = [4,5]  # Use time boost and bonus multiplier
boosts = []
b.play(boosts)
