from abc import ABC, abstractmethod

class Fish(ABC):
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def food_required(self) -> float:
        pass
    
class Goldfish(Fish):
    def food_required(self) -> float:
        return 0.1
    
class Angelfish(Fish):
    def food_required(self) -> float:
        return 0.2
    
class Babelfish(Fish):
    def food_required(self) -> float:
        return 0.3