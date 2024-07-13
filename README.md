# Fish Tank Management
<br>

* [Fish Tank Library](#fish-tank-library)
<br>

## Fish Tank Library

This library provides a Python class (FishTank) to simulate a virtual fish tank and manage its inhabitants. It allows you to:

* Add Fish: You can introduce various fish species by creating instances of their corresponding fish classes (e.g., ```Goldfish```, ```Angelfish```) in ```fish.py``` or dynamically adding new fish types using the ```add_fish_type``` method.
* Track Food Requirements: The ```food_required``` method calculates the total amount of food needed daily for all fish in the tank.
* Manage Cleaning Schedule: The ```days_until_cleaning``` method estimates the remaining days before the tank requires cleaning based on the number of fish (initially set to 30 days). The ```reset_days_until_cleaning``` method allows you to manually reset this estimate.

Control over Fish types:

* Abstract Fish Class: The Fish class serves as an abstract base class, defining a common interface (```name``` attribute and ```food_required``` abstract method) for all fish types. An abstract class cannot be instantiated directly and abstract methods must be implemented by any subclass. Specific fish classes (e.g., ```Goldfish```, ```Angelfish```) inherit from Fish and provide concrete implementations for ```food_required```.
* Dynamic Fish Type Addition: The ```add_fish_type method``` enables you to introduce new fish types during runtime by specifying the fish type name and its daily food requirement.


Usage:

* Create FishTank: Instantiate a ```FishTank``` object to represent your virtual fish tank.
* Add Fish - Add fish to the tank using the following approaches:
    * Create fish objects of existing classes (e.g., ```goldfish = Goldfish()```).
    * Use the ```add_fish_type``` method to define new fish types and then create instances of those types.
    * Call the ```add_fish``` method on the ```FishTank``` object, passing the fish object as an argument.
* Manage Food and Cleaning:
    * Use the ```food_required``` method to determine the total daily food amount for all fish in the tank.
    * Call the ```days_until_cleaning``` method to check the estimated days remaining before cleaning is needed.
    * Use the ```reset_days_until_cleaning``` method to manually reset the cleaning estimate if necessary.