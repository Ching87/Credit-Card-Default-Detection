from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import os
from sklearn.preprocessing import StandardScaler


model = pickle.load(open('credit_card_default_detection.pkl', 'rb'))
std_scaler = pickle.load(open('std_scaler.pkl', 'rb'))


data = {'IT staff': 0, 'Secretaries': 1, 'Accountants': 2, 'Core staff': 3, 'High skill tech staff': 4,
 'Others': 5, 'Managers': 6, 'Private service staff': 7, 'Medicine staff': 8, 'HR staff': 9,
 'Sales staff': 10, 'Realty agents': 11, 'Security staff': 12, 'Waiters/barmen staff': 13,
 'Cleaning staff': 14, 'Laborers': 15, 'Cooking staff': 16, 'Drivers': 17, 'Low-skill Laborers': 18}
gender_data = {'Male': 1, 'Female': 0}
yes_no_data  = {'Yes':1, 'No':0}


app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['Age'])

        gender = str(request.form['Gender'])
        gen = gender_data[gender]

        total_family_members = int(request.form['Total family members'])
        owns_house = str(request.form['own_house'])
        house = yes_no_data[owns_house]
        owns_car = str(request.form['own_car'])
        car = yes_no_data[owns_car]

        occupation = str(request.form['Occupation'])
        occupation = data[occupation]

        migrant_worker = str(request.form['migrant'])
        migrant = yes_no_data[migrant_worker]

        no_of_days_employed = int(request.form['days employed'])
        yearly_debt_payments = float(request.form['yearly deft payments'])
        credit_limit = float(request.form['Credit Limit'])
        credit_limit_used = float(request.form['Credit Limit used(%)'])
        credit_score = float(request.form['Credit Score'])
        prev_defaults = float(request.form['previous defaults'])

        

        x = [[age, gen, total_family_members, house, car, occupation, migrant,
              no_of_days_employed, yearly_debt_payments, credit_limit, credit_limit_used, credit_score,
              prev_defaults]]

        x_input = std_scaler.transform(x)

        prediction = model.predict(x_input)
        return render_template('predict.html', prediction = prediction)

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port =port)