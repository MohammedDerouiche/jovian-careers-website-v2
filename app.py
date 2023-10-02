from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        "title" : "Data Scintist",
        "location" : "Algeria, alger",
        'salary' : 'RS. 10,10,100'
    },
    {
        'id' : 2,
        "title" : "Data Analyst",
        "location" : "Algeria, el-oued",
        'salary' : 'RS. 10,10,100'
    },
    {
        'id' : 3,
        "title" : "Front-End Engineer",
        "location" : "Egybt, alexandia",
        'salary' : 'RS. 12,10,100'
    },
    {
        'id' : 4,
        "title" : "Back-End Engineer",
        "location" : "Tunisia, Sousa",
        'salary' : 'RS. 20,10,100'
    }
]

@app.route("/")
def hello_hello():
    return render_template("home.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ != "main":
    app.run(debug=True)
