FROM python:3.12.2-alpine3.19

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache pkgconfig \
                       gcc \
                       openldap \
                       gpgme-dev \
                       libc-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app .

ENV PROD=1

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]