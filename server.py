from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add(first, second):
    data = request.get_json()  # Assuming JSON data in the request
    first = data.get('first')
    second = data.get('second')
    result = first + second
    return result
    
@app.route("/calculator/subtract", methods=['POST'])
def subtract(first, second):
    data = request.get_json()  # Assuming JSON data in the request
    first = data.get('first')
    second = data.get('second')
    result = first - second
    return result

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
