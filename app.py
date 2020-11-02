import numpy as np

from flask import Flask, request, jsonify, render_template

import pickle

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])

def predict():
    
    init_features=[int(x) for x in request.form.values()]
    final_vals=[np.array(init_features)]
    
    prediction=model.predict(final_vals)
    
    otp=round(prediction[0],2)
    
    return render_template("index.html",prediction_text="Employee Salary is :$ "+str(otp))

if "__name__"=="__main__":
    app.run(debug=True)
    
