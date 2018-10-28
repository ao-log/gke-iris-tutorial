from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def __predict(user_input):
    backend_url = 'http://predict-service.default.svc.cluster.local:8081'
    iris = [v for k, v in user_input.items()]
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        backend_url + '/predict',
        json.dumps({'data':[iris]}),
        headers=headers)
    result = response.json()

    if result['predicted_class'] == [0]:
        return 'setosa'
    elif result['predicted_class'] == [1]:
        return 'versicolor'
    elif result['predicted_class'] == [2]:
        return 'virginica'

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        return render_template(
            'result.html',
            result =  __predict(request.form))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

