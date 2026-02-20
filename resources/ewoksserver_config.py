import os

RESOURCE_DIRECTORY = "/ewoksweb_app/resources"

EWOKS = {
    "handlers": [
        {
            "class": "ewokscore.events.handlers.Sqlite3EwoksEventHandler",
            "arguments": [
                {
                    "name": "uri",
                    "value": "file:/ewoksweb_app/resources/ewoks_events.db",
                }
            ],
        }
    ]
}


port = os.environ["REDIS_PORT"]
CELERY = {
    "broker_url": f"redis://redis:{port}/3",
    "result_backend": f"redis://redis:{port}/4",
    "result_serializer": "pickle",
    "accept_content": [
        "application/json",
        "application/x-python-serialize",
    ],
    "result_expires": 600,
    "task_remote_tracebacks": True,
}
