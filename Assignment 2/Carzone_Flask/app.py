from flask import Flask, render_template, url_for, request, redirect
from werkzeug.datastructures import ImmutableMultiDict
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import foo
import pandas as pd
import plotly.express as px
import plotly
import os

app = Flask(__name__)
app.secret_key = "JabWeMet"  


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cars.db"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcar', methods=['GET', 'POST'])
def addcar():
    if request.method == 'POST':
        content = json.dumps(request.form)
    
        new_car = Car(content=content)
        db_err = foo.db_add_one(new_car, db)    
        
        if db_err is not None:
            return db_err
        
        return redirect('/viewtable')
    
    else:
        return render_template('addcar.html')
    
    
@app.route('/viewtable', methods=['GET', 'POST'])
def viewtable():
    try:
        cars = Car.query.order_by(Car.id).all() 
        for car in cars:
            car.content = ImmutableMultiDict(json.loads(car.content))
    except:
        pass
    
    if request.method == 'POST':
        pass
    else:
        return render_template('viewtable.html', cars = cars)


@app.route('/viewgraph', methods=['GET', 'POST'])
def viewgraph():
    # try:
    #     cars = Car.query.order_by(Car.id).all() 
    #     for car in cars:
    #         car.content = ImmutableMultiDict(json.loads(car.content))
    # except:
    #     pass
    
    # cars_content = []
    # for car in cars:
    #     car.content = dict(car.content)
    #     cars_content += [car.content]
    
    # df = pd.DataFrame(cars_content)
    
    # df.sort_values("Price", inplace=True)
    
    # fig = px.scatter(df, x='Year', y='Price', color='Make')
    # fig.update_xaxes(range=[1990, 2024])
    # fig['layout']['yaxis'].update(autorange = True)
    # fig.show()
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # return render_template('viewgraph.html', graphJSON = graphJSON)
    return render_template('viewgraph.html')


@app.route('/graphone', methods=['GET', 'POST'])
def graphone():
    try:
        cars = Car.query.order_by(Car.id).all() 
        for car in cars:
            car.content = ImmutableMultiDict(json.loads(car.content))
    except:
        pass
    
    cars_content = []
    for car in cars:
        car.content = dict(car.content)
        cars_content += [car.content]
    
    df = pd.DataFrame(cars_content)
    
    df.sort_values("Price", inplace=True)
    
    fig = px.scatter(df, x='Year', y='Price', color='Make')
    fig.update_xaxes(range=[1990, 2024])
    fig['layout']['yaxis'].update(autorange = True)
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('viewgraph.html', graphJSON = graphJSON)


@app.route('/graphtwo', methods=['GET', 'POST'])
def graphtwo():
    try:
        cars = Car.query.order_by(Car.id).all() 
        for car in cars:
            car.content = ImmutableMultiDict(json.loads(car.content))
    except:
        pass
    
    cars_content = []
    for car in cars:
        car.content = dict(car.content)
        cars_content += [car.content]
    
    df = pd.DataFrame(cars_content)
    
    data = dict(
        character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

    fig = px.sunburst(
        df,
        names='County',
        parents='Make',
        values='Price',
    )
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('viewgraph.html', graphJSON = graphJSON)


@app.route('/uploadcsv', methods=['GET', 'POST'])
def uploadcsv():

    if request.method == 'POST':
        f = request.files['File']
        df = pd.read_csv(f)
        for index, row in df.iterrows():
            car_dict = {k: row[k] for k in ['Name', 'Year', 'Price', 'Make', 'Model', 'Engine', 'Fuel', 'Odometer', 'Transmission', 'Body', 'County', 'Doors', 'Color', 'Owners', 'Tax-Expiry', 'NCT-Expiry']}
            car_json = json.dumps(car_dict)
            new_car = Car(content=car_json)
            db_err = foo.db_add_one(new_car, db)
            
            if db_err is not None:
                return db_err
            
        return redirect('/')
    
    else:
        return render_template('uploadcsv.html')


if __name__ == "__main__":
    app.run(debug=True)