from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello-world-10')
def hello_world():
    return f"Hello World 10", 200

if __name__ == '__main__':
    app.run(debug=True)