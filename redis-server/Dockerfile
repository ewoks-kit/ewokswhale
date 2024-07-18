FROM redis

WORKDIR /redis

ARG REDIS_PORT=6379
ENV REDIS_PORT ${REDIS_PORT}
EXPOSE $REDIS_PORT

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]