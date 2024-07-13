from flask import request, jsonify
from app import app
from fish_tank.tank import FishTank


tank = FishTank()

@app.route('/add_fish', methods=['POST'])
def add_fish():
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
