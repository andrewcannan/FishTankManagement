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
    
    
    def reset_days_until_cleaning(self) -> int:
        """
        Resets the days_until_cleaning attribute to 30 minus the number of fish in the tank.
        """
        self.days_until_cleaning = 30 - len(self.fish_list)
        

    def update_days_until_cleaning(self):
        """
        Updates the 'days_until_cleaning' attribute based on the time elapsed since the last update.
        """
        now = datetime.now()
        days_passed = (now - self.last_updated).days
        if days_passed > 0:
            self.days_until_cleaning -= days_passed
            self.last_updated = now
            
    
    def get_tank_status(self):
        """
        Gets the current status of the fish tank.

        This function retrieves various data points about the fish tank and returns them as a dictionary. Before retrieving the data, it calls the `update_days_until_cleaning` method to ensure the `days_until_cleaning` attribute is up-to-date.

        The returned dictionary contains the following information:

        * `fish_types`: A list of all the unique fish types currently in the tank (keys from the `fish_types` dictionary).
        * `fish_list`: A list of dictionaries representing each fish in the tank. Each dictionary is the result of calling the `to_dict` method on the corresponding fish object.
        * `days_until_cleaning`: An integer representing the number of days remaining until cleaning is required (based on the `days_until_cleaning` attribute).
        * `total_food_required`: An float representing the total amount of food required for all fish in the tank (presumably calculated by the `food_required` method).

        **Returns:**
            dict: A dictionary containing the current status information about the fish tank.
        """
        self.update_days_until_cleaning()
        fish_list = []
        for fish in self.fish_list:
            fish_dict = {
                'name': fish.name,
                'food_required': fish.food_required()
            }
            fish_list.append(fish_dict)
        return {
            'fish_types': list(self.fish_types.keys()),
            'fish_list': fish_list,
            'days_until_cleaning': self.days_until_cleaning,
            'total_food_required': self.food_required()
        }