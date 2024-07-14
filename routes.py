from flask import request, jsonify
from app import app, tank


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
    tank_status = tank.get_tank_status()
    return jsonify(tank_status), 200    


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
    try:
        data = request.json
        fish_type = str(data['fish_type'])
        fish_name = str(data['fish_name'])
    except KeyError:
        return jsonify({"error": "Fish type and name are required."}), 400
    
    fish_class = tank.fish_types.get(fish_type)
    if not fish_class:
        return jsonify({'error': 'Fish type not found.'}), 400
    
    fish = fish_class(fish_name)
    tank.add_fish(fish)
    tank_status = tank.get_tank_status()
    return jsonify({'message': 'Fish added successfully.',
                    'tank_status': tank_status}), 200

    
@app.route('/add_fish_type', methods=['POST'])
def add_fish_type():
    """
    Adds a new fish type to the fish tank based on data received in a JSON POST request.

    This function expects a JSON request body containing the following keys:

    * `fish_type` (str): The name of the new fish type to be added.
    * `food_required` (float): The daily food requirement for this fish type.

    Returns:
        JSON: A dictionary containing a message on success or an error message on failure.

    Raises:
        400 Bad Request: If the request data is missing required fields (`fish_type` or `food_required`) or if adding the fish type results in a `ValueError` (e.g., attempting to add a duplicate fish type).

    """
    try:
        data = request.json
        fish_type = str(data['fish_type']).strip()
        food_required = float(data['food_required'])
    except KeyError:
        return jsonify({"error": "Fish type and food amount are required."}), 400
    except ValueError:
        return jsonify({"error": "Food amount must be a valid number. E.g - 0.1"}), 400
    
    if not fish_type:
        return jsonify({"error": "Fish type must be provided as a non-empty string."}), 400
        
    
    try:
        tank.add_fish_type(fish_type, food_required)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({'message': f'New fish type {fish_type} added successfully.'}), 200
