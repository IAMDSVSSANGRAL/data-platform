from dagster import job, op

@op
def hello():
    print("Hello from Dagster")

@job
def hello_job():
    hello()