from .fish import Fish, Goldfish, Angelfish, Babelfish
from datetime import datetime

class FishTank:
    """
    This class allows you to add fish, track food requirements, and manage the tank's cleaning schedule.

    Attributes:
        fish_list (list[Fish]): A list containing all the fish objects currently in the tank.
        days_until_cleaning (int): The estimated number of days until the tank needs cleaning based on the number of fish.
        fish_types (dict[str, Fish]): A dictionary that maps fish type names (strings) to their corresponding fish class objects.
    """
    def __init__(self):
        self.fish_list = []
        self.days_until_cleaning = 30
        self.fish_types = {
            'Goldfish': Goldfish,
            'Angelfish': Angelfish,
            'Babelfish': Babelfish
        }
        self.last_updated = datetime.now()
    
    
    def add_fish(self, fish: Fish):
        """
        Adds a fish object to the fish tank and reduces the days_until_cleaning by 1.

        Args:
            fish (Fish): The fish object to be added to the tank.
        """
        self.fish_list.append(fish)
        self.days_until_cleaning -= 1
    
    
    def add_fish_type(self, fish_type: str, food_required: float):
        """
        Adds a new fish type to the fish_types dictionary.

        Args:
            fish_type (str): The name of the new fish type.
            food_required (float): The amount of food required by this fish type per day.

        Raises:
            ValueError: If the fish type already exists in the dictionary.
        """
        if fish_type in self.fish_types:
            raise ValueError(f'Fish type {fish_type} already exists.')
        
        class NewFish(Fish):
            def __init__(self, name: str):
                self.name = name
                
            def food_required(self) -> float:
                return food_required
                
        self.fish_types[fish_type] = NewFish
    
    
    def food_required(self) -> float:
        """
        Calculates the total amount of food required by all fish in the tank.

        Returns:
            float: The total daily food requirement for all fish in the tank.
        """
        return sum(fish.food_required() for fish in self.fish_list)
    
    
    def days_until_cleaning(self) -> int:
        """
        Returns the estimated number of days until the tank needs cleaning.

        Returns:
            int: The estimated days until cleaning based on the number of fish.
        """
        return self.days_until_cleaning
    
    
    def reset_days_until_cleaning(self) -> int:
        """
        Resets the days_until_cleaning attribute to 30 minus the number of fish in the tank.
        """
        self.days_until_cleaning = 30 - len(self.fish_list)