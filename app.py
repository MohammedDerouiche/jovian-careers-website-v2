from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_hello():
    return render_template("home.html")

# if __name__ != "main":
#     app.run(host="0.0.0.0", debug=True)
