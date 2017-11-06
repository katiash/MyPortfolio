# Activating your virtualEnvironments
# While in the parent directory to our virtual environments (myEnvironments), 
# activate the virtual environment by typing:

# ------------------------------------------------------------------
# | Mac/Linux: | source flaskEnv/bin/activate                   |
# -------------+----------------------------------------------------
# | Windows command prompt :   | call flaskEnv/Scripts/activate |
# ------------------------------------------------------------------
# | Windows git bash :  |  source flaskEnv/Scripts/activate     |
# ------------------------------------------------------------------


#REQUIRED WITH ANY FLASK APPLICATION

#1. Importing Flask enables us to create the variable
# that is our application (i.e. "app" below).
from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def portfolio_main():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

app.run(debug=True)

# run this file via '*.py'.

#GENERIC ROUTE(S) CREATION FOLLOWS FOLLOWING STRUCTURE:
# @app.route('/some_route')
# def some_function_name():
#   // your code here
