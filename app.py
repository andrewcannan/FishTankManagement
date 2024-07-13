from flask import Flask
from fish_tank.tank import FishTank

app = Flask(__name__)
tank = FishTank()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)