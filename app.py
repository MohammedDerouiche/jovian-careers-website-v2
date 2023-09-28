from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_hello():
    return "hello, world from mohammed der"

if __name__ != "main":
    app.run(host="0.0.0.0", debug=True)
