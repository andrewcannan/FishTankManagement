from abc import ABC, abstractmethod

class Fish(ABC):
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def food_required(self) -> float:
        pass
    