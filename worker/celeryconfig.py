import os

port = os.environ["REDIS_PORT"]

broker_url = f"redis://redis:{port}/3"
result_backend = f"redis://redis:{port}/4"

result_serializer = "pickle"
accept_content = [
    "application/json",
    "application/x-python-serialize",
]
result_expires = 600
task_remote_tracebacks = True
