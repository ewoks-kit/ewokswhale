FROM python:slim-bullseye

# https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED=1

WORKDIR /worker

ARG REDIS_PORT
ENV REDIS_PORT ${REDIS_PORT}

RUN pip install ewoksjob[redis,worker]

COPY celeryconfig.py .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]