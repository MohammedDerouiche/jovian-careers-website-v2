from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db #, all_application_to_db

app = Flask(__name__)

@app.route("/")
def hello_hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/api/jobs/<id>")
def show_job_json(id):
    job = load_job_from_db(id)
    return jsonify(job)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply",methods=['POST'])
def apply_to_job(id):
    application = request.form
    job = load_job_from_db(id)
    # all_application_to_db(id, application) # to work on later
    return render_template('application_submitted.html', application=application, job=job)



# if __name__ != "main":
#     app.run(debug=True)
