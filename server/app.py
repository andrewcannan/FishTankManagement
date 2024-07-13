from flask import Flask
from routes import *
from fish_tank.tank import FishTank

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)