FROM python:slim-bullseye

# https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED=1

WORKDIR /ewoksweb_app
RUN pip install ewoksweb

ARG APP_PORT=8000
EXPOSE $APP_PORT
ENV APP_PORT ${APP_PORT}

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]