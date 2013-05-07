from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def print_hello(name):
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
