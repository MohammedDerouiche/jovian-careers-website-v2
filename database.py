from sqlalchemy import create_engine, text
from DBconf import dbname, host, password, userName

engine = create_engine(f"mysql+pymysql://{userName}:{password}@{host}/{dbname}?charset=utf8mb4")

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        resultList = result.fetchall()
        jobsList = []
        for row in resultList:
            row_dict = row._asdict()  # Convert the row to a dictionary
            jobsList.append(row_dict)
        
        return jobsList

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from jobs where id = {id}"))

        job = result.fetchall()
        if len(job) ==0:
            return None
        else:
            return job[0]._asdict()


# This aproach is likely the must efficiante, but it didn't work

# def all_application_to_db(job, application):
#     with engine.connect() as conn:
#         query = text("insert into application (job_id, full_name, email, linkedin_url, education, experience, resume_url) values (?, ?, ?, ?, ?, ?, ?)")
#         conn.execute(query,{ 
#                      "job_id": job['id'], 
#                      "full_name" : application['full_name'],
#                      "email": application['email'],
#                      "linkedin_url" : application['linkedin_url'],
#                      "education" : application['education'],
#                      "working_experience" : application['working_experience'],
#                      "resume_url" : application['resume_url']
#                     }
#                     )

# This is another approach using formated string, but it's not secure cause to sql injection.

# def all_application_to_db(job, application):
#     job_id=job['id'],
#     full_name=application['full_name'],
#     email=application['email'],
#     linkedin_url=application['linkedin_url'],
#     education=application['education'],
#     working_experience=application['working_experience'],
#     resume_url=application['resume_url']

#     with engine.connect() as conn:
#         query = text(f"insert into application (job_id, full_name, email, linkedin_url, education, working_experience, resume_url) values ({job_id}, {full_name}, {email}, {linkedin_url}, {education}, {working_experience}, {resume_url})")
#         conn.execute(query,
#         )
