# Fish Tank Management
<br>

* [Brief](#brief)
* [Design Overview](#design-overview)
* [Fish Tank Library](#fish-tank-library)
* [Fish Tank API](#fish-tank-api)
<br>

## Brief

In a language of your choosing:

I need a new system to help me manage my fish tank. Don’t worry about the UI: I will build that.
<br>

The library should satisfy the following user stories and demonstrate your design, coding and
testing abilities.
<br>
 
Here are the user stories:

1. A user should be able to add 3 types of fish to the tank (Goldfish, Angel fish, Babel
fish) and name the fish.
2. The amount of food required for each fish is as follows:
    * a. 0.1g for each Goldfish
    * b. 0.2g for each Angel fish
    * c. 0.3g for each Babel fish
3. A user should be able to see how much food is needed to feed the fish in the tank.
4. Every 30 days the tank needs cleaning but each time a fish is added the number of
days is reduced by 1. As a user I should be able to see the number of days until
cleaning is required.

Ensure the design allows me to add more types of fish in the future without having to change
the code.

## Design Overview

**Design Decisions**:

* Using a Python package provides a reusable library for managing the fish tank.
* Separating fish types and tank logic offers modularity and easier expansion.
* The abstract Fish class promotes code maintainability for future fish types.

**User Stories**:

* Adding Fish: The ``FishTank.add_fish`` method allows adding various fish types (```Goldfish```, ```Angelfish```, ```Babelfish```) with custom names by creating instances of the corresponding classes.
* Food Requirements: Specific fish classes (```Goldfish```, ```Angelfish```, ```Babelfish```) implement the ```food_required``` method to return their daily food amount. The ```FishTank.food_required``` method calculates the total food needed for all fish.
* Cleaning Schedule: The ```days_until_cleaning``` attribute tracks the estimated days before cleaning. Adding fish reduces this value by 1.

New fish types can be added by creating classes inheriting from ```Fish``` and implementing ```food_required``` without modifying existing code. The ```fish_types``` dictionary in ```FishTank``` automatically incorporates them.

**Future Implementations**:

* Tracking Cleaning Schedule: The current last_updated attribute and update_days_until_cleaning method offer the ability to implement a scheduled update of tank_status for the user, so long as the session persists.
* Reset Cleaning Schedule : The current reset_days_until_cleaning methods offers the ability for the user to update the tank_status after a clean has been performed.

Endpoints for each would need to be created.

**Alternative Approach**:

While the provided Python library offers a solid solution, an alternative approach could utilize a relational database and a web API for managing the fish tank.

This method involves creating three tables:

* ```fish``` to store individual fish information
* ```fish_type``` to define various fish species and their daily food requirements
* ```tank_status``` to track the estimated days until cleaning.
* Initial ```fish_types``` and ```tank_status``` could be defined as defult values.

 A similar web API would interact with this database, enabling CRUD functionalities like adding new fish, retrieving information about existing fish, calculating total daily food requirements, updating the cleaning schedule as fish are added, and monitoring the current status of the tank. The benefit to this approach would be the persistence of data between sessions, but as a library was mentioned in the brief I created a standalone python package/library and a RESTful API that utilizes it.

## Fish Tank Library

This library provides a Python class (FishTank) to simulate a virtual fish tank and manage its inhabitants. It allows you to:

**Fish Management**:

* Add Fish: You can introduce various fish species by creating instances of their corresponding fish classes (e.g., ```Goldfish```, ```Angelfish```) in fish.py or dynamically adding new fish types using the ```add_fish_type``` method.
* Control Over Fish Types:
    * Abstract Fish Class: The Fish class serves as an abstract base class, defining a common interface (```name``` attribute and ```food_required``` abstract method) for all fish types. Specific fish classes (e.g., ```Goldfish```, ```Angelfish```) inherit from ```Fish``` and provide concrete implementations for ```food_required```.
    * Dynamic Fish Type Addition: The ```add_fish_type``` method enables you to introduce new fish types during runtime by specifying the fish type name and its daily food requirement.

**Monitoring and Maintenance**:

* Track Food Requirements: The ```food_required``` method calculates the total amount of food needed daily for all fish in the tank.
* Manage Cleaning Schedule: 
    * The ```days_until_cleaning``` attribute displays the remaining days before the tank requires cleaning based on the number of fish (initially set to 30 days). The ```reset_days_until_cleaning``` method allows you to manually reset this estimate.
    * The ```update_days_until_cleaning``` method automatically updates the ```days_until_cleaning``` attribute based on the time elapsed since the last update. It calculates the number of days that have passed and subtracts that value from ```days_until_cleaning``` if necessary. It also updates the ```last_updated``` attribute to the current time.

**Usage**:

* Create FishTank: Instantiate a ```FishTank``` object to represent your virtual fish tank.
* Add Fish - Add fish to the tank using the following approaches:
    * Create fish objects of existing classes (e.g., ```goldfish = Goldfish()```).
    * Use the ```add_fish_type``` method to define new fish types and then create instances of those types.
    * Call the ```add_fish``` method on the ```FishTank``` object, passing the fish object as an argument.
* Manage Food and Cleaning:
    * Use the ```food_required``` method to determine the total daily food amount for all fish in the tank.
    * Query the ```days_until_cleaning``` attribute to check the days remaining before cleaning is needed.
    * Use the ```reset_days_until_cleaning``` method to manually reset the cleaning estimate if necessary.
    * Utilize the ```get_tank_status``` method to retrieve a comprehensive overview of the tank's current state.
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
* ```test_update_days_until_cleaning```: Verifies that the ```update_days_until_cleaning``` method correctly updates the ```days_until_cleaning``` attribute based on the elapsed time since the last update.
<br>

## Fish Tank API

This section describes the API endpoints available for interacting with the Fish Tank application. The API uses JSON for data exchange and follows RESTful principles.

**Flask Dependencies**:

The Fish Tank application utilizes Flask, a lightweight web framework for Python. Server can be initalised by changing into the root directory and running the command ```flask run``` (so long as flask and python is installed).

**Global Fish Tank Instance**:

The application maintains a single ```FishTank``` object (```tank```) to represent the virtual fish tank.

**Endpoints**:

1. GET ```/tank```

* Description: This endpoint provides information about the current state of the fish tank.
* Method: GET
* Response: JSON object containing:
    * ```fish_types``` (list[str]): A list of all available fish types in the tank.
    * ```fish_list``` (list[dict]): A list of dictionaries representing the fish currently in the tank.
    * ```days_until_cleaning``` (int): The estimated days until the tank needs cleaning based on the current number of fish.
    * ```total_food_required``` (float): The total daily food requirement for all fish in the tank.
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

**Testing the API**:

The API includes unit tests written in pytest to ensure the code behaves as expected. To run these tests, you'll need to have pytest installed.

* ```test_current_tank```: Verifies that the ```/tank``` endpoint returns the expected response with initial fish tank data.
* ```test_add_fish```: Tests adding a new fish and checks the response and updated tank state.
* ```test_tank_after_adding_fish```: Confirms that the fish details are reflected after adding a fish.
* ```test_add_fish_type```: Tests adding a new fish type and verifies the success message.
* ```test_missing_data_add_fish```: Ensures appropriate error handling for missing data in the ```/add_fish``` request.
* ```test_missing_data_add_fish_type```: Checks for error handling when required data is missing in the ```/add_fish_type``` request.
* ```test_add_duplicate_fish_type```: Verifies that adding a duplicate fish type results in an error.
* ```test_add_non_existent_fish_type```: Tests adding a fish with a non-existent fish type and checks the error response.