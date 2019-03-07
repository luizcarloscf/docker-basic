## First stage, fetch dependencies
FROM python:3.6-alpine as build_step 

RUN apk add --update --no-cache \
    gcc                         \
    musl-dev                    \
    linux-headers

COPY requirements.txt /requirements.txt
RUN pip wheel --wheel-dir=/root/wheels -r /requirements.txt

## Second and last stage, copy dependencies and the application
FROM python:3.6-alpine as package_step

COPY . /app
WORKDIR /app

COPY --from=build_step /root/wheels /root/wheels
COPY requirements.txt /requirements.txt

RUN pip install \
    --no-index \
    --find-links=/root/wheels \
    -r /requirements.txt      


