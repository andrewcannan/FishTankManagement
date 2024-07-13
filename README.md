# Fish Tank Management
<br>

* [Fish Tank Library](#fish-tank-library)
* [Fish Tank API](#fish-tank-api)
<br>

## Fish Tank Library

This library provides a Python class (FishTank) to simulate a virtual fish tank and manage its inhabitants. It allows you to:

* Add Fish: You can introduce various fish species by creating instances of their corresponding fish classes (e.g., ```Goldfish```, ```Angelfish```) in ```fish.py``` or dynamically adding new fish types using the ```add_fish_type``` method.
* Track Food Requirements: The ```food_required``` method calculates the total amount of food needed daily for all fish in the tank.
* Manage Cleaning Schedule: The ```days_until_cleaning``` method estimates the remaining days before the tank requires cleaning based on the number of fish (initially set to 30 days). The ```reset_days_until_cleaning``` method allows you to manually reset this estimate.

**Control over Fish types**:

* Abstract Fish Class: The Fish class serves as an abstract base class, defining a common interface (```name``` attribute and ```food_required``` abstract method) for all fish types. An abstract class cannot be instantiated directly and abstract methods must be implemented by any subclass. Specific fish classes (e.g., ```Goldfish```, ```Angelfish```) inherit from Fish and provide concrete implementations for ```food_required```.
* Dynamic Fish Type Addition: The ```add_fish_type method``` enables you to introduce new fish types during runtime by specifying the fish type name and its daily food requirement.


**Usage**:

* Create FishTank: Instantiate a ```FishTank``` object to represent your virtual fish tank.
* Add Fish - Add fish to the tank using the following approaches:
    * Create fish objects of existing classes (e.g., ```goldfish = Goldfish()```).
    * Use the ```add_fish_type``` method to define new fish types and then create instances of those types.
    * Call the ```add_fish``` method on the ```FishTank``` object, passing the fish object as an argument.
* Manage Food and Cleaning:
    * Use the ```food_required``` method to determine the total daily food amount for all fish in the tank.
    * Call the ```days_until_cleaning``` method to check the estimated days remaining before cleaning is needed.
    * Use the ```reset_days_until_cleaning``` method to manually reset the cleaning estimate if necessary.
<br>

**Testing**:

The ```fish_tank``` library includes unit tests written in pytest to ensure the code behaves as expected. To run these tests, you'll need to have pytest installed.

The provided tests cover various aspects of the ```FishTank``` class and fish types:

* ```test_initial_tank```: Verifies the initial state of a new ```FishTank``` object.
* ```test_add_fish```: Checks the behavior of adding a single fish to the tank.
* ```test_add_multiple_fish```: Tests adding multiple fish and calculating total food requirements.
* ```test_add_fish_type```: Ensures that new fish types can be added.
* ```test_add_duplicate_fish_type```: Confirms that adding a duplicate fish type raises an error.
* ```test_add_fish_of_new_type```: Tests adding a fish of a newly defined fish type.
* ```test_sum_of_food_required```: Verifies that the total food requirement reflects the food needs of all fish.
* ```test_days_until_cleaning```: Tests how adding and removing fish affects the estimated cleaning days and demonstrates the ```reset_days_until_cleaning``` method.
<br>

## Fish Tank API

This section describes the API endpoints available for interacting with the Fish Tank application. The API uses JSON for data exchange and follows RESTful principles.

**Flask Dependencies**:

The Fish Tank application utilizes Flask, a lightweight web framework for Python. Server can be initalised by changing into the server directory and running the command ```flask run``` (so long as flask and python is installed).

**Global Fish Tank Instance**:

The application maintains a single ```FishTank``` object (```tank```) to represent the virtual fish tank.

**Endpoints**:

1. GET ```/tank```

* Description: This endpoint provides information about the current state of the fish tank.
* Method: GET
* Response: JSON object containing:
    * ```fish_types``` (list[str]): A list of all available fish types in the tank.
    * ```fish_list``` (list[dict]): A list of dictionaries representing the fish currently in the tank. Each dictionary may contain details about the fish depending on your implementation (e.g., name, type).
    * ```days_until_cleaning``` (int): The estimated days until the tank needs cleaning based on the current number of fish.
    * t```otal_food_required``` (float): The total daily food requirement for all fish in the tank.
<br><br>

2. POST ```/add_fish```

* Description: This endpoint allows adding a new fish to the tank.
* Method: POST
* Request Body (JSON):
    * ```fish_type``` (str): The type of fish to be added (e.g., "Goldfish", "Angelfish"). This should correspond to a previously defined fish type or one added using the ```/add_fish_type``` endpoint.
    * ```fish_name``` (str): The desired name for the fish.
* Response: JSON object containing:
    * ```message``` (str): A success message upon adding the fish.
    * ```total_food_required``` (float): The total daily food requirement for all fish in the tank after adding the new fish.
    * ```days_until_cleaning``` (int): The estimated days until the tank needs cleaning after adding the new fish.
* Error Handling:
    * Returns a 400 Bad Request error with a message if required data (```fish_type``` or ```fish_name```) is missing, or if the specified fish type is not found.
<br><br>

3. POST ```/add_fish_type```

* Description: This endpoint allows adding a new fish type to the tank.
* Method: POST
* Request Body (JSON):
    * ```fish_type``` (str): The name of the new fish type to be added.
    * ```food_required``` (float): The daily food requirement for this fish type.
* Response: JSON object containing:
    * ```message``` (str): A success message upon adding the new fish type.
* Error Handling:
    * Returns a 400 Bad Request error with a message if required data (```fish_type``` or ```food_required```) is missing, or if adding the fish type results in a ```ValueError``` (e.g., attempting to add a duplicate fish type).