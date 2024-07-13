from flask import request, jsonify
from app import app
from fish_tank.tank import FishTank


tank = FishTank()

@app.route('/get_fish_types', methods=['GET'])
def get_fish_types():
    """
    Retrieves a list of available fish types in the fish tankin response to GET requests.

    Returns:
        JSON: A list containing all the currently available fish types in the tank.
    """
    fish_types = list(tank.fish_types.keys())
    return jsonify(fish_types)


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
