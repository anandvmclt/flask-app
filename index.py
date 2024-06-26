# index.py

# Importing the Flask class from the flask module
from flask import Flask

# Creating an instance of the Flask class with the name of the current module (__name__) as argument
app = Flask(__name__)

# Defining a route for the root URL ("/") that responds to HTTP GET requests


@app.route('/')
def hello():
    # Returning a string "Hello from Python Flask App!" as the response
    return "Hello from Python Flask App!"

@app.route('/home')
def home():
    # Returning a string "Jai Sree Ganesh !" as the response
    return "Jai  Ganesh !"


@app.route('/about')
def about():
    # Returning a about page as the response
    return "About Us Page Added !"


# Entry point of the application. This block ensures that the app is run only if executed directly, not imported as a module.
if __name__ == '__main__':
    # Running the Flask application on the specified host ('0.0.0.0') and port (5000)
    app.run(host='0.0.0.0', port=5000)