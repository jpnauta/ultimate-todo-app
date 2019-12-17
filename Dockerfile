FROM python:3-alpine

RUN apk -q update && \
    # Curl
    apk -q add --update curl curl-dev && \
    # OpenSSL
    apk -q --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main add openssl openssl-dev py-service_identity && \
    # PostgreSQL
    apk -q --no-cache add gcc musl-dev py-psycopg2 postgresql-dev && \
    # bash
    apk -q --no-cache add bash && \
    # Debugging
    apk -q --no-cache add nano htop postgresql-client

WORKDIR /code/

ADD requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ADD scripts/ scripts/
RUN chmod +x scripts/*
ENV PATH "$PATH:/code/scripts"

ADD runserver.py .
ADD modules/ modules/

CMD ["docker-entrypoint.sh"]
