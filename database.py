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

    
