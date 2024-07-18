#!/bin/sh

ewoksweb --config resources/ewoksserver_config.py --host 0.0.0.0 --rediscover-tasks --port $APP_PORT
