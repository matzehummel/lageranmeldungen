from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/registration', methods=['POST'])
@cross_origin()
def submit_data():
    print(request)
    data = request.get_json()
    print(data)
    # do something with the data
    return 'Data received: {}'.format(data)

if __name__ == '__main__':
    app.run(debug=True)