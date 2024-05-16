from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
fmodel = pickle.load(open('classifier1.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('to_predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    Nitrogen = request.form.get('Nitrogen')
    Potassium = request.form.get('Potassium')
    Phosphorous = request.form.get('Phosphorous')

    # prediction
    if(int(Nitrogen) > 100 or int(Potassium) > 100 or int(Phosphorous) > 100):
        result='Enter a value between 0 and 100'
        return render_template('error.html', result=result)
    if(int(Nitrogen) < 0 or int(Potassium) < 0 or int(Phosphorous) < 0):
        result='Enter a positive value'
        return render_template('error.html', result=result)
    result = fmodel.predict(np.array([[Nitrogen, Potassium, Phosphorous]]))
    # ... (rest of your code)
    if result[0] == 0:
        result = "TEN-TWENTY SIX-TWENTY SIX"
    elif result[0] == 1:
        result = "Fourteen-Thirty Five-Fourteen"
    elif result[0] == 2:
        result = "Seventeen-Seventeen-Seventeen"
    elif result[0] == 3:
        result = "TWENTY-TWENTY"
    elif result[0] == 4:
        result = "TWENTY EIGHT-TWENTY EIGHT"
    elif result[0] == 5:
        result = "DAP"
    else:
        result = "UREA"
    
    return render_template('predict.html', result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
