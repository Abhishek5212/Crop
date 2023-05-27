
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('proj_nb.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index.html")

@app.route('/Find')
def find():
  
    return render_template("Find.html")

  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    
    '''
    For rendering results on HTML GUI
    '''
    N = float(request.args.get('N'))
    P = float(request.args.get('P'))
    K = float(request.args.get('K'))
    temperature = float(request.args.get('temperature'))
    humidity = float(request.args.get('humidity'))
    ph = float(request.args.get('ph'))
    rainfall = float(request.args.get('rainfall'))
    prediction = model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    print(prediction)
    if prediction==['apple']:
        output='Apple'
    if prediction==['banana']:
        output='Banana'
    if prediction==['blackgram']:
        output='Blackgram'
    if prediction==['chickpea']:
        output='chickpea'
    if prediction==['coconut']:
        output='coconut'
    if prediction==['coffee']:
        output='coffee'
    if prediction==['cotton']:
        output='cotton'
    if prediction==['grapes']:
        output='grapes'
    if prediction==['jute']:
        output='jute'
    if prediction==['kidneybeans']:
        output='kidneybeans'
    if prediction==['lentil']:
        output='lentil'
    if prediction==['maize']:
        output='maize'
    if prediction==['mango']:
        output='mango'
    if prediction==['mothbeans']:
        output='mothbeans'
    if prediction==['mungbean']:
        output='mungbean'
    if prediction==['muskmelon']:
        output='muskmelon'
    if prediction==['orange']:
        output='orange'
    if prediction==['papaya']:
        output='papaya'
    if prediction==['pigeonpeas']:
        output='pigeonpeas'
    if prediction==['pomegranate']:
        output='pomegranate'
    if prediction==['rice']:
        output='rice'
    
    else:
        output='watermelon'
        
    return render_template('Find.html', prediction_text='Model has predicted that you should grow : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
