from flask import request, jsonify
from app import app
from fish_tank.tank import FishTank


tank = FishTank()


@app.route('/tank', methods=['GET'])
def current_tank():
    """
    Provides information about the current state of the fish tank.

    This function responds to GET requests on the '/tank' endpoint and returns a JSON object containing the following information:

    * `fish_types` (list[str]): A list of all available fish types in the tank.
    * `fish_list` (list[dict]): A list of dictionaries representing the fish currently in the tank. (e.g., name, food_required).
    * `days_until_cleaning` (int): The estimated days until the tank needs cleaning based on the current number of fish.
    * `total_food_required` (float): The total daily food requirement for all fish in the tank.

    Returns:
        JSON: A dictionary containing information about the current tank state.
    """
    fish_types = list(tank.fish_types.keys())
    fish_list = list(tank.fish_list)
    days_until_cleaning = tank.days_until_cleaning()
    total_food_required = tank.food_required()
    return jsonify({'fish_types': fish_types,
                    'fish_list': fish_list,
                    'days_until_cleaning': days_until_cleaning,
                    'total_food_required': total_food_required})    


@app.route('/add_fish', methods=['POST'])
def add_fish():
    """
    Adds a new fish to the fish tank based on data received in a JSON POST request.

    This function expects a JSON request body containing the following keys:

    * `fish_type` (str): The type of fish to be added.
    * `fish_name` (str): The desired name for the fish.

    Returns:
        JSON: A dictionary containing a message on success or an error message on failure. 
        The response also includes the following information on success:
            * `total_food_required` (float): The total daily food requirement for all fish in the tank after adding the new fish.
            * `days_until_cleaning` (int): The estimated days until the tank needs cleaning after adding the new fish.

    Raises:
        400 Bad Request: If the request data is missing required fields (`fish_type` or `fish_name`) or if the specified fish type is not found in the tank's fish_types dictionary.
    """
    data = request.json
    fish_type = data['fish_type']
    fish_name = data['fish_name']
    
    if not fish_type or not fish_name:
            return jsonify({"error": "Fish type and name are required"}), 400
    
    fish_class = tank.fish_types.get(fish_type)
    if not fish_class:
        return jsonify({'error': 'Fish type not found.'}), 400
    
    fish = fish_class(fish_name)
    tank.add_fish(fish)
    return jsonify({'message': 'Fish added successfully.',
                    'total_food_required': tank.food_required(),
                    'days_until_cleaning': tank.days_until_cleaning()}), 200
