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
        
    def add_fish(self, fish: Fish):
        self.fish_list.append(fish)
        self.days_until_cleaning -= 1
        
    def add_fish_type(self, fish_type: str, food_required: float):
        if fish_type in self.fish_types:
            raise ValueError(f'Fish type {fish_type} already exists.')
        
        class NewFish(Fish):
            def __init__(self):
                self.name = fish_type
                
            def food_required(self) -> float:
                return food_required
    
        self.fish_types[fish_type] = NewFish