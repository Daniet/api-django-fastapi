FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DOCKER true

RUN mkdir /server
WORKDIR /server
COPY ./ /server/
RUN pip install poetry && \
    poetry install && \
    poetry run python manage.py migrate && \
    poetry run python manage.py collectstatic --noinput
