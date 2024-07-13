from abc import ABC, abstractmethod

class Fish(ABC):
    """
    An abstract base class representing a fish.

    This class defines a common interface for various fish species,
    specifying their `name` attribute and the abstract method `food_required`.

    Attributes:
        name (str): The name of the fish.

    Methods:
        food_required(self) -> float (abstract):
            Calculates the amount of food required by the fish,
            specific implementation depends on the fish species, must be overridden.
    """
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def food_required(self) -> float:
        pass


class Goldfish(Fish):
    """
    A specific type of fish known as a Goldfish.

    Inherits from the Fish base class and implements the `food_required`
    method to provide a specific value for Goldfish.
    """
    def food_required(self) -> float:
        return 0.1

  
class Angelfish(Fish):
    """
    A specific type of fish known as an Angelfish.

    Inherits from the Fish base class and implements the `food_required`
    method to provide a specific value for Angelfish.
    """
    def food_required(self) -> float:
        return 0.2


class Babelfish(Fish):
    """
    A specific type of fish known as a Babelfish.

    Inherits from the Fish base class and implements the `food_required`
    method to provide a specific value for Babelfish.
    """
    def food_required(self) -> float:
        return 0.3