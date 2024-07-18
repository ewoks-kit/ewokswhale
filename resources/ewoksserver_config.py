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
