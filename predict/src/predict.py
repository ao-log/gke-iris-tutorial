from flask import Flask, request, jsonify
from sklearn.externals import joblib

clf = joblib.load('model/iris.joblib')
app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    dat = request.json
    pred = clf.predict(dat['data'])
    return jsonify({"predicted_class": pred.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

