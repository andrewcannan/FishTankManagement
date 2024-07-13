from .fish import Fish, Goldfish, Angelfish, Babelfish

class FishTank:
    def __init__(self):
        self.fish_list = []
        self.days_until_cleaning = 30
        self.fish_types = {
            'Goldfish': Goldfish,
            'Angelfish': Angelfish,
            'Babelfish': Babelfish
        }