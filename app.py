
from flask import Flask,render_template,request
import numpy as np
import pickle
import json

model = pickle.load(open("artifacts/model1.pkl","rb"))

with open("artifacts/columns_name.json","r") as json_file:
    col_name = json.load(json_file)
col_name_list =col_name['col_name']


app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def user_info():
    data = request.form
    print(data)

    user_data = np.zeros(len(col_name_list))
    user_data[0] = data['age']
    user_data[1] = data['gender']
    user_data[2] = data['race']
    user_data[3] = data['driving_experience']
    user_data[4] = data['income']
    user_data[5] = data['credit_score']
    user_data[6] = data['vehicle_ownership']
    user_data[7] = data['vehicle_year']
    user_data[8] = data['postal_code']
    user_data[9] = data['annual_mileage']
    user_data[10] = data['vehicle_type']
    user_data[11] = data['speeding_violations']
    user_data[12] = data['duis']
    user_data[13] = data['past_accidents']

    print(user_data)

    result = model.predict([user_data])

    if result[0] == 0:
        insurance_result = "Approved"
    else: 
        insurance_result = "Not Approved"
    
    print(insurance_result)


    return render_template("result.html",Prediction = insurance_result)



if __name__=='__main__':
    app.run(host='0.0.0.0',port='8585',debug=True)

