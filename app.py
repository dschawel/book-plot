# Flask app
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
import random 

# Database set up
client = MongoClient('mongodb://localhost:27017')
db = client['characters']
db = client['victims']
db = client['plots']

# Declaring app instance
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    def get_random_doc():
        count = plots.count()
        return plots.find()[random.randrange(count)]
    return render_template('home.html')
        
@app.route('/characters', methods=('GET', 'POST'))
def characters():
    if request.method == 'GET':
        characters = list(db.characters.find())
        return render_template('characters.html', characters=characters)
    elif request.method == 'POST':
        db.characters.insert_one({
            'character': request.form['character']
        })
        return redirect('/characters')

@app.route('/victims', methods=('GET', 'POST'))
def victims():
    if request.method == 'GET':
        victims = list(db.victims.find())
        return render_template('victims.html', victims=victims)
    elif request.method == 'POST':
        db.victims.insert_one({
            'victim': request.form['victim']
        })
        return redirect('/victims')

@app.route('/plots', methods=('GET', 'POST'))
def plots():
    if request.method == 'GET':
        plots = list(db.plots.find())
        return render_template('plots.html', plots=plots)
    elif request.method == 'POST':
        db.plots.insert_one({
            'plot': request.form['plot']
        })
        return redirect('/plots')
        
# Getting the server up and running
if __name__ == '__main__':
    app.run(port=5000, debug=True)